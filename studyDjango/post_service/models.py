from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # 1. 게시물의 고유한 인덱스는 models.Model 에 기본으로 포함되는 pk를 이용
    # 2. 게시물의 제목, 1024자 제한
    title = models.CharField(max_length=1024)
    # 3. 게시물의 내용, 4069자 제한
    body = models.CharField(max_length=4069)
    # 4. 게시물의 작성자는 django의 기본 User를 활용
    author = models.ForeignKey(User)
    # 5. 게시물의 작성시간, 자동으로 게시물이 등록되는 시간이 설정 되도록
    regdate = models.DateTimeField(auto_created=True, auto_now_add=True)
    # 6. 게시물의 고유 비밀번호는 author의 권한 인증을 따름