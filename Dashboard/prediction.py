import pickle
from pandas import DataFrame,get_dummies

model = pickle.load(open("E:\\8 Purwadhika Data Analysis\\Final Project\\finalized_model.sav",'rb'))
real_columns = pickle.load(open("E:\\8 Purwadhika Data Analysis\\Final Project\\real_colomn.sav",'rb'))
one_hot_columns = pickle.load(open("E:\\8 Purwadhika Data Analysis\\Final Project\\x_dummies_columns.sav",'rb'))

def prediction(data):
    df= DataFrame(data,index=[0])
    df= get_dummies(df)
    df = df.reindex(columns=one_hot_columns,fill_value=0)
    hasil = model.predict(df)
    return round(hasil[0])
