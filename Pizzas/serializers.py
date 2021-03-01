from rest_framework import serializers
from .models import Pizza

class pizzaSerializers(serializers.ModelSerializer):

    class Meta:
        model=Pizza
        fields='__all__'
