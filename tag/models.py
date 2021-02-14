from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')

    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        # model 클래스를 문자열로 변환하면 fcuserobject 1 이런식으로 된다.
        # 또한 다른 테이블에서 외래키로 참조하려고할 때 object라고 뜨지 않고 여기서 설정한 값이 뜬다.
        return self.name
        # 파이썬에서는 클래스가 문자열로 변환될 때 어떻게 변환될지 __str__ 내장함수를 가지고있다.

    class Meta:
        db_table = 'fastcampus_tag'
        verbose_name = '패스트캠퍼스 태그'
        verbose_name_plural = '패스트캠퍼스 태그'     # 복수단어 처리
