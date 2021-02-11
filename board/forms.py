from django import forms
from django.contrib.auth.hashers import check_password


class BoardForm(forms.Form):    # forms.Form 상속받음

    title = forms.CharField(
        error_messages={
            'required': '제목을 입력해주세요'
        }, max_length=128, label="제목")

    contents = forms.CharField(         # DB는 TextField로 되어있는데 TextField 지정시 오류남 왜지..? AttributeError: module 'django.forms' has no attribute 'TextField'
        error_messages={                # model에서 컬럼 type length 지정할 때 textfield는 text를 받지만 제한 길이는 없는 것을 의미하고
                                        # form. 에서는 문자냐 아니냐 이런식으로만 판단해서 CharField만 존재하는듯?
            'required': '내용을 입력해주세요'
        }, widget=forms.Textarea,  label="내용")    # widget에는 TextField 없음 Textarea 존재
    # widget=forms.Textarea 없어도 되는듯 어차피 이미 템플릿에서 textarea로 해줫기 때문에
