from django.contrib.auth.models import User
from rest_framework import serializers
from webapp.models import Status, Type, Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'users')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    type = TypeSerializer()
    project = ProjectSerializer()

    class Meta:
        model = Task
        fields = ('id', 'summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at')