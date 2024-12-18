from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    # on_delete=models.CASCADE -> 계정 삭제 시, 이 계정이 작성한 질문을 모두 삭제한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # null=True
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField(null=True, blank=True)

    # id 대신 제목으로 나옴
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField(null=True, blank=True)
