from django.db import models

# Create your models here.
# Django가 PK필드를 제공하기 때문에 따로 선언하지 않아도 된다.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title