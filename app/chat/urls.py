from django.urls import path

from .views import ChatMessageList, ChatRoomList, show_html

urlpatterns = [
    path("room/", ChatRoomList.as_view(), name="room-list"),
    path("<int:room_id>/messages", ChatMessageList.as_view(), name="message-list"),
    path("chatting", show_html, name="chatting"),
]
