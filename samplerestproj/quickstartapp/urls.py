from .views import StudentView
from django.urls import path

urlpatterns= [
    path('students/', StudentView.as_view()),
    path('students/<int:id>/', StudentView.as_view())

]