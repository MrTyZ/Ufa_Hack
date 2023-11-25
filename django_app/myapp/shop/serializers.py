from rest_framework import serializers
from shop.models import Subject

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()


class SubjectsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Subject
        fields = "__all__"

"""
 name = serializers.CharField(max_length = 255)
    description = serializers.CharField()
    price = serializers.FloatField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance
    """

