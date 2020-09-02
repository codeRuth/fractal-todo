from django.db import models


class Bucket(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Todo(models.Model):
    bucket_id = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()

    def __str__(self):
        return self.name
