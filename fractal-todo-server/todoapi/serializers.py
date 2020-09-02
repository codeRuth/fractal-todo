from rest_framework import serializers

from .models import Bucket, Todo


class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucket
        fields = ('id', 'name', 'created_at', 'color')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'bucket_id', 'name', 'created_at', 'done')
