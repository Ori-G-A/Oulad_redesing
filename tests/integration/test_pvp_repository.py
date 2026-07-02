"""
tests/integration/test_pvp_repository.py
=========================================
Pruebas de integración de los métodos PvP del SQLiteRepository contra una DB
temporal: create_pvp_match → save_pvp_answer → finish_pvp_match → get_pvp_history.
También cubre get_course_blocks.
"""

import pytest
from src.infrastructure.persistence.sqlite_repository import SQLiteRepository


@pytest.fixture
def repo(tmp_path) -> SQLiteRepository:
    db_path = str(tmp_path / "test_pvp.db")
    return SQLiteRepository(db_name=db_path)


def _two_players(repo):
    """Registra dos estudiantes y retorna (id1, id2)."""
    repo.register_user("jugador_a", "password123", "student", education_level="universidad")
    repo.register_user("jugador_b", "password123", "student", education_level="universidad")
    a = repo.login_user("jugador_a", "password123")[0]
    b = repo.login_user("jugador_b", "password123")[0]
    return a, b


class TestPvpMatchLifecycle:
    def test_create_returns_match_id(self, repo):
        a, b = _two_players(repo)
        mid = repo.create_pvp_match("calculo_diferencial", a, b, ["i1", "i2", "i3"])
        assert isinstance(mid, int) and mid > 0

    def test_full_match_recorded_in_history(self, repo):
        a, b = _two_players(repo)
        mid = repo.create_pvp_match("calculo_diferencial", a, b, ["i1", "i2", "i3"])

        repo.save_pvp_answer(mid, a, "i1", True)
        repo.save_pvp_answer(mid, a, "i2", True)
        repo.save_pvp_answer(mid, b, "i1", False)

        # a gana 2-0
        repo.finish_pvp_match(
            match_id=mid, winner_id=a,
            score_p1=2, score_p2=0,
            elo_delta_p1=12.0, elo_delta_p2=-12.0,
            p1_id=a, p2_id=b,
        )

        hist_a = repo.get_pvp_history(a)
        assert len(hist_a) == 1
        m = hist_a[0]
        assert m["won"] is True
        assert m["draw"] is False
        assert m["my_score"] == 2
        assert m["opp_score"] == 0
        assert m["elo_delta"] == 12.0
        assert m["opponent"] == "jugador_b"

    def test_history_perspective_is_per_user(self, repo):
        """El historial del perdedor refleja SU perspectiva (su score, su delta)."""
        a, b = _two_players(repo)
        mid = repo.create_pvp_match("calculo_diferencial", a, b, ["i1"])
        repo.finish_pvp_match(
            match_id=mid, winner_id=a,
            score_p1=5, score_p2=1,
            elo_delta_p1=12.0, elo_delta_p2=-12.0,
            p1_id=a, p2_id=b,
        )
        hist_b = repo.get_pvp_history(b)
        assert len(hist_b) == 1
        m = hist_b[0]
        assert m["won"] is False
        assert m["my_score"] == 1   # b es player2 → su score es score_p2
        assert m["opp_score"] == 5
        assert m["elo_delta"] == -12.0
        assert m["opponent"] == "jugador_a"

    def test_finish_updates_current_elo(self, repo):
        a, b = _two_players(repo)
        elo_a_before = repo.get_user_by_id(a)["current_elo"]
        mid = repo.create_pvp_match("calculo_diferencial", a, b, ["i1"])
        repo.finish_pvp_match(
            match_id=mid, winner_id=a,
            score_p1=3, score_p2=0,
            elo_delta_p1=12.0, elo_delta_p2=-12.0,
            p1_id=a, p2_id=b,
        )
        assert repo.get_user_by_id(a)["current_elo"] == pytest.approx(elo_a_before + 12.0)

    def test_elo_never_negative(self, repo):
        """current_elo no baja de 0 aunque el delta sea muy negativo."""
        a, b = _two_players(repo)
        mid = repo.create_pvp_match("calculo_diferencial", a, b, ["i1"])
        repo.finish_pvp_match(
            match_id=mid, winner_id=b,
            score_p1=0, score_p2=9,
            elo_delta_p1=-99999.0, elo_delta_p2=12.0,
            p1_id=a, p2_id=b,
        )
        assert repo.get_user_by_id(a)["current_elo"] >= 0

    def test_only_finished_matches_in_history(self, repo):
        """Una partida creada pero no terminada NO aparece en el historial."""
        a, b = _two_players(repo)
        repo.create_pvp_match("calculo_diferencial", a, b, ["i1"])
        assert repo.get_pvp_history(a) == []


class TestCourseBlocks:
    def test_blocks_empty_for_unknown_course(self, repo):
        assert repo.get_course_blocks("__no_existe__") == []
