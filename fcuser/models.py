from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username  # model 클래스를 문자열로 변환하면 fcuserobject 1 이런식으로 된다.
        # 파이썬에서는 클래스가 문자열로 변환될 때 어떻게 변환될지 __str__ 내장함수를 가지고있다.

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'     # 복수단어 처리
