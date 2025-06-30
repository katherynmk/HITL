import streamlit as st
import pandas as pd
import numpy as np

st.header("Human-in-the-Loop Warehouse Model")

col1, col2, col3, col4 = st.columns(4)


col1.header("Inbound Dock")
a = col1.text_input("Processing Rate ID")
col1.subheader("Bank A")
col1.text_input("volume1") + col1.text_input("staff1")
col1.subheader("Bank B")
col1.text_input("volume2")
col1.text_input("staff2")
col1.subheader("Bank C")
col1.text_input("volume3")
col1.text_input("staff3")
col1.subheader("Bank D")
col1.text_input("volume4") + col1.text_input("staff4")

col2.header("Outbound Dock")
b = col2.text_input("Processing Rate OD")
col2.subheader("Bank A")
col2.text_input("volume5") + col2.text_input("staff5")
col2.subheader("Bank B")
col2.text_input("volume6")
col2.text_input("staff6")
col2.subheader("Bank C")
col2.text_input("volume7")
col2.text_input("staff7")
col2.subheader("Bank D")
col2.text_input("volume8") + col2.text_input("staff8")

col3.header("Small Sort")
c = col3.text_input("Processing Rate SS")
col3.subheader("Bank A")
col3.text_input("volume9") + col3.text_input("staff9")
col3.subheader("Bank B")
col3.text_input("volume10")
col3.text_input("staff10")
col3.subheader("Bank C")
col3.text_input("volume11")
col3.text_input("staff11")
col3.subheader("Bank D")
col3.text_input("volume12") + col3.text_input("staff12")


col4.header("General Sort")
d = col4.text_input("Processing Rate GS")
col4.subheader("Bank A")
col4.text_input("volume13") + col4.text_input("staff13")
col4.subheader("Bank B")
col4.text_input("volume14")
col4.text_input("staff14")
col4.subheader("Bank C")
col4.text_input("volume15")
col4.text_input("staff15")
col4.subheader("Bank D")
col4.text_input("volume16") + col4.text_input("staff16")

st.text_input("Processing Rate: Belt Loaders")
st.text_input("Processing Rate: Smalls Loaders")
st.text_input("Processing Rate: Pallet Jackers")



