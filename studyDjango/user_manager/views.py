from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.http.response import HttpResponse
from user_manager.forms import *

# Create your views here.


def login(request):
    template = get_template('login_form.html')

    context = Context({'login_form' : LoginForm()})
    context.update(csrf(request))

    return HttpResponse(template.render(context))

def login_validate(request):
    # 여기서 로그인 처리!!
    print(request.method)
    login_form_data = LoginForm(request.GET)
    print(login_form_data.data)
    if login_form_data.is_valid():
        # 로그인 정보 일치
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])
        if user != None:
            auth.login(request, user)

            return redirect('/board')
        else:
            return HttpResponse("사용자가 없거나 비밀번호를 잘못 입력하셨습니다.")
    else:
        return HttpResponse("로그인 폼이 비정상 입니다.")
    return HttpResponse("알 수 없는 오류 입니다.")

def join_page(request):
    # POST 방식으로 넘어온 데이터에 대해서만 회원가입 처리
    if request.method == 'POST':
        form_data = JoinForm(request.POST)
        print(form_data.is_valid())
        if form_data.is_valid():
            # 별 문제가 없다면, 회원가입 ㄱㄱ
            username = form_data.cleaned_data['id']
            password = form_data.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            # 로그인 폼으로 이동
            return redirect('/user/login/')
    else:
        # 만약 GET 방식 등으로 넘어온 데이터이면 빈 Form을 만듬
        form_data = JoinForm()

    template = get_template('join_page.html')

    # 처리된 form_data를 넘겨 준다
    context = Context({'join_form' : JoinForm()})
    context.update(csrf(request))

    return HttpResponse(template.render(context))