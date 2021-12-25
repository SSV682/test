from rest_framework import serializers
from ..models import *

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'
       
    def create(self, validated_data):
        isinstance = News.objects.create(**validated_data)
        isinstance.save()
        return isinstance
       
    def update(self, instance, validated_data):
        for item in validated_data:
            if News._meta.get_field(item):
                setattr(instance,item,validated_data[item])
        instance.save()
        return instance
