from rest_framework import serializers
from .models import Courses, Students, Mentors


class CoursesSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    course_duration = serializers.IntegerField()
    student = serializers.CharField(max_length=25)
    mentor = serializers.CharField(max_length=25)

    class Meta:
        model = Courses
        fields = '__all_'

    def create(self, validated_data):
        return Courses.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.course_duration = validated_data['course_duration']
        instance.student = validated_data['student']
        instance.mentor = validated_data['mentor']
        instance.save()
        return instance


class StudentsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()

    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        return Students.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.birth_date = validated_data['birth_date']
        instance.save()
        return instance


class MentorsSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=25)
    experience = serializers.IntegerField()

    class Meta:
        model = Students
        fields = '__all__'

    def create(self, validated_data):
        return Mentors.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.fullname = validated_data['fullname']
        instance.experience = validated_data['experience']
        instance.save()
        return instance

