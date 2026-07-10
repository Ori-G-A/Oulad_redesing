import json

from src.domain.learning.prealgebra import (
    INTEGERS_NODE_ID,
    IRRATIONALS_NODE_ID,
    N2_HUB_NODE_ID,
    N2_RADICATION_NODE_ID,
    N2_SUBTRACTION_NODE_ID,
    N2_SUM_NODE_ID,
    N3_ASSOCIATIVE_NODE_ID,
    N3_COMMUTATIVE_NODE_ID,
    N3_HUB_NODE_ID,
    N3_IDENTITY_NODE_ID,
    N3_INVERSES_NODE_ID,
    N4_CONCEPT_NODE_IDS,
    N4_DIVISIBILITY_NODE_ID,
    N4_FACTORIZATION_NODE_ID,
    N4_GCD_NODE_ID,
    N4_HUB_NODE_ID,
    N4_LCM_NODE_ID,
    N4_MULTIPLES_NODE_ID,
    N4_PRIMES_NODE_ID,
    NATURALS_NODE_ID,
    RATIONALS_NODE_ID,
    REALS_NODE_ID,
    STAIRCASE_NODE_ID,
    TRIGGER_NODE_ID,
    WELCOME_NODE_ID,
    evaluate_interaction,
    get_lesson,
    presentation_band,
)


def test_welcome_lesson_is_safe_and_non_evaluative():
    lesson = get_lesson(WELCOME_NODE_ID)

    assert lesson is not None
    assert lesson["node_type"] == "content_intro"
    assert lesson["is_safe_zone"] is True
    assert lesson["affects_elo"] is False


def test_lesson_catalog_returns_a_copy():
    first = get_lesson(WELCOME_NODE_ID)
    first["node_type"] = "changed"

    assert get_lesson(WELCOME_NODE_ID)["node_type"] == "content_intro"


def test_presentation_band_uses_diagnostic_cuts():
    assert presentation_band(None) == "basico"
    assert presentation_band(49.9) == "basico"
    assert presentation_band(50) == "intermedio"
    assert presentation_band(79.9) == "intermedio"
    assert presentation_band(80) == "avanzado"


def test_trigger_question_is_safe_and_uses_closed_interactions():
    lesson = get_lesson(TRIGGER_NODE_ID)

    assert lesson["unlock_after"] == WELCOME_NODE_ID
    assert lesson["affects_elo"] is False
    assert all(item["type"] == "single_select" for item in lesson["interactions"])
    assert all("free_text" not in item for item in lesson["interactions"])


def test_trigger_question_feedback_is_evaluated_in_domain():
    misconception = evaluate_interaction(TRIGGER_NODE_ID, "PREALG-N1-B02-Q01", "yes")
    intuition = evaluate_interaction(TRIGGER_NODE_ID, "PREALG-N1-B02-Q02", "bread")

    assert misconception["is_expected"] is False
    assert misconception["misconception_tag"] == "cree_que_todo_numero_sirve_para_contar"
    assert intuition["is_expected"] is None
    assert intuition["feedback_key"] == "sharing_needs_fractions"
    assert evaluate_interaction(TRIGGER_NODE_ID, "PREALG-N1-B02-Q01", "free text") is None


def test_staircase_has_five_core_steps_and_optional_complex_detour():
    lesson = get_lesson(STAIRCASE_NODE_ID)

    assert lesson["unlock_after"] == TRIGGER_NODE_ID
    assert lesson["staircase"]["core_steps"] == [
        "naturals",
        "integers",
        "rationals",
        "irrationals",
        "reals",
    ]
    assert lesson["staircase"]["optional_detour"] == "complex"
    assert lesson["affects_elo"] is False


def test_staircase_feedback_distinguishes_two_misconceptions():
    replacement = evaluate_interaction(STAIRCASE_NODE_ID, "PREALG-N1-B03-Q01", "replace")
    magnitude = evaluate_interaction(STAIRCASE_NODE_ID, "PREALG-N1-B03-Q01", "bigger")

    assert replacement["misconception_tag"] == "no_reconoce_ampliacion_progresiva"
    assert magnitude["misconception_tag"] == "interpreta_conjuntos_como_categorias_aisladas"


def test_naturals_accepts_numeric_and_multiple_choice_interactions():
    total = evaluate_interaction(NATURALS_NODE_ID, "PREALG-N1-B04-Q01", "08")
    classification = evaluate_interaction(
        NATURALS_NODE_ID, "PREALG-N1-B04-Q04", "zero,four,fifteen"
    )

    assert total["selected_option"] == "8"
    assert total["is_expected"] is True
    assert classification["selected_option"] == "fifteen,four,zero"
    assert classification["is_expected"] is True


def test_naturals_feedback_identifies_zero_and_negative_misconceptions():
    excludes_zero = evaluate_interaction(
        NATURALS_NODE_ID, "PREALG-N1-B04-Q04", "four"
    )
    includes_negative = evaluate_interaction(
        NATURALS_NODE_ID, "PREALG-N1-B04-Q04", "zero,four,fifteen,negative_two"
    )

    assert excludes_zero["misconception_tag"] == "excluye_cero_de_naturales_pese_a_convencion"
    assert includes_negative["misconception_tag"] == "incluye_negativos_en_naturales"


def test_naturals_story_contract_places_definition_before_practice():
    lesson = get_lesson(NATURALS_NODE_ID)
    content = lesson["content"]

    assert content["type"] == "narrative_with_integrated_definition"
    assert content["practice_position"] == "after_definition_plus_examples"
    definition_section = content["sections"][2]
    assert definition_section["type"] == "definition_plus_examples"
    assert definition_section["is_integrated"] is True
    assert len(definition_section["examples"]) >= 2


def test_integers_distinguishes_debt_sign_and_discrete_number_line():
    positive_debt = evaluate_interaction(
        INTEGERS_NODE_ID, "PREALG-N1-B05-Q03", "positive"
    )
    line_position = evaluate_interaction(
        INTEGERS_NODE_ID, "PREALG-N1-B05-Q04", "negative_5000"
    )

    assert positive_debt["is_expected"] is False
    assert positive_debt["misconception_tag"] == "confunde_deuda_con_cantidad_positiva"
    assert line_position["is_expected"] is True
    assert line_position["feedback_key"] == "number_line_correct"


def test_integers_numeric_answers_are_canonicalized():
    debt = evaluate_interaction(INTEGERS_NODE_ID, "PREALG-N1-B05-Q01", "035000")
    balance = evaluate_interaction(INTEGERS_NODE_ID, "PREALG-N1-B05-Q02", "5000")

    assert debt["selected_option"] == "35000"
    assert debt["is_expected"] is True
    assert balance["is_expected"] is True


def test_integers_story_contract_places_definition_before_practice():
    lesson = get_lesson(INTEGERS_NODE_ID)
    content = lesson["content"]

    assert content["type"] == "narrative_with_integrated_definition"
    assert content["practice_position"] == "after_definition_plus_examples"
    definition_section = content["sections"][2]
    assert definition_section["type"] == "definition_plus_examples"
    assert definition_section["is_integrated"] is True
    assert len(definition_section["examples"]) >= 2


def test_rationals_distinguishes_fraction_order_and_decimal_type():
    share = evaluate_interaction(
        RATIONALS_NODE_ID, "PREALG-N1-B06-Q01", "three_fourths"
    )
    reversed_share = evaluate_interaction(
        RATIONALS_NODE_ID, "PREALG-N1-B06-Q01", "four_thirds"
    )
    repeating = evaluate_interaction(
        RATIONALS_NODE_ID, "PREALG-N1-B06-Q03", "repeating_0333"
    )

    assert share["is_expected"] is True
    assert reversed_share["misconception_tag"] == "confunde_numerador_denominador"
    assert repeating["is_expected"] is False
    assert repeating["misconception_tag"] == "confunde_decimal_exacto_periodico"


def test_irrationals_unlock_chain_and_criterion_interactions():
    lesson = get_lesson(IRRATIONALS_NODE_ID)

    assert lesson["unlock_after"] == RATIONALS_NODE_ID
    assert lesson["affects_elo"] is False
    # Núcleo Q01–Q03 + rejilla de clasificación (mini-reto reconstruido).
    interaction_ids = {item["interaction_id"] for item in lesson["interactions"]}
    assert {
        "PREALG-N1-B07-Q01",
        "PREALG-N1-B07-Q02",
        "PREALG-N1-B07-Q03",
    } <= interaction_ids
    assert "PREALG-N1-B07-G-pi" in interaction_ids

    # Periódico (0,333…) es la respuesta; el infinito no periódico es la trampa.
    periodic = evaluate_interaction(IRRATIONALS_NODE_ID, "PREALG-N1-B07-Q01", "periodic_0333")
    infinite = evaluate_interaction(IRRATIONALS_NODE_ID, "PREALG-N1-B07-Q01", "nonperiodic_pi")
    assert periodic["is_expected"] is True
    assert infinite["misconception_tag"] == "cree_que_todo_decimal_infinito_es_irracional"

    # Aproximación vs valor exacto de π.
    approx = evaluate_interaction(IRRATIONALS_NODE_ID, "PREALG-N1-B07-Q02", "pi_approx")
    exact = evaluate_interaction(IRRATIONALS_NODE_ID, "PREALG-N1-B07-Q02", "pi_exact")
    assert approx["is_expected"] is True
    assert exact["misconception_tag"] == "confunde_aproximacion_con_valor_exacto"

    # √2 en la recta: entre 1 y 2.
    placed = evaluate_interaction(IRRATIONALS_NODE_ID, "PREALG-N1-B07-Q03", "between_1_2")
    assert placed["is_expected"] is True
    assert placed["feedback_key"] == "sqrt2_between_correct"
    assert evaluate_interaction(IRRATIONALS_NODE_ID, "PREALG-N1-B07-Q03", "free text") is None


def test_reals_close_the_core_route_and_separate_complex_distractors():
    lesson = get_lesson(REALS_NODE_ID)

    assert lesson["unlock_after"] == IRRATIONALS_NODE_ID
    assert lesson["nucleus_closing_node"] is True
    assert lesson["affects_elo"] is False

    # Q01: la unión de racionales e irracionales forma los reales.
    union = evaluate_interaction(REALS_NODE_ID, "PREALG-N1-B08-Q01", "union_yes")
    excluded = evaluate_interaction(REALS_NODE_ID, "PREALG-N1-B08-Q01", "irr_not_on_line")
    assert union["is_expected"] is True
    assert excluded["misconception_tag"] == "no_reconoce_irracionales_como_reales"

    # Q02 (multi): el conjunto exacto de reales (orden indiferente).
    correct = evaluate_interaction(REALS_NODE_ID, "PREALG-N1-B08-Q02", "pi,sqrt2,neg4,dec075")
    assert correct["is_expected"] is True
    assert correct["feedback_key"] == "reales_correct"

    # incluir un complejo (trampa) prima sobre cualquier otro error.
    trap = evaluate_interaction(REALS_NODE_ID, "PREALG-N1-B08-Q02", "neg4,dec075,sqrt2,pi,two_i")
    assert trap["is_expected"] is False
    assert trap["misconception_tag"] == "ubica_complejos_en_recta_real"
    assert trap["feedback_key"] == "complex_not_real"

    # excluir un irracional → feedback de "faltan reales".
    missing = evaluate_interaction(REALS_NODE_ID, "PREALG-N1-B08-Q02", "neg4,dec075")
    assert missing["feedback_key"] == "irrationals_are_real"

    # opción inválida → None (nunca acepta texto/llaves desconocidas).
    assert evaluate_interaction(REALS_NODE_ID, "PREALG-N1-B08-Q02", "neg4,foo") is None


def test_naturals_multiselect_still_uses_its_specific_feedback():
    # El camino genérico no debe romper el caso especial de naturales (B04-Q04).
    excludes_zero = evaluate_interaction(NATURALS_NODE_ID, "PREALG-N1-B04-Q04", "four")
    assert excludes_zero["feedback_key"] == "zero_is_natural"


def test_level_two_hub_unlocks_after_level_one_closing_and_is_non_elo():
    lesson = get_lesson(N2_HUB_NODE_ID)

    assert lesson["unlock_after"] == "PREALG-N1-B13-CIERRE-DIAGNOSTICO"
    assert lesson["affects_elo"] is False
    assert lesson["is_safe_zone"] is True
    assert lesson["content"]["gating"]["cards_required"] == 6
    assert len(lesson["interactions"]) == 6


def test_level_two_sum_uses_integrated_definition_before_practice():
    lesson = get_lesson(N2_SUM_NODE_ID)
    content = lesson["content"]

    assert content["story_contract"]["type"] == "unified_set_extension"
    assert content["story_contract"]["practice_position"] == "after_definition_plus_examples"
    assert content["definition_katex"] == "a+b=c"
    assert content["discovery"]["body"]
    assert len(content["worked_examples"]) >= 2
    assert len(lesson["interactions"]) == 4


def test_level_two_subtraction_uses_integrated_definition_before_practice():
    lesson = get_lesson(N2_SUBTRACTION_NODE_ID)
    content = lesson["content"]

    assert content["story_contract"]["type"] == "unified_set_extension"
    assert content["story_contract"]["practice_position"] == "after_definition_plus_examples"
    assert content["definition_katex"] == "a-b=c"
    assert content["discovery"]["body"]
    assert len(content["worked_examples"]) >= 2
    assert len(lesson["interactions"]) == 4


def test_level_two_accepts_decimal_comma_for_radication():
    result = evaluate_interaction(
        N2_RADICATION_NODE_ID,
        "PREALG-N2-E06-RADICACION-RAIZ-S5",
        "7.0711",
    )

    assert result["selected_option"] == "7,0711"
    assert result["is_expected"] is True


def test_level_three_hub_and_machines_follow_storytelling_contract():
    hub = get_lesson(N3_HUB_NODE_ID)
    conmutative = get_lesson(N3_COMMUTATIVE_NODE_ID)
    identity = get_lesson(N3_IDENTITY_NODE_ID)

    assert hub["unlock_after"] == N2_RADICATION_NODE_ID
    assert hub["content"]["gating"]["machines_required"] == 5
    assert len(hub["interactions"]) == 5
    assert conmutative["unlock_after"] == N3_HUB_NODE_ID
    assert conmutative["content"]["opening_hook"]["katia_message"] == "¡Qué curioso! El orden no importa."
    assert "no tiene elemento neutro" in " ".join(identity["content"]["formalization"]).lower()


def test_level_three_accepts_decimal_comma_and_inverse_text():
    decimal = evaluate_interaction(
        N3_ASSOCIATIVE_NODE_ID,
        "PREALG-N3-M02-ASOCIATIVA-O9",
        "1.5",
    )
    inverse = evaluate_interaction(
        N3_INVERSES_NODE_ID,
        "PREALG-N3-M05-INVERSOS-O5",
        "1/5",
    )
    positive_opposite = evaluate_interaction(
        N3_INVERSES_NODE_ID,
        "PREALG-N3-M05-INVERSOS-O3",
        "+15",
    )
    rational_non_integer = evaluate_interaction(
        N3_INVERSES_NODE_ID,
        "PREALG-N3-M05-INVERSOS-O7",
        "4/3",
    )
    irrational_opposite = evaluate_interaction(
        N3_INVERSES_NODE_ID,
        "PREALG-N3-M05-INVERSOS-O8",
        "-√5",
    )

    assert decimal["selected_option"] == "1,5"
    assert decimal["is_expected"] is True
    assert inverse["is_expected"] is True
    assert positive_opposite["selected_option"] == "15"
    assert positive_opposite["is_expected"] is True
    assert rational_non_integer["is_expected"] is True
    assert irrational_opposite["selected_option"] == "-sqrt5"
    assert irrational_opposite["is_expected"] is True


def test_n3_chains_into_n4_hub():
    inverses = get_lesson(N3_INVERSES_NODE_ID)
    hub = get_lesson(N4_HUB_NODE_ID)

    assert inverses["next_node_id"] == N4_HUB_NODE_ID
    assert hub["unlock_after"] == N3_INVERSES_NODE_ID
    assert hub["content"]["gating"]["cards_required"] == 6
    assert len(hub["content"]["cards"]) == 6
    assert hub["content"]["cards"][0]["node_id"] == N4_DIVISIBILITY_NODE_ID


def test_n4_lesson_content_is_json_serializable():
    # Regresion: los items multi_select se autoraban como sets (no serializables
    # en JSON) al vivir dentro de `content`, que sí viaja al frontend.
    for node_id in (N4_HUB_NODE_ID, *N4_CONCEPT_NODE_IDS):
        lesson = get_lesson(node_id)
        json.dumps(lesson["content"])


def test_n4_divisibility_mixed_interactions():
    numeric = evaluate_interaction(N4_DIVISIBILITY_NODE_ID, f"{N4_DIVISIBILITY_NODE_ID}-Q1", "4")
    single = evaluate_interaction(N4_DIVISIBILITY_NODE_ID, f"{N4_DIVISIBILITY_NODE_ID}-Q3", "c")
    single_wrong = evaluate_interaction(N4_DIVISIBILITY_NODE_ID, f"{N4_DIVISIBILITY_NODE_ID}-Q3", "a")
    multi_correct = evaluate_interaction(N4_DIVISIBILITY_NODE_ID, f"{N4_DIVISIBILITY_NODE_ID}-Q7", "21,45,63")
    multi_trap = evaluate_interaction(N4_DIVISIBILITY_NODE_ID, f"{N4_DIVISIBILITY_NODE_ID}-Q7", "21,40,63")

    assert numeric["is_expected"] is True
    assert single["is_expected"] is True
    assert single_wrong["is_expected"] is False
    assert single_wrong["misconception_tag"] == "criterio_por_cantidad_de_digitos"
    assert multi_correct["is_expected"] is True
    assert multi_trap["is_expected"] is False
    assert multi_trap["misconception_tag"] == "confunde_criterio_de_3_con_otros_criterios"


def test_n4_enriched_concepts_mixed_interactions():
    # C02-C06 fueron enriquecidos con la misma riqueza que el piloto C01
    # (PROMPT_N4_divisibilidad.md): al menos un numeric, single_select y
    # multi_select correcto/incorrecto por nodo.
    multiples_num = evaluate_interaction(N4_MULTIPLES_NODE_ID, f"{N4_MULTIPLES_NODE_ID}-Q1", "36")
    multiples_multi = evaluate_interaction(N4_MULTIPLES_NODE_ID, f"{N4_MULTIPLES_NODE_ID}-Q6", "12,18,30")
    assert multiples_num["is_expected"] is True
    assert multiples_multi["is_expected"] is True

    primes_num = evaluate_interaction(N4_PRIMES_NODE_ID, f"{N4_PRIMES_NODE_ID}-Q2", "2")
    primes_single = evaluate_interaction(N4_PRIMES_NODE_ID, f"{N4_PRIMES_NODE_ID}-Q5", "a")
    primes_single_wrong = evaluate_interaction(N4_PRIMES_NODE_ID, f"{N4_PRIMES_NODE_ID}-Q5", "b")
    assert primes_num["is_expected"] is True
    assert primes_single["is_expected"] is True
    assert primes_single_wrong["is_expected"] is False
    assert primes_single_wrong["misconception_tag"] == "olvida_que_2_es_primo_y_par"

    factor_num = evaluate_interaction(N4_FACTORIZATION_NODE_ID, f"{N4_FACTORIZATION_NODE_ID}-Q3", "4")
    factor_multi_trap = evaluate_interaction(N4_FACTORIZATION_NODE_ID, f"{N4_FACTORIZATION_NODE_ID}-Q6", "2²×3²,6×6")
    assert factor_num["is_expected"] is True
    assert factor_multi_trap["is_expected"] is False
    assert factor_multi_trap["misconception_tag"] == "detiene_la_descomposicion_antes_de_llegar_a_primos"

    gcd_single = evaluate_interaction(N4_GCD_NODE_ID, f"{N4_GCD_NODE_ID}-Q3", "b")
    gcd_num = evaluate_interaction(N4_GCD_NODE_ID, f"{N4_GCD_NODE_ID}-Q5", "14")
    assert gcd_single["is_expected"] is True
    assert gcd_num["is_expected"] is True

    lcm_single = evaluate_interaction(N4_LCM_NODE_ID, f"{N4_LCM_NODE_ID}-Q3", "b")
    lcm_num = evaluate_interaction(N4_LCM_NODE_ID, f"{N4_LCM_NODE_ID}-Q7", "1980")
    assert lcm_single["is_expected"] is True
    assert lcm_num["is_expected"] is True


def test_n4_sequence_unlocks_sequentially():
    lessons = [get_lesson(node_id) for node_id in N4_CONCEPT_NODE_IDS]
    assert lessons[0]["unlock_after"] == N4_HUB_NODE_ID
    for previous, current in zip(lessons, lessons[1:]):
        assert current["unlock_after"] == previous["node_id"]
    assert lessons[-1]["node_id"] == N4_LCM_NODE_ID
    assert lessons[-1]["next_node_id"] is None
