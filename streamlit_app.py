import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


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


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


#Putting up a sample selected fruit items, which would be easy for first time users.
fruits_selected = streamlit.multiselect("Pick some fruit items:", list(my_fruit_list.index),["Avocado","Strawberries"])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)


#Creating a funtion for the repeatable code block
def get_fruityvice_data(this_fruit_choice):
   
   #Let's Call the Fruityvice API from Our Streamlit App
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    #For Displaying the response  -->  #streamlit.text(fruityvice_response)  
    
    # Normalizing the JSON version of the response 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
 # New section to display Fruityvice API
streamlit.header("Fruityvice Fruit Advice!")
try:
  #Adding a Text Entry Box for sending the input
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information..!!!")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
   
    
    # Output as a table
    #streamlit.dataframe(fruityvice_normalized)
    
except URLError as e:
  Steramlit.error()
  
 

#Stopping the flow past here for Troubleshooting! -->  streamlit.stop()


#Setting Up Streamlit to Work with Snowflake

streamlit.header("The fruit load list contains :")
#Snowflake-related functions
def get_fruit_load_list():
   with my_cur = my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM fruit_load_list")
        return  my_cur.fetchall()
      
#Adding button to load the fruit
if streamlit.button('Get fruit Load List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)



#Adding a Text Entry Box for sending the input
add_my_fruit = streamlit.text_input('What fruit would you like to add?','Kiwi')
streamlit.write('Thanks for adding: ', add_my_fruit)

my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlit')")

