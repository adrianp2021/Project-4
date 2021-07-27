#here, I will check whether a user is authenticated or not.
# from jwt import algorithms
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import PermissionDenied   
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt

newUser = get_user_model()

class JWTAuthentication(BasicAuthentication):
    def authenticate(self, request):
        #taking the token from the request -> as the req comes in, it has a header object with a token and information about the req from the user; it will look at the object and find the key of authorization(if found, then token has been sent in, if not then is nothing attached to header which may be useful, hence None will be returned)
        header = request.headers.get('Authorization')

        # if not token is found in the header, return None
        if not header:
            return None

        #next, if the token is is the incorrect format, throw an error (if the header that comes in does not start with the word 'bearer', then throw error; it's not the format that is expected)
        if not header.startswith('Bearer'):
            raise PermissionDenied(detail="Invalid token")

        #conversely, if token starts with 'Bearer', need to remove and replace with empty strings
        token = header.replace('Bearer ', '')

        #once the token is found, it must be decoded
        try:
            #this will pull out the payload itself so I can get information about the user and find him/her in db. decode token to get payload (info about user that lives on the token), needs the token and algorithms
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])  #1 arg is token itself, 2 arg is the secret and 3 arg is the algorithm used when it was encoded originally.
            print('PAYLOAD', payload)

            # use the 'sub' from the payload to search the DB for a matching user
            user = newUser.objects.get(pk=payload.get('sub'))
        #now, I do the exceptions
        except jwt.exceptions.InvalidTokenError:   #if for whatever reason, token is invalid or has any issues while decoding, throw an error
            raise PermissionDenied(detail="Invalid token")
        except newUser.DoesNotExist:               #if an issue with finding the user appears, throw an error
            raise PermissionDenied(detail="User not found")

        #if token is valid, 
        return(user, token)

        #hence, I check whether there are req headers and if they have a token on incoming req; if none, throw error and stop it, else I go to check if it starts with word Bearer(if it doesnt, throw error; if it does carry on)
        #replace the bearer and the space with empty string to have access to token
        #if it goel well, in the try except, I grab the payload from token -> decode token to grab it
        #token is object that hold info about user
        #once I have payload from user, I can use unique identifier to find user in db; 
        #if token is invalid, throw an error
        #if cant find user to match the payload, throw error
        #if all good, return user and token -> and permission will be granted