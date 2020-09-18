from rest_framework import serializers
from api import models

class InstituteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    #nested serializer institute in Student
    institute = InstituteSerializers(read_only=True)
    class Meta:
        model = models.Student
        fields = '__all__'