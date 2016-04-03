from django.shortcuts import render
from .models import Message
from .models import Question
from django.http import HttpResponse
import json
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import JsonResponse


#def index(request):
#	return HttpResponse("Hello, world. You're at the bottle index.")

def info(request, message_id):
	m = Message.objects.get(id = message_id)
	data = {'text' : str(m), 'id' : str(m.id)}
	json_data = json.dumps(data)
	return HttpResponse((json_data), content_type='application/json')

@csrf_exempt
def update(request):
	if request.method == 'POST':
		val = request.POST.get('id')
		return JsonResponse({"id": val})

@csrf_exempt
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('bottle/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
