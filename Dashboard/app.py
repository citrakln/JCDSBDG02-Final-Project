from dash import Dash
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from flask import Flask,render_template,request, redirect,url_for
from dashboardSQL import df_sample
from data import neighbourhood_cleansed,Weekend,property_type,room_type,pool,gym, elevator, kitchen, hairdryer, highchair, smokingallowed, essentials,family,freeparkingonpremises
from prediction import prediction
from plots import neighbourhood_plots,Weekend_plots,room_type_plots,neighbourhood_price,Weekend_price,room_type_price


## translatr flask to python object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/table')
def table_data():
    data = df_sample
    return render_template('table_data.html', data = data,title='Data Sample')

@app.route('/prediction',methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        data = request.form
        data = data.to_dict()
        df = pd.DataFrame(data,index=['Your Input']).transpose()
        data['month'] = int(data['month'])
        data['guests_included'] = int(data['guests_included'])
        data['number_of_reviews_ltm'] = int(data['number_of_reviews_ltm'])
        data['security_deposit'] = int(data['security_deposit'])
        data['extra_people'] = int(data['extra_people'])
        data['cleaning_fee'] = int(data['cleaning_fee'])
        data['minimum_nights'] = int(data['minimum_nights'])
        data['host_listings_count'] = int(data['host_listings_count'])
        hasil = prediction(data)
        return render_template('result.html',hasil_pred=hasil,data=df)
        # return render_template('result.html',hasil_pred=hasil)
        # kita jalanin function predict
        # Render result.html
    return render_template('prediction.html',data_neighbourhood_cleansed = sorted(neighbourhood_cleansed), 
    data_property_type = sorted(property_type), data_room_type = sorted(room_type),data_pool=sorted(pool),
    data_gym=sorted(gym),data_elevator=sorted(elevator),data_kitchen=sorted(kitchen),data_hairdryer=sorted(hairdryer),
    data_highchair=highchair,data_smokingallowed=smokingallowed,data_essentials=essentials,data_Weekend=Weekend,data_family=family,
    data_freeparkingonpremises=freeparkingonpremises)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/helps')
def help():
    return render_template('help.html')

@app.route('/plots')
def plot():
    data1 = neighbourhood_plots()
    data2 = room_type_plots()
    data3 = Weekend_plots()
    data4 = neighbourhood_price()
    data5 = room_type_price()
    data6 = Weekend_price()
    return render_template('plots.html',data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6)


if __name__ == '__main__':
    app.run(debug=True,port=1305)

