from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Assignment
from .serializers import AssignmentSerializer

@api_view(['GET'])
def get_assignments(request):
    assignments = Assignment.objects.all()
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_assignment(request):
    serializer = AssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    serializer = AssignmentSerializer(instance=assignment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_assignment(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    assignment.delete()
    return Response(status=204)
