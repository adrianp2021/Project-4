from django.contrib import admin # /admin 
from .models import Comment

admin.site.register(Comment)  #add ability to add this model to interact with it
