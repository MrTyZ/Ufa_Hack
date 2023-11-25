from rest_framework import serializers
from shop.models import Subject

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()


class SubjectsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Subject
        fields = "__all__"
