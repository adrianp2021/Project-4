from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .serializers.common import CommentSerializer

class CommentListView(APIView):
    permission_classes = (IsAuthenticated)
    
    def post(self, request):
        request.dara["owner"] = request.user.id
        comment_to_create = CommentSerializer(data=request.data)
        if comment_to_create.is_valid():
            comment_to_create.save()
            return Response(comment_to_create.data, status=status.HTTP_201_CREATED)
        return Response(comment_to_create.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class CommentDetailView(APIView):

    def delete(self, request, pk):
        try: 
            comment_to_delete = Comment.objects.get(pk=pk)  #this will find the comment
        except Comment.DoesNotExist:
            raise NotFound()
        if comment_to_delete.owner != request.user:
            raise PermissionDenied()
        comment_to_delete.delete()  #this will in fact delete that comment
        return Response(status=status.HTTP_204_NO_CONTENT)
