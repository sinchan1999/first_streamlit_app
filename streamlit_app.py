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

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

#Putting up a sample selected fruit items, which would be easy for first time users.
streamlit.multiselect("Pick some fruit items:", list(my_fruit_list.index),["Avocado","Strawberries"])
