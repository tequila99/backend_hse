from drf_spectacular.utils import extend_schema
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from core.models import TaskModel


class TaskListSerializer(ModelSerializer):
    class Meta:
        model = TaskModel
        fields = (
            "id",
            "name",
            "description",
            "is_done",
        )
        read_only_fields = ("id",)


class TaskListAPIView(APIView):
    @extend_schema(
        request=TaskListSerializer,
        responses=TaskListSerializer,
        description="Создание задачи",
    )
    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=201)

    @extend_schema(
        request=None,
        responses=TaskListSerializer(many=True),
        description="Получить список задач",
    )
    def get(self, request):
        return Response(
            data=TaskListSerializer(TaskModel.objects.all(), many=True).data
        )


class TaskDetailAPIView(APIView):
    @extend_schema(
        request=None,
        responses=TaskListSerializer,
        description="Получить задачу",
    )
    def get(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)
        return Response(data=TaskListSerializer(task).data)

    @extend_schema(
        request=TaskListSerializer,
        responses=TaskListSerializer,
        description="Редактировать задачу",
    )
    def put(self, request, pk):
        task = get_object_or_404(TaskModel, pk=pk)

        serializer = TaskListSerializer(data=request.data, instance=task)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data=serializer.data)

    @extend_schema(
        request=None,
        responses=None,
        description="Удалить задачу",
    )
    def delete(self, request, pk):
        TaskModel.objects.filter(pk=pk).delete()
        return Response(status=204)
