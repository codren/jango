from django.shortcuts import render, redirect
from .models import Board
from fcuser.models import Fcuser
from .forms import BoardForm
from django.http import Http404

# Create your views here.


# 게시글 목록
def board_list(request):
    boards = Board.objects.all().order_by('-id')    # - 역순 의미
    return render(request, 'board_list.html', {'boards': boards})


# 게시글 작성
def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            # writer = models.ForeignKey('fcuser.Fcuser', 모델에서 이렇게 정의했기 때문에 그것에 해당하는 인스턴스를 주면 그것의 값을 참조해서 값을 저장? 조회? 그런듯
            board.writer = fcuser
            board.save()

            return redirect('/board/list')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


# 게시글 (상세)보기

# /board_detail/1 2 3 4 이런식으로 주소에 값을 넣어서 요청하게 만들어야함 why? 어떤 게시글인지 구분하기위해
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})
