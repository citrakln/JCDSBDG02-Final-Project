import pandas as pd
def data_clean():
    df = pd.read_csv("E:\\8 Purwadhika Data Analysis\\Final Project\\Airbnb_clean_for_plotting.csv")
    return df

neighbourhood_cleansed = ['Geylang', 'Kallang', 'Rochor', 'Outram', 'Novena', 'Bukit Merah',
       'Downtown Core', 'River Valley', 'Bedok', 'Tanglin', 'Queenstown',
       'Marine Parade', 'Singapore River', 'Bukit Timah', 'Jurong West',
       'Newton', 'Orchard', 'Toa Payoh', 'Hougang', 'Jurong East', 'Clementi',
       'Serangoon', 'Tampines', 'Museum', 'Woodlands', 'Choa Chu Kang',
       'Pasir Ris', 'Bishan', 'Punggol', 'Sengkang', 'Bukit Batok',
       'Bukit Panjang', 'Ang Mo Kio', 'Yishun', 'Sembawang',
       'Central Water Catchment', 'Mandai', 'Sungei Kadut',
       'Western Water Catchment', 'Southern Islands']

Weekend=['Weekdays', 'Weekend']

property_type= ['Apartment', 'Condominium', 'Serviced apartment', 'House', 'Hostel',
       'Townhouse', 'Loft', 'Hotel', 'Bed and breakfast', 'Bungalow', 'Other',
       'Boutique hotel', 'Guest suite', 'Guesthouse', 'Tent', 'Villa', 'Boat',
       'Aparthotel', 'Campsite', 'Cottage', 'Cabin']

room_type = ['Entire home/apt', 'Private room', 'Shared room']

pool = [1,0]
gym = [1,0]
elevator = [1,0]
kitchen = [1,0]
hairdryer = [1,0]
highchair = [1,0]
smokingallowed = [1,0]
essentials = [1,0]
family = [1,0]
freeparkingonpremises = [1,0]


