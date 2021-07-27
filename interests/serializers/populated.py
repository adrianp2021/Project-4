from users.serializers.common import UserSerializer
from .common import InterestSerializer

class PopulatedInterestSerializer(InterestSerializer):
    users = UserSerializer(many=True)
