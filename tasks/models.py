from django.db import models
from django.db.models import Q


class Task(models.Model):

    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    schedule = models.CharField(max_length=128)

    @staticmethod
    def get_hour_target(datetime):
        return f'H{datetime.hour:02d}'

    @staticmethod
    def get_weekday_target(datetime):
        return f'WD{datetime.isoweekday()}'

    @classmethod
    def get_datetime_tasks(cls, datetime):

        hh_target = cls.get_hour_target(datetime)
        wd_target = cls.get_weekday_target(datetime)

        return cls.objects.filter(
            Q(schedule__contains=hh_target) &
            Q(schedule__contains=wd_target))

    def __str__(self):
        return f'{self.name} ({self.id})'


class TaskResult(models.Model):

    STATUS_PENDING = 'PENDING'
    STATUS_DONE = 'DONE'
    STATUS_CANCELED = 'CANCELED'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_DONE, 'Done'),
        (STATUS_CANCELED, 'Canceled'),
    )

    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return f'{self.get_status_display()} ({self.id})'
