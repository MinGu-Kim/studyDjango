from django.contrib import auth
from django.shortcuts import render, redirect
from django.template import Context
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.http.response import HttpResponse

from post_service.forms import LoginForm
from post_service.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
'''
Django 에서 View는‘어떤 데이터를 보여줄 것인가?’에 집중
다시 말해, 데이터들을 모아서 Template 에 보내주고, 그 결과를 사용자에게 보여주는 역할
'''
def post_list(request):
    template = get_template("post_list.html")

    page_data = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')

    if page is None:
        page = 1
    try:
        posts = page_data.page(page)
    except PageNotAnInteger:
        posts = page_data.page(1)
    except EmptyPage:
        posts = page_data.page(page_data.num_pages)

    context = Context({'post_list' : posts, 'current_page' : int(page), 'total_page': range(1, page_data.num_pages+1)})

    return HttpResponse(template.render(context))

def login(request):
    template = get_template('login_form.html')

    context = Context({'login_form' : LoginForm()})
    context.update(csrf(request))

    return HttpResponse(template.render(context))

def login_validate(request):
    # 여기서 로그인 처리!!
    login_form_data = LoginForm(request.POST)
    print(login_form_data.data)
    if login_form_data.is_valid():
        # 로그인 정보 일치
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])
        if user.is_active:
            auth.login(request, user)

            return redirect('/board')
        else:
            return HttpResponse("사용자가 없거나 비밀번호를 잘못 입력하셨습니다.")
    else:
        return HttpResponse("로그인 폼이 비정상 입니다.")
    return HttpResponse("알 수 없는 오류 입니다.")