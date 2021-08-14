from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .serializers import TodoSerializer
from .models import Todo
from django.contrib.auth.models import User


# Create your views here.

#Tutorial Django Rest Api
@api_view(['POST'])
def register(request):
    if 'username' not in request.data or 'password' not in request.data:
        return Response(
            {"message": "User needs to have a username and a password"},
            status=400)

    try:
        User.objects.create_user(
            username=request.data['username'],
            password=request.data['password'])
    except:
        try:
            User.objects.filter(username=request.data['username'])
            return Response({"message": "User exists"}, status=409)
        except:
            return Response({"message": "Impossible to create user"}, status=400)

    return Response("User created", status=201)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def task_list(request, format=None):
    tasks = Todo.objects.filter(author=request.user.username)
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def task_detail(request, id):
    task = Todo.objects.get(id=id)
    if task.author != request.user.username:
        raise PermissionDenied(
            {"message": "You don't have permission"})
    serializer = TodoSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def deleteTask(request, id):
    task = Todo.objects.get(id=id)
    if task.author != request.user.username:
        raise PermissionDenied(
            {"message": "Please pass the Token "})
    task.delete()
    return Response("Task deleted")

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create(request):
    request.data.update({"author": request.user.username})
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PATCH'])
@permission_classes((IsAuthenticated,))
def updateTask(request, id):
    task = Todo.objects.get(id=id)
    if task.author != request.user.username:
        raise PermissionDenied(
            {"message": "You don't have permission"})
    serializer = TodoSerializer(instance=task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)