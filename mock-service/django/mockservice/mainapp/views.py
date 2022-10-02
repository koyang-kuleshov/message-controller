import os
from random import randint
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer


class PostMessage(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        percent = int(os.environ.get("PERCENT_OF_GOOD_RESPONSE"))
        if randint(1, 100) < percent:
            return Response({"message": ("Message added in queue with id "
                                         f"{response.data['id']}"),
                             "status": 202
                             })
        return Response("Service unavailable",
                        status=status.HTTP_503_SERVICE_UNAVAILABLE
                        )


@api_view()
def get_status(request):
    queryset = Message.objects.filter(user_id=request.user.id)
    data = []
    for message in queryset:
        data.append({"id": message.id,
                     "Number of message(s)": message.number_of_message})
    return Response({
                        "message": f"Messages for user {request.user.username}",
                        "data": data,
                     }
    )
