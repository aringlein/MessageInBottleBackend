from django.shortcuts import render
from .models import Message, User, Question
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.http import JsonResponse
from django.utils import timezone
import ast


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

		##assume update format is [{"id": id, "val": 0}, ...
		messageList = []

		user = User.objects.get(id=userId)
		#print(user.latitude)
		user.latitude = lat
		user.longitude = lon

		#add all messages which have been updated
		for mes in Message.objects():
			if mes.lastUpdate < user.lastRequest:
				messageList.append(mes.id)

		#add messages which should be passed by people who are local
		for other in User.objects():
			if ((user.latitude - other.latitude) ** 2 + (user.longitude - other.longitude) ** 2) ** .5 < .05:
				#close enough
				mOther = ast.literal_eval(other.messages)
				mUser = ast.literal_eval(user.messages)

				for item in mOther:
					if mUser.contains(item) == False and messageList.contains(item) == False:
						messageList.append(item)
						g = GraphItem(lat1 = other.latitude, lat2=user.latitude, lon1 = other.longitude, lon2= user.longitude, message_id = item)
						g.save()

						#update the last updated time of the message
						m = Message.objects.get(id=item)
						m.lastUpdate = timezone.now()
						m.save()

						#TODO: change byte array

		#add graph items to a list to send to a dict

		user.lastRequest = timezone.now()
		user.save()
		#print(User.objects.get(id=userId).currentLocation[0])

		for update in updates:
			print(update)
			#update rejections/forwards
			m_id = update.id
			val = update.val
			mes = Message.objects.get(id=m_id)
			mes.lastUpdate = timezone.now()
			if val == 0:
				mes.rejections += 1
			else:
				mes.forwards += 1
				#Set this user to actively forward TODO
			mes.save()

		return JsonResponse({"id": userId, "lat": lat, "lon":lon})

@csrf_exempt
def new(request):
	if request.method == 'POST':

		txt = request.POST.get('message')
		userId = request.POST.get('id')
		lat = request.POST.get('latitude')
		lon = request.POST.get('longitude')

		m = Message(text = txt, firstSender = userId, pub_date = timezone.now(), rejections = 0, forwards = 1, graphData = null)
		m.save()

		return HttpResponse('OK')



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
