"""Los WebSockets deben validar cuenta, rol y alcance del recurso solicitado."""

import pytest
from starlette.websockets import WebSocketDisconnect


def test_notification_room_accepts_owner(api_client, student_token, student_headers):
    user_id = api_client.get("/api/auth/me", headers=student_headers).json()["user_id"]
    with api_client.websocket_connect(f"/api/ws/notifications/student_{user_id}") as socket:
        socket.send_json({"token": student_token})
        assert socket.receive_json() == {
            "type": "connected",
            "room": f"student_{user_id}",
        }


def test_notification_room_rejects_another_account(api_client, student_token, teacher_headers):
    teacher_id = api_client.get("/api/auth/me", headers=teacher_headers).json()["user_id"]
    with api_client.websocket_connect(f"/api/ws/notifications/teacher_{teacher_id}") as socket:
        socket.send_json({"token": student_token})
        with pytest.raises(WebSocketDisconnect) as closed:
            socket.receive_json()
        assert closed.value.code == 4003


def test_pvp_rejects_course_without_enrollment(api_client, student_token):
    with api_client.websocket_connect("/api/ws/pvp/curso-inexistente") as socket:
        socket.send_json({"token": student_token})
        with pytest.raises(WebSocketDisconnect) as closed:
            socket.receive_json()
        assert closed.value.code == 4001
