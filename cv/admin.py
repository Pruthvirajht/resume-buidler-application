from django.contrib import admin

from .models import Profile,Education,Experience,Skill

# Register your models here.
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Experience)
