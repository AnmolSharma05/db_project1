
from django.contrib import admin
from Home.models import About_User,Breakfast,Lunch,Dinner,DIET_PLAN,Exercises,Event,User_Image
# Register your models here.

admin.site.register(About_User)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)
admin.site.register(DIET_PLAN)
admin.site.register(Exercises)
admin.site.register(Event)
admin.site.register(User_Image)

