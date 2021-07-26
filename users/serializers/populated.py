from comments.serializers.common import CommentSerializer
from .common import UserSerializer
from interests.serializers.common import InterestSerializer

class PopulatedUserSerializer(UserSerializer):
    comments = CommentSerializer(many=True)  #adding a field to User object called comment
    interests = InterestSerializer(many=True)