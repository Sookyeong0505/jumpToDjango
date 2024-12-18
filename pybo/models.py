from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    # on_delete=models.CASCADE -> 계정 삭제 시, 이 계정이 작성한 질문을 모두 삭제한다.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')  # null=True
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가, 다대다(N:N) 관계

    # id 대신 제목으로 나옴
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modified_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
