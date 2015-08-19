from django.shortcuts import render
from django.http import HttpResponse, Http404
'''from django.template import RequestContext, loader'''
''' mandando a llamar a las vistas: HttpResponse, RequestContext y loader o podemos cargar solo a shortcuts render '''

from .models import Question

# Create your views here.


def index(request):
    '''return HttpResponse("Hello, world. You're at the polls index.")'''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    sezzhRights = 'This is a webpage made by sezzh'
    context = {
        'latest_question_list': latest_question_list,
        'sezzhRights': sezzhRights
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('question no existe...')
    context = {
            'question': question,
        }
    return render(request, 'polls/detail.html', context )


def results(request, question_id):
    response = "You're looking at the results of question %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def sezzh(request):
    ''' This is a example view function to see how it is works '''
    print request
    return HttpResponse('entraste a sezzh')
