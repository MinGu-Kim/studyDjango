from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http.response import HttpResponse
from post_service.models import Post

# Create your views here.
'''
Django 에서 View는‘어떤 데이터를 보여줄 것인가?’에 집중
다시 말해, 데이터들을 모아서 Template 에 보내주고, 그 결과를 사용자에게 보여주는 역할
'''
def post_list(request):
    template = get_template("post_list.html")
    context = Context({'post_list' : Post.objects.all()})

    return HttpResponse(template.render(context))