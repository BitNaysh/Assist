from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Assignment
from rest_framework import serializers

from .serializers import AssignmentSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
 

class AssignmentItemViews(APIView):
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'), 
            'due_date': request.data.get('due_date'), 
            'grade': request.user.get('grade'),
            'credits': request.user.get('credits'),
        }
        serializer = AssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, *args, **kwargs):
        todos = Assignment.objects.all()
        serializer = AssignmentSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
