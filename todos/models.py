from django.db import models


# Create your models here.
# dev_2
class Todo(models.Model):  # models를 상속 받음
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # ''
    created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.description  # 게시글의 내용을 썸네일로 한다.
