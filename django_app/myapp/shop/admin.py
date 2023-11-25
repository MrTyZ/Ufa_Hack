from django.contrib import admin
from .models import *

admin.site.register(Subject)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Question_Type)
admin.site.register(Choice)
