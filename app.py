from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\Maitrik\Desktop\\Solution-I\\Project\\final_model.pkl','rb'))

#model = pickle.load(open("C:\\Users\\Raj\\Downloads\\sample\\project\\flight_Model.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':

        dep_date=request.form['Dept_hour']
        journey_date=int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").day)
        journey_month=int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").month)

        Dep_hour=int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").hour)
        Dep_minute=int(pd.to_datetime(dep_date,format="%Y-%m-%dT%H:%M").minute)

        date_arr=request.form['arr_hour']
        arr_hour=int(pd.to_datetime(date_arr,format="%Y-%m-%dT%H:%M").hour)
        arr_minute=int(pd.to_datetime(date_arr,format="%Y-%m-%dT%H:%M").minute)

        duration_hour=abs(arr_hour-Dep_hour)
        duration_minute=abs(arr_minute-Dep_minute)

        Total_stops=int(request.form['Stops'])
        

        Airline=request.form['Airline']
        if(Airline=='Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='IndiGo'):
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='Air_India'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 1
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='Multiple_carriers'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='SpiceJet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='Vistara'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0          
        elif(Airline=='GoAir'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='Multiple_carriers_Premium_economy'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0  
        elif(Airline=='Jet_Airways_Business'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0 
        elif(Airline=='Vistara_Premium_economys'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0 
        elif(Airline=='Trujet'):
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1
        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        Source=request.form['Source'] 
        if (Source=='Kolkata'):
            S_Kolkata=1
            S_Delhi=0
            S_Chennai=0
            S_Mumbai=0
        elif (Source=='Delhi'):
            S_Kolkata=0
            S_Delhi=1
            S_Chennai=0
            S_Mumbai=0
        elif (Source=='Chennai'):
            S_Kolkata=0
            S_Delhi=0
            S_Chennai=1
            S_Mumbai=0
        elif (Source=='Mumbai'):
            S_Kolkata=0
            S_Delhi=0
            S_Chennai=0
            S_Mumbai=1 
        else:
            S_Kolkata=0
            S_Delhi=0
            S_Chennai=0
            S_Mumbai=0
        Destination=request.form['Destination']

        if (Destination=='Cochin'):
            d_Coachin=1
            d_Delhi=0
            d_Hyderabad=0
            d_Kolkata=0
            d_NewDelhi=0
        elif (Destination=='Delhi'):
            d_Coachin=0
            d_Delhi=1
            d_Hyderabad=0
            d_Kolkata=0
            d_NewDelhi=0
        elif (Destination=='Hyderabad'):
            d_Coachin=0
            d_Delhi=0
            d_Hyderabad=1
            d_Kolkata=0
            d_NewDelhi=0 
        elif (Destination=='Kolkata'):
            d_Coachin=0
            d_Delhi=0
            d_Hyderabad=0
            d_Kolkata=1
            d_NewDelhi=0 
        elif (Destination=='NewDelhi'):
            d_Coachin=0
            d_Delhi=0
            d_Hyderabad=0
            d_Kolkata=0
            d_NewDelhi=1 
        else:
            d_Coachin=0
            d_Delhi=0
            d_Hyderabad=0
            d_Kolkata=0
            d_NewDelhi=0

        prediction=model.predict([[journey_date,journey_month,Dep_hour,Dep_minute,arr_hour,arr_minute,duration_hour,duration_minute,Total_stops,Jet_Airways,IndiGo,Air_India,Multiple_carriers,SpiceJet,Vistara,GoAir,Multiple_carriers_Premium_economy,Jet_Airways_Business,Vistara_Premium_economy,Trujet,d_Coachin,d_Delhi,d_Hyderabad,d_Kolkata,d_NewDelhi,S_Kolkata,S_Delhi,S_Chennai,S_Mumbai
        ]]) 
        output=round(prediction[0],2)
        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)         
























