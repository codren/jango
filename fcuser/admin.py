from django.contrib import admin
from .models import Fcuser      # 현재 디렉토리에 있는 models.py에 있는 Fcuser 클래스 import

# Register your models here.


class FcuserAdmin(admin.ModelAdmin):
    # 이렇게 지정하면 user들 목록을 보여줄 때 각 항목을 보여준다
    list_display = ('username', 'password', 'useremail')


admin.site.register(Fcuser, FcuserAdmin)
