from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework.views import APIView

from .filters import TodoFilter
from .models import  Todo
from rest_framework import status
from rest_framework.response import Response
from .serializers import  TodoSerializer
from rest_framework.permissions import IsAuthenticated

class TodoView(APIView):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TodoFilter
    ordering_fields = ['title', 'user__name']

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        queryset = Todo.objects.all()

        # Применение фильтров
        filterset = TodoFilter(request.GET, queryset=queryset)
        queryset = filterset.qs

        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)



    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)