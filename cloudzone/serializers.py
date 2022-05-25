from rest_framework import serializers
from .models import Cloud


class CloudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloud  # cloud 모델 사용
        fields = '__all__'  # 모든 필드 포함
