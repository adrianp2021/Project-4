from django.contrib import admin  #we just register the model with the admin portal
from django.contrib.auth import get_user_model  #we want to register the model but need to specify which model will be used

newUser = get_user_model() #getting the current user model (my custom user and not Django default user)

admin.site.register(newUser)

# next, I will install pyjwt which will assist with generating/decoding a token