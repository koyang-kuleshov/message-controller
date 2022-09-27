from django.urls import path

from .views import get_status, PostMessage

urlpatterns = [
    path("post/message", PostMessage.as_view(), name="post-message"),
    path("get/status", get_status, name="get-status"),
    ]

