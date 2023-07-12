from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    address = serializers.CharField(max_length=500,required=True)
    mobile_num = serializers.CharField(max_length=10,required=True)

    class Meta:
        model = Student
        fields = ('__all__')