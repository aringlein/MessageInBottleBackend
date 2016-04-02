from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
import json

def index(request):
	return HttpResponse("Hello, world. You're at the bottle index.")

def info(request, message_id):
	m = Message.objects.get(id = message_id)
	data = {'text' : str(m), 'id' : str(m.id)}
	json_data = json.dumps(data)
	return HttpResponse((json_data), content_type='application/json')