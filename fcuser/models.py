from django.db import models

# Create your models here.
# DB Section


class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    useremail = models.EmailField(max_length=128, verbose_name='이메일')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        # model 클래스를 문자열로 변환하면 fcuserobject 1 이런식으로 된다.
        # 또한 다른 테이블에서 외래키로 참조하려고할 때 object라고 뜨지 않고 여기서 설정한 값이 뜬다.
        return self.username
        # 파이썬에서는 클래스가 문자열로 변환될 때 어떻게 변환될지 __str__ 내장함수를 가지고있다.

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'     # 복수단어 처리
