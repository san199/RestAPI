from dataclasses import fields
from rest_framework import serializers
from datetime import datetime
from app_restapi.models import AppPost

class AppPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppPost
        fields = ['id','video_title', 'video_desc', 'video_by','video_created_at']