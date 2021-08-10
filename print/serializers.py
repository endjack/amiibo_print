from rest_framework import serializers
from .models import Amiibo

class AmiiboSerializer(serializers.ModelSerializer):

    class Meta:

        model = Amiibo
        fields = '__all__'