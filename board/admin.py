from django.contrib import admin
from .models import Board      # 현재 디렉토리에 있는 models.py에 있는 Fcuser 클래스 import

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    # 이렇게 지정하면 user들 목록을 보여줄 때 각 항목을 보여준다
    list_display = ('title',)   # 튜플로 보내줄때 한개 값은 , 꼭 해주기


admin.site.register(Board, BoardAdmin)
