from django.contrib import admin
from .models import Tag      # 현재 디렉토리에 있는 models.py에 있는 Tag 클래스 import

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tag, TagAdmin)
