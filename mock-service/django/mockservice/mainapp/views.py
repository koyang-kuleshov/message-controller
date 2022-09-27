from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer


class PostMessage(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response({"message": "Message added in queue",
                         "status": 202
                         })


@api_view()
def get_status(request):
    queryset = Message.objects.filter(user_id=request.user.id)
    data = []
    for message in queryset:
        data.append({"id": message.id,
                     "Number of message(s)": message.get_message_quantity})
    return Response({
                        "message": f"Messages for user {request.user.username}",
                        "data": data,
                     }
    )
