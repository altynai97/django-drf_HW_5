from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Courses, Students, Mentors
from .serializers import CoursesSerializer, StudentsSerializer, MentorsSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class StudentsGenericView(generics.GenericAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer


class MentorsAPIView(APIView):
    def get(self, request):
        mentors = Mentors.objects.all()
        serializer = MentorsSerializer(mentors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MentorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



