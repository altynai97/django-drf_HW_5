from django.urls import path

from . import views

urlpatterns = [
    path('mentors/', views.MentorsAPIView.as_view()),
    path('viewset/courses/', views.CoursesViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),



]