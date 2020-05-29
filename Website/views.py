from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from a1_cricket.predictions.pred import *


from .forms import *
from .models import *


# Create your views here.
def main(request):
    return render(request, 'a1temp/main.html', {})





def about(request):
        return render(request, 'a1temp/about.html', {})








def first_inn(request):
    TW=""
    t=""
    nu=""
    te1=""
    te2=""
    if request.method == 'POST':
        title_form = InningsFirst(request.POST)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            team2 = title_form.cleaned_data['team2']
            
            
            neutralvenue = title_form.cleaned_data['neutralvenue']
            if neutralvenue == "1":
                nu="TRUE"
            else:
            
                nu="FALSE"
                
            tosswinner = title_form.cleaned_data['tosswinner']
            tossdecision = title_form.cleaned_data['tossdecision']
            if tossdecision == "1":
                t="bat"
            else:
            
                t="field"
            print(neutralvenue)
            print( str(tosswinner)+ "oiouoiuiou")
            print(tossdecision)
            
            if team1=="1":
                if tosswinner == "1":
                    TW="Australia"
                
                
                te1="Australia"
                print(te1)
            
            
            if team1=="2":
                if tosswinner == "2":
                    TW="England"
                te1="England"
                print(te1)
            if team1=="3":
                if tosswinner == "3":
                    TW="India"
                
                te1="India"
                print(te1)
            if team1=="4":
                if tosswinner == "4":
                    TW="New Zealand"
                te1="New Zealand"
                print(te1)
            if team1=="5":
                if tosswinner == "5":
                    TW="Pakistan"
                
                te1="Pakistan"
                print(te1)
            if team1=="6":
                if tosswinner == "6":
                    TW="South Africa"
                te1="South Africa"
                print("South Africa")
            if team1=="7":
                if tosswinner == "7":
                    TW="Sri Lanka"
                te1="Sri Lanka"
                print(te1)
            if team1=="8":
                if tosswinner == "8":
                    TW="West Indies"
                te1="West Indies"
                print(te1)
            if team1=="9":
                if tosswinner == "9":
                    TW="Zimbabwe"
                te1="Zimbabwe"
                print(te1)
                
            
           
            
            
            
            
            
            
            
            
            
            
            
            
            if team2=="1":
                
                if tosswinner == "1":
                    TW="Australia"
                te2="Australia"
                print(te2)
            if team2=="2":
                if tosswinner == "2":
                    TW="England"
                te2="England"
                print(te2)
            if team2=="3":
                if tosswinner == "3":
                    TW="India"
                te2="India"
                print(te2)
            if team2=="4":
                if tosswinner == "4":
                    TW="New Zealand"
                te2="New Zealand"
                print(te2)
            if team2=="5":
                if tosswinner == "5":
                    TW="Pakistan"
                te2="Pakistan"
                print(te2)
            if team2=="6":
                if tosswinner == "6":
                    TW="South Africa"
                te2="South Africa"
                print(te2)
            if team2=="7":
                if tosswinner == "7":
                    TW="Sri Lanka"
                te2="Sri Lanka"
                print(te2)
            if team2=="8":
                if tosswinner == "8":
                    TW="West Indies"
                te2="West Indies"
                print(te2)
            if team2=="9":
                if tosswinner == "9":
                    TW="Zimbabwe"
                te2="Zimbabwe"
                print(te2)
            
            
            winner = Get_Cities_Names(te1,te2)
            print(winner)
            
            if (prin(3))== 1:
                
                answer = request.POST.get('color')
                print(answer)
                print(TW)
                print(te1)
                print(te2)
                if (TW !=te1) and (TW !=te2):
                    message="Please choose correct input for  Toss winner"
                    return render(request, 'a1temp/firstinn.html', context={'form1': title_form,"messag":message,"city":winner,"cityt":1})
                    
    
                team_predicted = predintion_win(team_=te1,team1_=te2,city_=answer,neutralvenue_=nu,toss_winner_=TW,toss_decision_=t,winner_=te1)
                prin(0)
                print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaagggggggggggggg")
                return render(request, 'a1temp/firstinn.html', context={'form1': title_form,"runs":team_predicted,"city":winner,"cityt":0})
            else:
                
                prin(1)
               
                return render(request, 'a1temp/firstinn.html', context={'form1': title_form,"city":winner,"cityt":1})
                
            
            

            


    else:
        title_form = InningsFirst()
      

    return render(request, 'a1temp/firstinn.html', context={'form1': title_form})



def second_inn(request):
    if request.method == 'POST':
        
        
        title_form = InningsSecond(request.POST)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            team2 = title_form.cleaned_data['team2']
            venue = title_form.cleaned_data['venue']
            runs = title_form.cleaned_data['runs']
            overs_played = title_form.cleaned_data['overs_played']
            target_chasing = title_form.cleaned_data['target_set']
            wickets = title_form.cleaned_data['wickets_fallen']

            result = predict_2nd_inn(team1,team2,runs,6*overs_played,wickets,target_chasing,venue)
            by_run = 0
            by_wicket = 0
            if result[0]>0.5:
                winner = get_team(team1)
                probab = result[0] * 100
                by_wicket = int(result[1])
            elif result[0]<0.5:
                winner = get_team(team2)
                probab = (1-result[0])*100
                by_run = int(result[1])
            else:
                winner = "Can be any one"
                probab = 50

            if(result[2]>=120):
                result[2]=119
            end = str(int(result[2]/6)+1)

            return render(request, 'a1temp/secondinn.html', context={'form2': title_form,
                            "winner":winner,"probab":probab,"by_run":by_run,"by_wicket":by_wicket,"end":end})

    else:
        title_form = InningsSecond()

    return render(request, 'a1temp/secondinn.html', context={'form2': title_form})



def prematch(request):
    if request.method == 'POST':
        title_form = PreMatch(request.POST)
        if title_form.is_valid():
            team1 = title_form.cleaned_data['team1']
            print(team1)
            print(team1)
            print(team1)
            print(team1)
            print(team1)
            print(team1)
            team2 = title_form.cleaned_data['team2']
            venue = title_form.cleaned_data['venue']
            probab = pre_match_predict("2016",team1,team2,venue)
            if probab > 0.5 :
                winner = get_team(team1)
                probab = probab * 100
            else:
                winner =  get_team(team2)
                probab = (1- probab) * 100

            return render(request, 'a1temp/pre_pred.html', context={'form3': title_form,"winner":winner,"probab":probab})

    else:
        title_form = PreMatch()

    return render(request, 'a1temp/pre_pred.html', context={'form3': title_form})
