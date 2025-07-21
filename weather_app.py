import streamlit as st
import requests

st.title("🌨️ My weather app") 

indian_cities = [
    "Agra", "Ahmedabad", "Ajmer", "Akola", "Aligarh", "Allahabad", "Amravati", "Amritsar", "Asansol", "Aurangabad",
    "Bareilly", "Belgaum", "Bhilai", "Bhiwandi", "Bhopal", "Bhubaneswar", "Bikaner", "Chandigarh", "Chennai", "Coimbatore",
    "Cuttack", "Dehradun", "Delhi", "Dhanbad", "Durgapur", "Erode", "Faridabad", "Firozabad", "Gaya", "Ghaziabad",
    "Gorakhpur", "Gulbarga", "Guntur", "Gurgaon", "Guwahati", "Gwalior", "Howrah", "HubliDharwad", "Hyderabad", "Indore",
    "Jabalpur", "Jaipur", "Jalandhar", "Jammu", "Jamnagar", "Jamshedpur", "Jhansi", "Jodhpur", "Kalyan-Dombivli", "Kanpur",
    "Kochi", "Kolhapur", "Kolkata", "Kota", "Kurnool", "Loni", "Lucknow", "Ludhiana", "Madurai", "Maheshtala",
    "Malegaon", "Mangalore", "Meerut", "Mira-Bhayandar","Mohali", "Mumbai", "Mysore", "Nagpur", "Nanded", "Nashik", "Navi Mumbai",
    "Nellore", "Noida", "Patiala", "Patna", "Pune", "Raipur", "Rajkot", "Rourkela", "Saharanpur", "Salem", "Sangli",
    "Siliguri", "Solapur", "Srinagar", "Surat", "Tiruchirappalli", "Tirunelveli", "Tiruppur", "Thane", "Udaipur", "Ujjain",
    "Ulhasnagar", "Vadodara", "Varanasi", "Vasai-Virar", "Vijayawada", "Visakhapatnam", "Warangal"
]

API_KEY="99ee855371b0f537862465aacda17cf8"

choice= st.selectbox("Choose your city ", indian_cities)

if choice:
    url=f"https://api.openweathermap.org/data/2.5/weather?q={choice}&appid={API_KEY}"

    responce=requests.get(url)

    if responce.status_code==200:
        st.write("API working")
        #st.json(responce.json())
        weather_info=responce.json()
        st.write(weather_info["weather"][0]["main"])

        st.write(weather_info["main"]["temp"])

    else:
        st.write("Something went wrong...")
       
 
    # st.write(f"{responce}")
