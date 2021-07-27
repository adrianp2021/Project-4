from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers.common import InterestSerializer
from .models import Interest

class InterestListView(APIView):

    def get(self, _request):
        interests = Interest.objects.all()
        serialized_interests = InterestSerializer(interests, many=True)
        return Response(serialized_interests.data, status=status.HTTP_200_OK)
