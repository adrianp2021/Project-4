from django.http import JsonResponse, request

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound

from .models import User
from .serializers.common import UserSerializer
from .serializers.populated import PopulatedUserSerializer

class UserListView(APIView):

    def get(self, _request):
        users = User.objects.all() # get everything from the shows table in the db
        serialized_users = PopulatedUserSerializer(users, many=True) # transform data into python by running through serializer
        return Response(serialized_users.data, status=status.HTTP_200_OK) # return data and status code



    def post(self, request):
      # print('Requesting data', request.data)
        user_to_add = UserSerializer(data=request.data)
        if user_to_add.is_valid():
            user_to_add.save()
            return Response(user_to_add.data, status=status.HTTP_201_CREATED)
        return Response(user_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class UserDetailView(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(detail="🆘 Cannot find this user")

    def get(self, _request, pk):
        user = self.get_user(pk=pk)
        serialized_user = PopulatedUserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)

    def delete(self, _request, pk):
        user_to_delete = self.get_user(pk=pk)
        user_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    

    def put(self, request, pk):
        user_to_edit = self.get_user(pk=pk)
        updated_user = UserSerializer(user_to_edit, data=request.data)
        if updated_user.is_valid():
          updated_user.save()
          return Response(updated_user.data, status=status.HTTP_202_ACCEPTED)
        return Response(updated_user.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)