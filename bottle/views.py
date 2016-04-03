from django.shortcuts import render
from .models import Message, User 
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

		userId = request.POST.get('user')
		lat = request.POST.get('latitude')
		lon = request.POST.get('longitude')
		updates = json.loads(request.POST.get('updates'))

		user = User.objects.get(id=userId)
		print(user.latitude)
		user.latitude = lat
		user.longitude = lon
		user.save()
		#print(User.objects.get(id=userId).currentLocation[0])

		for update in updates:
			print(update)
		return JsonResponse({"id": userId, "lat": lat, "lon":lon})

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
