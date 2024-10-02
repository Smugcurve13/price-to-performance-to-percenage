import streamlit as st
import pandas as pd

st.title("Price to Performance to Percentage")
st.write("This Tool provide you how much performance your dollars will net you")

num_of_pcs = st.text_input(label="how many pcs you want to compare?")
try:
    num_of_pcs = int(num_of_pcs)
    name=[]
    price=[]
    performance=[]

    pcs_dict = {}

    for num in range(1,num_of_pcs+1):
        name = st.text_input(label=f"enter name of PC {num}")
        price = int(st.text_input(label=f"enter price of PC {num}"))
        performance = int(st.text_input(label=f"enter performance of PC {num}"))

        pcs_dict[f"PC {num}"] = {'name' : name , 'price' : price , 'performance' : performance}
except ValueError:
    pass
try:
    df=pd.DataFrame(pcs_dict)
    print(df)
    price_to_performance=st.write(df)
except NameError:
    pass

st.button(label="Calculate")
st.button("Reset", type="primary")

print(st.session_state)
# display table of pcs after finish entering
# then also add Calculate button
# Then output in different