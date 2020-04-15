from rest_framework.serializers import ModelSerializer
from realjobs.models import JobOffer


class JobOfferSerializer(ModelSerializer):
    class Meta:
        model = JobOffer
        fields = "__all__"



