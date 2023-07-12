from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class StudentView(APIView):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')
        if id:
            result = Student.objects.get(id=id)
            serializer = StudentSerializer(result)
            return Response({'status':'success', 'students':serializer.data}, status=200)
        else:
            result = Student.objects.all()
            serializer = StudentSerializer(result, many=True)
            return Response({'status':'success','students':serializer.data})
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, *args, **kwargs):
        id = kwargs.get('id')
        result = Student.objects.get(id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', 'data':serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', 'data':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, id=None):
        student = Student.objects.filter(id=id)
        student.delete()
        return Response({'status':'success', 'data':'record deleted'})