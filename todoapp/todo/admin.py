from django.contrib import admin
from .models import Todo

# Register your models here.

# todo 모델을 등록하는 코드
admin.site.register(Todo)