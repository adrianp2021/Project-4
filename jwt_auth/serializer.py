from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):

        #remove the password and password confirmation from the req body so that it is not stored in db
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')

        # checking if passwords match
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'Passwords do not match'})

        # if passing this check, we need to check that password is valid
        try: 
            password_validation.validate_password(password=password)  # this method looks at what Django expects from a password, see if password passing in meets requirements (if yes, goes through, if not, throw error)
        except ValidationError as err:
            raise ValidationError({'password': err.messages})

        # now, the password must be hashed and add back to the dictionary (to be stored in db; before storing in db, password must always be hashed)
        data['password'] = make_password(password)

        return data 

    class Meta:
      model = user
      fields = '__all__'

  
    # define which fields I dont want to go through serializer and not be included in db
    #inside the validate functions, remove both fields (password and password_confirmation) from data dictionary
    #check if passwords match, if not, throw error
    #if they match, check if password is valid and in the format Django expects it to be(password=password)
    #if missing characters or any other errors, missing special characters, throw except block and throw error
    #if passing validation, hash password and add to a new key of password on the dictonary
