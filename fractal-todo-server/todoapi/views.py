from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Bucket, Todo
from .serializers import BucketSerializer, TodoSerializer


class BucketList(APIView):
    def get(self, request):
        buckets = Bucket.objects.all()
        data = BucketSerializer(buckets, many=True).data
        return Response({
            "count": len(data),
            "buckets": data
        })

    def post(self, request):
        bucket_data = JSONParser().parse(request)
        data = BucketSerializer(data=bucket_data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class BucketDetail(APIView):
    def get(self, request, id):
        try:
            bucket = Bucket.objects.get(pk=id)
            data = BucketSerializer(bucket).data
            return Response(data)
        except Bucket.DoesNotExist:
            return Response({'message': 'The Bucket does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            bucket = Bucket.objects.get(pk=id)
            bucket.delete()
            return Response({'message': 'Bucket successfully Deleted'}, status=200)
        except Bucket.DoesNotExist:
            return Response({'message': 'The Bucket does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            Bucket.objects.get(pk=id)
            bucket_data = JSONParser().parse(request)
            data = BucketSerializer(data=bucket_data)
            if data.is_valid():
                data.save()
                return Response({'message': 'Bucket successfully Updated'}, status=200)
            else:
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Bucket.DoesNotExist:
            return Response({'message': 'The Bucket does not exist'}, status=status.HTTP_404_NOT_FOUND)


class TodoBucketDetail(APIView):
    def get(self, request, id):
        try:
            bucket = Bucket.objects.get(pk=id)
            todos = Todo.objects.filter(bucket_id=id)
            bucket_data = BucketSerializer(bucket).data
            todo_data = TodoSerializer(todos, many=True).data
            return Response({
                "bucket": bucket_data,
                "todos": todo_data
            })
        except Bucket.DoesNotExist:
            return Response({'message': 'The Bucket does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, id):
        todo_data = JSONParser().parse(request)
        todo_data['bucket_id'] = id
        data = TodoSerializer(data=todo_data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    def get(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
            data = TodoSerializer(todo).data
            return Response(data)
        except Todo.DoesNotExist:
            return Response({'message': 'The Todo does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
            todo.delete()
            return Response({'message': 'Todo successfully Deleted'}, status=200)
        except Todo.DoesNotExist:
            return Response({'message': 'The Todo does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        try:
            Todo.objects.get(pk=id)
            todo_data = JSONParser().parse(request)
            data = TodoSerializer(todo_data, data=todo_data)
            if data.is_valid():
                data.save()
                return Response({'message': 'Todo successfully Updated'}, status=200)
            else:
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response({'message': 'The Todo does not exist'}, status=status.HTTP_404_NOT_FOUND)


class TodoDoneToggle(APIView):
    def get(self, request, id):
        try:
            todo = Todo.objects.get(pk=id)
            data = TodoSerializer(todo, data={"done": False if todo.done else True}, partial=True)
            if data.is_valid():
                data.save()
                return Response({'message': 'Todo successfully Updated'}, status=200)
            else:
                return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response({'message': 'The Todo does not exist'}, status=status.HTTP_404_NOT_FOUND)
