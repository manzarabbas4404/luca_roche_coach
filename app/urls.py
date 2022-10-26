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
    path('my-measurements-and-my-progress-curve/',views.my_measurements_and_my_progress_curve, name='my_measurements_and_my_progress_curve'),
    path('recipe_doc/',views.recipe_doc, name='recipe_doc'),
    path('video-sessions-poids-de-corps/',views.video_sessions_poids_de_corps, name='video-sessions-poids-de-corps'),
    path('video-sessions-kettlebel/',views.video_sessions_kettlebel, name='video-sessions-kettlebel'),
    path('different-exercices-videos/',views.different_exercices_videos, name='different-exercices-videos'),
    path('video-sessions/',views.video_sessions, name='video-sessions'),
    path('email_submit/',views.email_submit, name='email_submit'),

    
    

    path('signup',views.signup_user, name='signup'),
    path('login',views.login_user, name='login'),
    path('logout',views.log_out, name='logout'),


    
    
    
    
   
] 