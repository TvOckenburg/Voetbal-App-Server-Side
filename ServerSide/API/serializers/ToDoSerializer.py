from rest_framework import serializers
from API.models import *

myVars = vars()


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ["task", "completed", "timestamp", "updated", "user"]
