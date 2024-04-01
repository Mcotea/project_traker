from django.db import models

from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = (
        ('New', 'Новая'),
        ('In_progress', 'В работе'),
        ('Completed', 'Завершена'),
    )

    PRIORITY_CHOICES = (
        ('Low', 'Низкий'),
        ('Average', 'Средний'),
        ('Height', 'Высокий'),
        ('Very_height', 'Очень высокий'),
        ('Critical', 'Критический'),
    )

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    description = models.TextField()
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='test',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New',
    )

    priority = models.CharField(
        max_length=50,
        default='Average',
        choices=PRIORITY_CHOICES,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    STATUS_CHOICES = (
        ('Under_consideration', 'На рассмотрении'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    )
    PRIORITY_CHOICES = (
        ('Low', 'Низкий'),
        ('Average', 'Средний'),
        ('Height', 'Высокий'),
        ('Very_height', 'Очень высокий'),
        ('Critical', 'Критический'),
    )
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    description = models.TextField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Under_consideration',
    )
    priority = models.CharField(
        max_length=50,
        default='Average',
        choices=PRIORITY_CHOICES,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
