from django.db import models

class Comment(models.Model):
    text = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User",
        related_name = "comments",
        on_delete = models.CASCADE,  # if a user is deleted, all the comments will also be deleted
        default=1
    )
