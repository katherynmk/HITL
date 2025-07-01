import streamlit as st
import pandas as pd
import numpy as np
import math

st.write("Charts")

df = pd.read_csv("hitl_warehouse_data.csv")

# Calculate Staff Needed and Gap
bank_hours = 6
df["StaffNeeded"] = df["Volume"] / (df["ProcessingRate"] * bank_hours)
df["StaffGap"] = df["Staff"] - df["StaffNeeded"]

# ──────────────── Simple Bar Chart: Volume and Staff ────────────────
st.subheader("📊 Volume vs Staff by Area-Bank")
df["Label"] = df["Area"] + " " + df["Bank"]
chart_data = df[["Label", "Volume", "Staff", "StaffNeeded"]].set_index("Label")
st.bar_chart(chart_data)

# ──────────────── Line Chart: Efficiency (Volume per Staff) ────────────────
st.subheader("📈 Efficiency: Volume per Staff")
df["Efficiency"] = df["Volume"] / df["Staff"]
eff_chart = df[["Label", "Efficiency"]].set_index("Label")
st.line_chart(eff_chart)

# ──────────────── Bar Chart: Staff Gap ────────────────
st.subheader("⚠️ Staffing Gap (Positive = Overstaffed)")
gap_chart = df[["Label", "StaffGap"]].set_index("Label")
st.bar_chart(gap_chart)