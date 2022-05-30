from rest_framework import serializers
from .models import Cloud, NonSmokingArea, SmokingArea


class CloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloud  # cloud 모델 사용
        fields = '__all__'  # 모든 필드 포함


class NonSmokingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonSmokingArea
        fields = '__all__'


class SmokingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmokingArea
        fields = '__all__'
