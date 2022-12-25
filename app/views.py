from http.client import HTTPResponse
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . models import *
from .forms import SignUpForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')

def myprogram(request):
    return render(request, 'myprogram.html')
    
def shoppinglist(request):
    return render(request, 'shoppinglist.html')

def recipes(request):
    return render(request, 'recipes.html')

def sports(request):
    return render(request, 'sports.html')

def motivation(request):
    return render(request, 'motivation.html')

def performance(request):
    return render(request, 'performance.html')

def food(request):
    return render(request, 'food.html')

def training(request):
    return render(request, 'training.html')

def cardio(request):
    return render(request, 'cardio.html')

def gym(request):
    return render(request, 'gym-sessions.html')
    
def home_session(request):
    return render(request, 'home-session.html')

def my_measurements_and_my_progress_curve(request):
    return render(request, 'my-measurements-and-my-progress-curve.html')

def recipe_doc(request):
    return render(request, 'recipe-doc.html')
   
def different_exercices_videos(request):
    return render(request, 'different_exercices_videos.html')

def video_sessions_kettlebel(request):
    return render(request, 'video_sessions_kettlebel.html')

def video_sessions_poids_de_corps(request):
    return render(request, 'video-sessions-poids-de-corps.html')

def video_sessions(request):
    return render(request, 'video-sessions.html')

def email_submit(request):
    if request.method=='POST':
        email = request.POST['email']
        return redirect('signup')
    











def signup_user(request):
    if request.method=='POST':
        ins= user_table(request.POST)
        name = request.POST['email']
        print('kkkkkkkk',name)
        password = request.POST['password']

        # Food_Plan_Summary_week_one = request.POST['foodplansummaryweekone']
        # Food_Plan_Summary_week_one_chart = request.POST['foodplansummaryweekonechart']
        # Food_Plan_Summary_week_two = request.POST['foodplansummaryweektwo']
        # Food_Plan_Summary_week_two_chart = request.POST['foodplansummaryweektwochart']
        # Food_Plan_Summary_week_three = request.POST['foodplansummaryweekthree']
        # Food_Plan_Summary_week_three_chart  = request.POST['foodplansummaryweekthreechart']
        # Food_Plan_Summary_week_four = request.POST['foodplansummaryweekfour']
        # Food_Plan_Summary_week_four_chart = request.POST['foodplansummaryweekfourchart']

        # Training_Plan_Summary_week_one = request.POST['trainingplansummaryweekone']
        # Training_Plan_Summary_week_one_chart = request.POST['trainingplansummaryweekonechart']
        # Training_Plan_Summary_week_two = request.POST['trainingplansummaryweektwo']
        # Training_Plan_Summary_week_two_chart = request.POST['trainingplansummaryweektwochart']
        # Training_Plan_Summary_week_three = request.POST['trainingplansummaryweekthree']
        # Training_Plan_Summary_week_three_chart = request.POST['trainingplansummaryweekthreechart']
        # Training_Plan_Summary_week_four = request.POST['trainingplansummaryweekfour']
        # Training_Plan_Summary_week_four_chart = request.POST['trainingplansummaryweekfourchart']

        # Buy_week_one = request.POST['buyweekone']
        # Buy_week_one_chart = request.POST['buyweekonechart']
        # Buy_week_two = request.POST['buyweektwo']
        # Buy_week_two_chart = request.POST['buyweektwochart']
        # Buy_week_three = request.POST['buyweekthree']
        # Buy_week_three_chart = request.POST['buyweekthreechart']
        # Buy_week_four = request.POST['buyweekfour']
        # Buy_week_four_chart = request.POST['buyweekfourchart']

        # Progress_week_one = request.POST['prone']
        # Progress_week_one_chart = request.POST['pronechart']
        # Progress_week_two = request.POST['prtwo']
        # Progress_week_two_chart = request.POST['prtwochart']
        # Progress_week_three = request.POST['prthree']
        # Progress_week_three_chart = request.POST['prthreechart']
        # Progress_week_four = request.POST['prfour']
        # Progress_week_four_chart = request.POST['prfourchart']

        # My_measurements_and_progress = request.POST['exone']
        # The_summary_of_the_progression_curve = request.POST['extwo']
        # Meal_close_to_the_training_summary = request.POST['exthree']
        # Pre_post_recipe_data = request.POST['exfour']
        # In_Case_recipe_data = request.POST['exfive']
        # Meal_away_training_recipe_data = request.POST['exsix']
        # Dessert_recipe_data = request.POST['exseven']

        # ins = user_table(name=name, password=password, Food_Plan_Summary_week_one=Food_Plan_Summary_week_one,
        #                 Food_Plan_Summary_week_one_chart=Food_Plan_Summary_week_one_chart, Food_Plan_Summary_week_two=Food_Plan_Summary_week_two, Food_Plan_Summary_week_two_chart=Food_Plan_Summary_week_two_chart, Food_Plan_Summary_week_three=Food_Plan_Summary_week_three,
        #                 Food_Plan_Summary_week_three_chart=Food_Plan_Summary_week_three_chart, Food_Plan_Summary_week_four=Food_Plan_Summary_week_four, Food_Plan_Summary_week_four_chart=Food_Plan_Summary_week_four_chart, Training_Plan_Summary_week_one=Training_Plan_Summary_week_one,
        #                 Training_Plan_Summary_week_one_chart=Training_Plan_Summary_week_one_chart, Training_Plan_Summary_week_two=Training_Plan_Summary_week_two, Training_Plan_Summary_week_two_chart=Training_Plan_Summary_week_two_chart, Training_Plan_Summary_week_three=Training_Plan_Summary_week_three,
        #                 Training_Plan_Summary_week_three_chart=Training_Plan_Summary_week_three_chart, Training_Plan_Summary_week_four=Training_Plan_Summary_week_four, Training_Plan_Summary_week_four_chart=Training_Plan_Summary_week_four_chart , Buy_week_one=Buy_week_one,
        #                 Buy_week_one_chart=Buy_week_one_chart, Buy_week_two=Buy_week_two, Buy_week_two_chart=Buy_week_two_chart, Buy_week_three=Buy_week_three,
        #                 Buy_week_three_chart=Buy_week_three_chart, Buy_week_four=Buy_week_four, Buy_week_four_chart=Buy_week_four_chart, Progress_week_one=Progress_week_one,
        #                 Progress_week_one_chart=Progress_week_one_chart, Progress_week_two=Progress_week_two, Progress_week_two_chart=Progress_week_two_chart, Progress_week_three=Progress_week_three,
        #                 Progress_week_three_chart=Progress_week_three_chart, Progress_week_four=Progress_week_four, Progress_week_four_chart=Progress_week_four_chart, My_measurements_and_progress=My_measurements_and_progress,
        #                 The_summary_of_the_progression_curve=The_summary_of_the_progression_curve, Meal_close_to_the_training_summary=Meal_close_to_the_training_summary, Pre_post_recipe_data=Pre_post_recipe_data, In_Case_recipe_data=In_Case_recipe_data,
        #                 Meal_away_training_recipe_data=Meal_away_training_recipe_data, Dessert_recipe_data=Dessert_recipe_data)
        ins = user_table(name=name, password=password,)
        ins.save()
        return redirect('/')
    else:
        return render(request, 'signup.html')














    # if request.method=='POST':
    #     fm=SignUpForm(request.POST)
    #     if fm.is_valid():
    #         fm.save()
    #         messages.success(request,'Account has been created successfully.')
    #         return HttpResponseRedirect('/')
    # else:
    #     fm=SignUpForm()
    # return render(request,'signup.html',{'form':fm})


def login_user(request):
    return render(request, 'login.html')
    # if not request.user.is_authenticated:
    #     if request.method=='POST':
    #         fm=AuthenticationForm(request=request,data=request.POST)
    #         if fm.is_valid():
    #             uname=fm.cleaned_data['username']
    #             upass=fm.cleaned_data['password']
    #             user=authenticate(username=uname, password=upass)
    #             if user is not None:
    #                 login(request, user)
    #                 return HttpResponseRedirect('/')                
    #     else:
    #         fm=AuthenticationForm() 
    #     return render(request,'index.html', {'form':fm})
    # else:
    #     messages.success(request,'You are already login')
    #     return HttpResponseRedirect('/') 
        


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


# def signup_usr(request):
#     if request.method=='POST':
#         fm=SignUpForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#             messages.success(request,'Account has been created successfully.')
#             return redirect('login')
#     else:
#         fm=SignUpForm()
#     return render(request,'mobileapplication/signup.html',{'form':fm})