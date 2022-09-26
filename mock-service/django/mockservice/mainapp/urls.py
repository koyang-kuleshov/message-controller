from django.urls import path

from .views import PostMessage, GetStatus

urlpatterns = [
    path("post/message", PostMessage.as_view(), name="post-message"),
    path("get/status", GetStatus.as_view(), name="get-status"),
    ]

