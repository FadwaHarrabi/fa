import streamlit as st
from pymongo import MongoClient
import pandas as pd

st.title('Braincert👋')
st.sidebar.header('Choose a Plan')
plan = st.sidebar.selectbox('LMS plans', ['Course creator plans', 'Enterprise LMS plans'])

# Function to connect to MongoDB Atlas and retrieve data
def get_data_from_mongo(uri, database, collection):
    client = MongoClient(uri)
    db = client[database]
    collection = db[collection]
    data = collection.find()
    return list(data)



# MongoDB connection parameters
MONGO_URI = st.secrets["MONGO_URI"]
DATABASE_NAME = 'braincert_database'
COLLECTION_NAME = 'EntrepriseLmsPlans'

# Fetch data from MongoDB
st.header('Fetching data from MongoDB Atlas...')
data = get_data_from_mongo(MONGO_URI, DATABASE_NAME, COLLECTION_NAME)

if data:
    # Convert the data to a DataFrame
    df = pd.DataFrame(data)
    # Display the DataFrame
    st.write(df)
else:
    st.write('No data found in the collection.')
