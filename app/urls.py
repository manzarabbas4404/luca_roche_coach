from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('profile/',views.profile, name='profile'),
    path('myprogram/',views.myprogram, name='myprogram'),
    path('shoppinglist/',views.shoppinglist, name='shoppinglist'),
    path('recipes/',views.recipes, name='recipes'),
    path('sports-sessions/',views.sports, name='sports'),
    path('motivation-lifestyle/',views.motivation, name='motivation'),
    path('performance-calculator/',views.performance, name='performance'),
    path('food-plans/',views.food, name='food'),
    path('training-plans/',views.training, name='training'),
    path('cardio-hitt-session/',views.cardio, name='cardio'),
    path('gym-session/',views.gym, name='gym'),
    path('home-sessions/',views.home_session, name='home_session'),
    
    path('signup',views.signup_user, name='signup'),
    path('login',views.login_user, name='login'),
    path('logout',views.log_out, name='logout'),

    
    
    
    
   
] 