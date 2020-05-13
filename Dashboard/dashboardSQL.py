import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:citratm08@localhost/airbnbsing1?host=localhost?port=3306")
conn = engine.connect()
result = conn.execute('SELECT * from airbnbsing1.airbnb_sample;').fetchall()

df_sample = pd.DataFrame(pd.DataFrame(result,columns=result[0].keys()))

