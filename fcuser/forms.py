from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):    # forms.Form 상속받음

    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요'
        }, max_length=32, label="사용자이름")

    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요'
        }, widget=forms.PasswordInput,  label="비밀번호")

    def clean(self):            # 상속 받은 부모의 함수를 오버라이딩함.
        # 오버라이딩 했기 때문에 부모의 clean 기능을 사용하기 위해 호출하고 자신만의 clean 기능사용할 것임.
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                # 중요!!!!!! form = LoginForm() 으로 클래스 인스턴스화 시킬 시 self 인스턴스 변수이므로 접근가능
                self.user_id = fcuser.id
