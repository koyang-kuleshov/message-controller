from rest_framework import generics


from .models import Message
from .serializers import MessageSerializer


class PostMessage(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class GetStatus(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
