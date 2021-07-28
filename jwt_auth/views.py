from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .serializer import UserSerializer


newUser = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        user_to_create = UserSerializer(data=request.data)  # when taking JSON in, needs to be serialized first and sent to db
        print('user to create', request.data)
        if user_to_create.is_valid():
            user_to_create.save()
            return Response({ 'message': 'Registration successful'}, status=status.HTTP_202_ACCEPTED)
        print('user to create errors', user_to_create.errors)
        return Response(user_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class LoginView(APIView):

    def post(self, request):
        #check if there is a user in db with the email user is trying to login with (email will be used as unique identifier, secondly, check if password is correct, Django will decode it, check it matches with password that exists in db; return error if its not the case). lastly, generate a token, so user can be identified; return token to client 
        email = request.data.get('email')
        password = request.data.get('password')
        print('request', request.data)
        try: 
            user_to_login = newUser.objects.get(email=email)
            print('user to login', user_to_login)
        except newUser.DoesNotExist:
            print('new user', newUser)
            raise PermissionDenied(detail='Invalid Credentials')
        if not user_to_login.check_password(password):
            raise PermissionDenied(detail='Invalid Credentials')

        dt = datetime.now() + timedelta(days=7)
        token = jwt.encode(
          {'sub': user_to_login.id, 'exp': int(dt.strftime('%s'))},
          settings.SECRET_KEY,
          algorithm='HS256'
        )
        return Response({ 'token': token, 'message': f"Good to see you again {user_to_login.username}" })
