from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse

'''from django.template import RequestContext, loader'''
''' mandando a llamar a las vistas: HttpResponse, RequestContext y loader o
podemos cargar solo a shortcuts render '''

from .models import Question, Choice

# Create your views here.


def index(request):
    '''return HttpResponse("Hello, world. You're at the polls index.")'''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print latest_question_list
    print type(latest_question_list)
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
    question = get_object_or_404(Question, pk = question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)

def vote(request, question_id):
    p = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = p.choice_set.get(pk = request.POST['choice'])
        print "esto es selected_choice: " + str(selected_choice)
        print p
    except (KeyError, Choice.DoesNotExist):
        #redisplay the question voting form
        context = {
            'question': p,
            'error_message': "You didn't select a choice...",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        #with POST data. This prevents data from being posted twice if a user
        #hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


################################################################################


def sezzh(request, name = 'bebi', working = 'default'):
    ''' This is a example view function to see how it is works '''
    context = {
        'title': 'Esto es una prueba de contextos',
        'name': name,
        'working': working,
    }
    return render(request, 'polls/sezzh.html', context)

def sezzh_form_send(request):
    name = request.POST['name']
    working = 'funciono'
    return HttpResponseRedirect(reverse('polls:sezzh', args = (name, working,)))
