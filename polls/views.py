from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('EVCARD！')


def detail(request, question_id):
	return HttpResponse("你正在浏览问题： %s." % question_id)


def results(request, question_id):
	response = "你正在浏览问题 %s 的结果"
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("你正在为问题 %s 投票" % question_id)