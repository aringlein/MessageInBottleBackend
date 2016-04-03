from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text


class Message(models.Model):
	text = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	firstSender = models.IntegerField(default=0)
	graphData = models.CharField(max_length=10000, default= 'x' * 10000)
	rejections = models.IntegerField(default=0)
	forwards = models.IntegerField(default=0)

	def __str__(self):
		return self.text

	def id():
		return self.id

class User(models.Model):
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	isActiveTransmitter = models.BooleanField(default = True)
	messages = models.CharField(max_length=1000) #use literal_eval to convert to list
	lastRequest = models.DateTimeField('last request')

	def getLocation(self):
		return self.currentLocation
