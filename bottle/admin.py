from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Message
from .models import User

admin.site.register(Question)
admin.site.register(Message)
admin.site.register(User)
