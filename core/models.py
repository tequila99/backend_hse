from django.db import models


class Status(models.TextChoices):
    PENDING = "pending", "В ожидании"
    IN_PROGRESS = "in_progress", "В работе"
    CANCELLED = "cancelled", "Отменено"
    DONE = "done", "Выполнено"


class TaskModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    deadline = models.DateTimeField(verbose_name="Контрольный срок")
    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name="Статус",
    )
