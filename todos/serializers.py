from django import forms
from .models import Todo
from rest_framework import serializers


# # dev_3
# Form: db로 연결
# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Todo
#         fields = ("title", "description", "important")


# dev_7
# serializers
class TodoDRFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        # 컬럼명
        fields = ("id", "title", "description", "created", "complete", "important")
