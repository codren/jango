from django.db import models

# Create your models here.
# DB Section


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', verbose_name='작성자',      # 외래키는 주키와 연결되므로 지정하지 않아도된다.
                               on_delete=models.CASCADE)  # SET.null / default 등 지정가능
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title  # model 클래스를 문자열로 변환하면 fcuserobject 1 이런식으로 된다.
        # 파이썬에서는 클래스가 문자열로 변환될 때 어떻게 변환될지 __str__ 내장함수를 가지고있다.

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'     # 복수단어 처리
