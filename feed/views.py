from rest_framework.views import APIView
from rest_framework.response import Response


class FirstView(APIView):

    def get(self, request):
        return Response(request.user.username)