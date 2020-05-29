

import numpy as np
import pandas as pd


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split




import pickle
import os
script_dir = os.path.dirname(__file__)









temp=[0]

def checktemp(b):
    
    if b==0:
        temp[0]=0
        
    if b==1:
        temp[0]=1;
        
        
    if b==3:
        
        return temp[0]
    
    return temp[0]


    
    



def prin(a):
    t=checktemp(a)
    return t
    
    












def pre_match_predict(season,team1,team2,city):
    """
    rel_path = "pre_pred/pre_pred.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "pre_pred/pre_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[season,team1,team2,city]]
    X_test = enc.transform(X_test).toarray()
    print(len(X_test[0]))
    y_pred = regressor.predict(X_test)
    print("our_prediction:",y_pred)
    """
    return 7






def predict_1st_inn():
    
    
    path = r'D:\FYP\python\Python code\ODITEST1.csv'
    df = pd.read_csv(path)
    print(df)
    """
    abc=df['team'].unique()
    abc1=df['toss_decision'].unique()
    df['team']=df.apply(text_to_number,axis=1)
    df['team.1']=df.apply(text_to_number1,axis=1)
    df['toss_winner']=df.apply(text_to_number2,axis=1)
    df['winner']=df.apply(text_to_number3,axis=1)
    df['toss_decision']=df.apply(text_to_number4,axis=1)
    df['method']=df.apply(text_to_number5,axis=1)

    # why you have deleted these attributes...?

    df=df.drop(['gender','season','date','series','venue','match_number','method','city','neutralvenue','player_of_match','umpire','umpire.1','tv_umpire','reserve_umpire','match_referee','competition','Total_Run_FirstInning','Total_Run_SecondInning','Overs_FirstInning','Overs_SecondInning','Wickets_loss_FirstInning','Wickets_loss_SecondInning'], axis = 1)

    df=df.fillna(0)  # will this improve the result

    y = df.winner.values
    x_data = df.drop(['winner'], axis = 1)
    x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values

    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2,random_state=2)




    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors = 2)  # n_neighbors means k
    knn.fit(x_train, y_train)
    prediction = knn.predict(x_test)
    print("{} NN Score: {:.2f}%".format(2, knn.score(x_test, y_test)*100))
    """
    
    
    
    
    print("our_prediction:")
    return 5


















def predict_if_bat_win(team_batting,team_bowling,run,ball,wicket,target,city):
    """
    rel_path = "2nd_inn/bat_win/2nd_inn_bat_win_wicket.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/bat_win/2nd_inn_bat_win_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    X_test = enc.transform(X_test).toarray()
    y_pred = regressor.predict(X_test)
    print("our_prediction:bat_win:wicket",y_pred)
    """
    return 8

def predict_if_bowl_win(team_batting,team_bowling,run,ball,wicket,target,city):
    """
    rel_path = "2nd_inn/bowl_win/2nd_inn_bowl_win_run.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/bowl_win/2nd_inn_bowl_win_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    X_test = enc.transform(X_test).toarray()
    y_pred = regressor.predict(X_test)
    print("our_prediction:bowl_win:wicket",y_pred)
    """
    return 9


def predict_2nd_end_ball(team_batting,team_bowling,run,ball,wicket,target,city):
    """
    rel_path = "2nd_inn/end/2nd_inn_end.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/end/2nd_inn_end_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    X_test = enc.transform(X_test).toarray()
    y_pred = regressor.predict(X_test)
    print("our_prediction:2nd_inn_end",y_pred)
    """
    return 10



def predict_2nd_inn(team_batting,team_bowling,run,ball,wicket,target,city):
    """
    rel_path = "2nd_inn/who_win/2nd_inn_win_pred.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    regressor = joblib.load(abs_file_path)

    rel_path = "2nd_inn/who_win/2nd_inn_win_hot.pkl"
    abs_file_path = os.path.join(script_dir, rel_path)
    enc = pickle.load( open( abs_file_path, "rb" ))

    X_test = [[team_batting,team_bowling,run,ball,wicket,target,city]]
    X_test = enc.transform(X_test).toarray()
    y_pred = regressor.predict(X_test)
    end_ball = predict_2nd_end_ball(team_batting,team_bowling,run,ball,wicket,target,city)
    if y_pred[0]>=0.5:
	       info = predict_if_bat_win(team_batting,team_bowling,run,ball,wicket,target,city)
    else:
	       info = predict_if_bowl_win(team_batting,team_bowling,run,ball,wicket,target,city)

    """
    return 2



def predintion_win(team_,team1_,city_,neutralvenue_,toss_winner_,toss_decision_,winner_):

   
    import pandas as pd
    rel_path = "selected_team_ODI.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    abs_file_path
    
    Favour_team=team_
    Against_Team=team1_
    
    
    F_A_Teams=[Favour_team,Against_Team]
    
    df = pd.read_csv(abs_file_path)
    print(df)
    df=df[df.team1.isin(F_A_Teams) & df.team.isin(F_A_Teams)]
    df=df.drop(['gender','season','date','winner_runs','winner_wickets','venue','series','match_number','method','player_of_match','umpire','umpire.1','tv_umpire','reserve_umpire','match_referee','competition','Total_Run_FirstInning','Total_Run_SecondInning','Overs_FirstInning','Overs_SecondInning','Wickets_loss_FirstInning','Wickets_loss_SecondInning'], axis = 1)
    
    df = df.append({'team' : Favour_team , 'team1' : Against_Team , 'city' : 'Leeds' , 'neutralvenue':'True','toss_winner':'pakistan','toss_decision':'bat','winner':'------'} , ignore_index=True)
    
    team1=df['team1'].unique()
    team2=df['team'].unique()
    c = np.hstack([team1,team2])
    BothTeams=np.unique(c)
    
    TossDeci=df['toss_decision'].unique()
    
    city= df['city'].unique()
    
    
    def text_to_number(df):
        for x in range(0,len(BothTeams)):
            if df['team'] == BothTeams[x]:
                return x
    
    def text_to_number1(df):
        for x in range(0,len(BothTeams)):
            if df['team1'] == BothTeams[x]:
                return x
            
    def text_to_number2(df):
        for x in range(0,len(BothTeams)):
            if df['toss_winner'] == BothTeams[x]:
                return x 
    
    def text_to_number3(df):
        for x in range(0,len(BothTeams)):
            if df['winner'] == BothTeams[x]:
                return x 
    
    def text_to_number4(df):
        for x in range(0,len(TossDeci)):
            if df['toss_decision'] == TossDeci[x]:
                return x 
    
    def text_to_number6(df):
        for x in range(0,len(city)):
            if df['city'] == city[x]:
                return x 
    
    def text_to_number7(df):
        if df['neutralvenue'] == True:
                return 1 
        
        
    df['team']=df.apply(text_to_number,axis=1)
    df['team1']=df.apply(text_to_number1,axis=1)
    df['toss_winner']=df.apply(text_to_number2,axis=1)
    df['winner']=df.apply(text_to_number3,axis=1)
    df['toss_decision']=df.apply(text_to_number4,axis=1)
    df['city']=df.apply(text_to_number6,axis=1)
    df['neutralvenue']=df.apply(text_to_number7,axis=1)
    
    
    
    df=df.fillna(0)  
    
    df["city"] = df["city"] / df["city"].max()
    
    Input_data=df.loc[len(df)-1]
    Input_data = pd.DataFrame(Input_data).transpose()
    Input_data = Input_data.drop(['winner'], axis = 1)
    
    
    df=df.drop(df.index[len(df)-1])
    
    
    
    y = df.winner.values
    x_data = df.drop(['winner'], axis = 1)
    
    
    x=x_data
    
    
    Zero_flag = np.all(y==0)
    One_flag = np.all(y==1)
    
    if Zero_flag:
        y[len(y)-1]=1
    
    if One_flag:
        y[len(y)-1]=0
    
    from sklearn.ensemble import GradientBoostingClassifier
    model = GradientBoostingClassifier(n_estimators=100,max_depth=6,learning_rate=0.1,random_state=0)
    model.fit(x, y)
    xyz = model.predict(Input_data)
    return F_A_Teams[int(xyz[0])]







def Get_Cities_Names(Favour_team_,Against_Team_):
    
    import pandas as pd
    rel_path = "selected_team_ODI.csv"
    abs_file_path = os.path.join(script_dir, rel_path)
    abs_file_path
    df = pd.read_csv(abs_file_path)
    
    Favour_team=Favour_team_
    Against_Team=Against_Team_
        
    F_A_Teams=[Favour_team,Against_Team]
    
    df=df[df.team1.isin(F_A_Teams) & df.team.isin(F_A_Teams)]
    
    city= df['city'].unique()
    city = city[~pd.isnull(city)]
    return city
    






def get_team(id):
    teams = {
            "1":'pakistan',
            "2":'india',
            "3":'england',
            "4":'westindies',
            "5":'srilanka',
            "6":'bangladesh',
            "7":'south africa',
            "8":'australia'
    }
    return teams[id]




#pred = predict_1st_inn(2,5,12,15,2,4)
#print("---------first-----------",pred)
#pred = predict_2nd_inn(1,6,12,15,2,174,11)
#print("-----------2nd---------------",pred)
