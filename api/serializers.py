from django.contrib.auth.models import User
from rest_framework import serializers
from webapp.models import Status, Type, Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypesSerializers(serializers.Serializer):
    class StatusSerializer(serializers.ModelSerializer):
        class Meta:
            model = Type
            fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'