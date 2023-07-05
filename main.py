import requests
import streamlit 
import pandas
import snowflake.connector

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
streamlit.text(my_cur.fetchone())
user_fruit=streamlit.text_input('fruit insert')
button=streamlit.button('insert')
if button:
  my_cur.execute('Insert into pc_rivery_db.public.fruit_load_list (FRUIT_NAME) values (%s)'%user_fruit)
  streamlit.info(my_cur.fetchone())
