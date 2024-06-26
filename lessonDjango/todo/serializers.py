from rest_framework import serializers
from .models import Todo
from django.contrib.auth import get_user_model

User = get_user_model()

class TodoSerializer(serializers.ModelSerializer):
    display_title = serializers.SerializerMethodField()


    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'isDone', 'user', 'display_title']

    def get_user_name(self, obj):
        return obj.user.name if obj.user else None

    def get_display_title(self, obj):
        return f"{obj.title} - Created by {self.get_user_name(obj)}"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['display_title'] = self.get_display_title(instance)
        return representation
