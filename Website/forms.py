from django import forms



team_choice = (
        (1,	'Australia'),
        (2,	'England'),
        (3,	'India'),
        (4,	'New Zealand'),
        (5,	'Pakistan'),
        (6,	'South Africa'),
        (7,	'Sri Lanka'),
        (8,	'West Indies'),
        (9,	'Zimbabwe'),
)

city_choice = (
    (1	, 'australia'),
    (2	, 'england'),
    (3	, 'india'),
    (4	, 'lords'),
    (5	, 'pakistan'),
    
)
neutral_choice = (
    (1	, 'True'),
    (2	, 'False'),
   
    
)
bat_choice = (
    (1	, 'Bat'),
    (2	, 'field'),
   
    
)


class PreMatch(forms.Form):
    team1 = forms.ChoiceField(choices=team_choice, widget=forms.Select())
    team2 = forms.ChoiceField(choices=team_choice, widget=forms.Select())
    venue = forms.ChoiceField(choices=city_choice, widget=forms.Select())


class InningsFirst(forms.Form):
    team1 = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Team 1")
    team2 = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Team 2")
    neutralvenue = forms.ChoiceField(choices=neutral_choice, widget=forms.Select(),label="Neutral Choice")
    tosswinner = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Toss Winner")
    tossdecision = forms.ChoiceField(choices=bat_choice, widget=forms.Select(),label="Toss Decision")
   
    
class cityy(forms.Form):
   
    venue = forms.ChoiceField(choices=city_choice, widget=forms.Select())
    runs = forms.IntegerField()
    overs_played = forms.IntegerField()
    wickets_fallen = forms.IntegerField()
    


class InningsSecond(forms.Form):
    team1 = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Current Batting Team")
    team2 = forms.ChoiceField(choices=team_choice, widget=forms.Select(),label="Current Bowling Team")
    venue = forms.ChoiceField(choices=city_choice, widget=forms.Select())
    runs = forms.IntegerField()
    wickets_fallen = forms.IntegerField()
    overs_played = forms.IntegerField()
    target_set = forms.IntegerField()
