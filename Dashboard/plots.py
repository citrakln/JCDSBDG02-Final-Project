import plotly
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json
from data import data_clean


def neighbourhood_plots():
    df = data_clean()
    df_group = df['neighbourhood_cleansed'].value_counts()
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def room_type_plots():
    df = data_clean()
    df_group = df['room_type'].value_counts()
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def property_plots():
    df = data_clean()
    df_group = df['property_type'].value_counts()
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Weekend_plots():
    df = data_clean()
    df_group = df['Weekend'].value_counts()
    fig = go.Figure([go.Bar(x=df_group.index, y = df_group.values)])
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def neighbourhood_price():
    df = data_clean()
    fig = px.box(df, x="neighbourhood_cleansed", y="price")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json


def room_type_price():
    df = data_clean()
    fig = px.box(df, x="room_type", y="price")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def Weekend_price():
    df = data_clean()
    fig = px.box(df, x="Weekend", y="price")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def property_type_price():
    df = data_clean()
    fig = px.box(df, x="property_type", y="price")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json