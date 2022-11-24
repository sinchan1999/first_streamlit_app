import streamlit
streamlit.title("Hey Sinchan this side! Starting on Streamlit with Food Menu.")

streamlit.header('Breakfast Menu')
streamlit.text("🍛Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞Avocado Toast")


streamlit.header("Lunch items")
streamlit.text("🍗Chicken Biriany/Paneer Biriany")
streamlit.text("🐟Fish curry / Mushroom curry")
streamlit.text("🍨Ice-cream")

streamlit.header("Dinner items") 
streamlit.text("Rice/Roti")
streamlit.text("Chicken curry")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


#Putting up a sample selected fruit items, which would be easy for first time users.
fruits_selected = streamlit.multiselect("Pick some fruit items:", list(my_fruit_list.index),["Avocado","Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# New section to display Fruityvice API
streamlit.header("Fruityvice Fruit Advice!")

#Adding a Text Entry Box for sending the input
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


#Let's Call the Fruityvice API from Our Streamlit App
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#For Displaying the response
#streamlit.text(fruityvice_response)

# Normalizing the JSON version of the response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Output as a table
streamlit.dataframe(fruityvice_normalized)

#Setting Up Streamlit to Work with Snowflake
import snowflake.connector

#Trying to Query Our Trial Account Metadata 
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
