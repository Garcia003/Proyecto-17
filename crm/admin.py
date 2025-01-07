from django.contrib import admin
from .models import agent, Cases, User

# Register your models here.
admin.site.register(agent)
admin.site.register(Cases)
admin.site.register(User)