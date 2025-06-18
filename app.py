import streamlit as st
import  numpy  as  np 
import joblib 
from sklearn.preprocessing import StandardScaler


Scaler = StandardScaler()

# Load Saved Model 
model = joblib.load('House_Price_Model.pk1')

st.title('🏠 House Price Predictor')

# Get the user input for the house price prediction 
def get_user_input():
    longitude = st.number_input("longitude", value=34.0)
    latitude = st.number_input('latitude', value=-118.0)
    housing_median_age = st.number_input('House median age', value= 20)
    total_rooms = st.number_input('Total Rooms',  value=15)
    total_bedrooms = st.number_input('Total Bedrooms',  value=3)
    population = st.number_input("Population", value=15)
    households = st.number_input('Households', value=5)
    median_income = st.number_input('How much do you earn', value=20000)
    zone = st.selectbox('zone', ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN'])
    rooms_per_house = total_bedrooms/total_rooms
    bedroom_ratio = total_rooms/households

    # Create a dictionary to hold the user input data 
    user_data = {
        'longitude': longitude,
        'Latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income,
        f'zone_{zone}': 1, 
        'rooms_per_house': rooms_per_house,
        'bedroom_ratio': bedroom_ratio,
    }
    return user_data


st.write('Enter the details below to estimate the House Price')
# Collect User Input 
user_data = get_user_input()

#Transforming the required input into the required format 
def prepare_input(data, feature_list):
    input_data = {feature: data.get(feature, 0) for feature in feature_list}
    return np.array([list(input_data.values())])

# Define the features used in the model 

features = [
    'longitude', 'latitude', 'housing_median_age','total_rooms', 'total_bedrooms', 
    'population', 'households', 'median_income', '<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN', 'room_per_house', 'bedroom_ratio'
]
if st.button('Predict'):
    # Format the feature array (update this on actual training input)
    input_array = prepare_input(user_data, features) 
    print(input_array)
    prediction = model.predict(input_array)
    st.subheader('Predicted Price')
    st.write(f'💰 Predicted House Price: ${prediction[0]:,.2f}')
    