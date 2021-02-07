from django.shortcuts import render
from .models import Fcuser
from django.http import HttpResponse    # 프론트엔드에서 사용자에게 보여줄 응답
from django.contrib.auth.hashers import make_password   # 비밀번호 해쉬화
# Create your views here.
# Backend Section


def register(request):
    # 기본적으로 templates 폴더를 바라봄 안에 register.html에 접근

    # 1. 회원가입 홈페이지 요청과
    # 2. 회원가입 정보 입력후 등록 요청 존재

    # 1.
    if request.method == 'GET':
        return render(request, 'register.html')
    # 2.
    elif request.method == 'POST':

        # 1번 방법 get 이용
        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)
        # re_password = request.POST.get('re-password', None)

        # 2번 방법 기본

        useremail = request.POST['useremail']
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        # 1번 2번 둘다 사용가능 원래 키 값에 밸류가 없으면 혹은 키 자체가없으면 error가 나는데 get을 이용하면 none이 출력된다.
        # 하지만 1번 방법에는 키 값에 '' 공백'값'이 들어가게 되서(혹은 그렇게 예외처리되서?) 오류가 나지 않는다. ''= false를 의미함

        res_data = {}

        if not (username and password and re_password and useremail):
            res_data['error'] = '모든 항목에 값을 입력해야합니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'

            # register.html 을 그대로 보내주지만 메시지로 바꿈
            # return HttpResponse('비밀번호가 일치하지 않습니다.')

        elif password == re_password:
            fcuser = Fcuser(        # 인스턴스 생성
                useremail=useremail,
                username=username,
                password=make_password(password)
            )
            fcuser.save()           # 인스턴스 저장

        return render(request, 'register.html', res_data)
