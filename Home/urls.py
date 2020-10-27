from django.urls import path,include
from . import views

urlpatterns = [
    path('',include('django.contrib.auth.urls'),name = 'login'),
    path('signup', views.signup,name='signup'),
    path('home',views.Home,name='home'),
    path('Create_Portfolio/<int:user_id>',views.mypage, name='mypage'),
    path('update',views.update,name = 'update_profile_image'),
    path('add_diet',views.Add_Diet,name = 'Add_Diet'),
    path('add_exercise',views.Add_Exercise,name = 'Add_Exercise'),
    path('add_event',views.Add_Event,name= 'Add_Event'),
    path('add_photo',views.Add_Photo,name = 'Add_Photo'),
    path('<int:pk>/update',views.Profile_Update.as_view(template_name = 'update.html')),
    path('<int:pk>/delete_ev',views.Delete_Event.as_view(template_name = 'delete.html')),
    path('<int:pk>/delete_ex',views.Delete_Exercise.as_view(template_name = 'delete.html')),
    path('<int:pk>/delete_bf',views.Delete_Breakfast.as_view(template_name = 'delete.html')),
    path('<int:pk>/delete_lh',views.Delete_Lunch.as_view(template_name = 'delete.html')),
    path('<int:pk>/delete_dn',views.Delete_Dinner.as_view(template_name = 'delete.html')),
    path('<int:pk>/delete_ph',views.Delete_Photo.as_view(template_name = 'delete.html')),
    path('Digital_Portfolio',views.Digital_Portfolio,name = "Digital_Portfolio"),

    
]

