import streamlit as st
import time
from src.main import monty_hall_simulator

st.title(":zap: Monty Hall Simulator :zap:")

num_of_games = st.number_input(
    'Please enter the number of games you would like to simulate',
    min_value=10, max_value=100000,
    value=100
)

col1, col2 = st.columns(2)

col1.subheader('Number of wins with switching')
col2.subheader('Number of wins without switching')

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_switch = 0
wins_no_switch = 0
for i in range(num_of_games):
    num_wins_with_switch, num_wins_without_switch = monty_hall_simulator(1)
    wins_switch += num_wins_with_switch
    wins_no_switch += num_wins_without_switch

    chart1.add_rows([wins_switch / (i+1)])
    chart2.add_rows([wins_no_switch / (i+1)])

    time.sleep(0.01)
