from django.contrib import admin
from .models import userproflile,Shift,Event


# Register your models here.
admin.site.register(userproflile)
admin.site.register(Shift)
admin.site.register(Event)