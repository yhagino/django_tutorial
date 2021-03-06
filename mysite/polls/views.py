from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)  # shortcuts.render
    # render(第1引数: request オブジェクト 第2引数: テンプレート名 第3引数: （任意）として辞書)


def index_page(request, id):
    return HttpResponse('This is INT urls test. id = ' + str(id))


def index_str(request, id):
    return HttpResponse('This is STR urls test. id = ' + str(id))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)  # try get except 404
    # 第一引数: Djangoモデル、第二引数: 任意の数のキーワード引数
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)