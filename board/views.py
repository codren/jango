from django.shortcuts import render, redirect
from .models import Board
from fcuser.models import Fcuser
from .forms import BoardForm
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.


# 게시글 목록
def board_list(request):
    all_boards = Board.objects.all().order_by('-id')    # - 역순 의미
    # 조회해온 모든 행들을 2개씩 페이징하겠다. /?p = 값 해서 알아서 템플릿을 만드는 느낌같음. url parse도 하고.
    paginator = Paginator(all_boards, 2)
    # GET 요청 Request url에 있는 ?p 변수에 있는 값을 가져오겠다 , 만약 없다면 기본 값은 1로 하겠다.
    page = int(request.GET.get('p', 1))
    boards = paginator.get_page(page)       # p안에 있는 p번째 페이지의 항목들(행들)을 넘기겠다.
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
