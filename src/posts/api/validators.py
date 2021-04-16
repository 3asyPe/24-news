from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class CreateProductSerializer(serializers.Serializer):
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    name = serializers.CharField()

    def validate_description(self, value):
        if len(value) < 10:
            raise ValidationError("Description is too small")
