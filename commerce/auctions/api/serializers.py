from rest_framework.serializers import ModelSerializer
from auctions.models import Listing

class IhaSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields ='__all__'