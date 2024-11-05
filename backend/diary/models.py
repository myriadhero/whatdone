from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()


class Tags(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class ActivityType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title


class Entry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    timestamp = models.DateField()
    duration = models.DurationField(blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    goal = models.ForeignKey(
        Goal,
        on_delete=models.PROTECT,
        blank=True,
        limit_choices_to={"user": user},
    )
    activity_type = models.ForeignKey(
        ActivityType,
        on_delete=models.PROTECT,
        blank=True,
    )
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title
