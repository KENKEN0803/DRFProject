from django.db import models


class TodoList(models.Model):
    seq = models.AutoField(primary_key=True)
    author = models.CharField(max_length=140, null=False)
    contents = models.TextField(null=True)
    completed = models.BooleanField(default=False)
    writtenTime = models.TimeField(default="00:00:00")
    deleted = models.BooleanField(default=False)
    # user = models.ForeignKey("Users")


# class Users(models.Model):
#     seq = models.AutoField(primary_key=True)
#     author = models.CharField(max_length=140, null=True)
#     password = models.CharField(max_length=1000, null=False)
