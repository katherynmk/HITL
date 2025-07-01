import streamlit as st
import pandas as pd
import numpy as np
import math

st.header("Human-in-the-Loop Warehouse Model")

col1, col2, col3, col4 = st.columns(4)
bank = 6

# ───────────────────── Inbound Dock ─────────────────────
col1.header("Inbound Dock")
a = col1.number_input("Processing Rate ID", min_value=0.01)

# Bank A
col1.subheader("Bank A")
x1 = col1.number_input("volume")
x2 = col1.number_input("staff")
if col1.button("Check Staffing - Inbound A"):
    staff_needed = x1 / (a * bank)
    col1.write(f"Staff Needed: {staff_needed:.2f}")
    col1.write("✅ You have enough staff" if x2 >= staff_needed else "❌ You do not have enough staff")

# Bank B
col1.subheader("Bank B")
x3 = col1.number_input("volume2")
x4 = col1.number_input("staff2")
if col1.button("Check Staffing - Inbound B"):
    staff_needed = x3 / (a * bank)
    col1.write(f"Staff Needed: {staff_needed:.2f}")
    col1.write("✅ You have enough staff" if x4 >= staff_needed else "❌ You do not have enough staff")

# Bank C
col1.subheader("Bank C")
x5 = col1.number_input("volume3")
x6 = col1.number_input("staff3")
if col1.button("Check Staffing - Inbound C"):
    staff_needed = x5 / (a * bank)
    col1.write(f"Staff Needed: {staff_needed:.2f}")
    col1.write("✅ You have enough staff" if x6 >= staff_needed else "❌ You do not have enough staff")

# Bank D
col1.subheader("Bank D")
x7 = col1.number_input("volume4")
x8 = col1.number_input("staff4")
if col1.button("Check Staffing - Inbound D"):
    staff_needed = x7 / (a * bank)
    col1.write(f"Staff Needed: {staff_needed:.2f}")
    col1.write("✅ You have enough staff" if x8 >= staff_needed else "❌ You do not have enough staff")

# ───────────────────── Outbound Dock ─────────────────────
col2.header("Outbound Dock")
b = col2.number_input("Processing Rate OD", min_value=0.01)

# Bank A
col2.subheader("Bank A")
x9 = col2.number_input("volume5")
x10 = col2.number_input("staff5")
if col2.button("Check Staffing - Outbound A"):
    staff_needed = x9 / (b * bank)
    col2.write(f"Staff Needed: {staff_needed:.2f}")
    col2.write("✅ You have enough staff" if x10 >= staff_needed else "❌ You do not have enough staff")

# Bank B
col2.subheader("Bank B")
x11 = col2.number_input("volume6")
x12 = col2.number_input("staff6")
if col2.button("Check Staffing - Outbound B"):
    staff_needed = x11 / (b * bank)
    col2.write(f"Staff Needed: {staff_needed:.2f}")
    col2.write("✅ You have enough staff" if x12 >= staff_needed else "❌ You do not have enough staff")

# Bank C
col2.subheader("Bank C")
x13 = col2.number_input("volume7")
x14 = col2.number_input("staff7")
if col2.button("Check Staffing - Outbound C"):
    staff_needed = x13 / (b * bank)
    col2.write(f"Staff Needed: {staff_needed:.2f}")
    col2.write("✅ You have enough staff" if x14 >= staff_needed else "❌ You do not have enough staff")

# Bank D
col2.subheader("Bank D")
x15 = col2.number_input("volume8")
x16 = col2.number_input("staff8")
if col2.button("Check Staffing - Outbound D"):
    staff_needed = x15 / (b * bank)
    col2.write(f"Staff Needed: {staff_needed:.2f}")
    col2.write("✅ You have enough staff" if x16 >= staff_needed else "❌ You do not have enough staff")

# ───────────────────── Small Sort ─────────────────────
col3.header("Small Sort")
c = col3.number_input("Processing Rate SS", min_value=0.01)

# Bank A
col3.subheader("Bank A")
x17 = col3.number_input("volume9")
x18 = col3.number_input("staff9")
if col3.button("Check Staffing - Small Sort A"):
    staff_needed = x17 / (c * bank)
    col3.write(f"Staff Needed: {staff_needed:.2f}")
    col3.write("✅ You have enough staff" if x18 >= staff_needed else "❌ You do not have enough staff")

# Bank B
col3.subheader("Bank B")
x19 = col3.number_input("volume10")
x20 = col3.number_input("staff10")
if col3.button("Check Staffing - Small Sort B"):
    staff_needed = x19 / (c * bank)
    col3.write(f"Staff Needed: {staff_needed:.2f}")
    col3.write("✅ You have enough staff" if x20 >= staff_needed else "❌ You do not have enough staff")

# Bank C
col3.subheader("Bank C")
x21 = col3.number_input("volume11")
x22 = col3.number_input("staff11")
if col3.button("Check Staffing - Small Sort C"):
    staff_needed = x21 / (c * bank)
    col3.write(f"Staff Needed: {staff_needed:.2f}")
    col3.write("✅ You have enough staff" if x22 >= staff_needed else "❌ You do not have enough staff")

# Bank D
col3.subheader("Bank D")
x23 = col3.number_input("volume12")
x24 = col3.number_input("staff12")
if col3.button("Check Staffing - Small Sort D"):
    staff_needed = x23 / (c * bank)
    col3.write(f"Staff Needed: {staff_needed:.2f}")
    col3.write("✅ You have enough staff" if x24 >= staff_needed else "❌ You do not have enough staff")

# ───────────────────── General Sort ─────────────────────
col4.header("General Sort")
d = col4.number_input("Processing Rate GS", min_value=0.01)

# Bank A
col4.subheader("Bank A")
x25 = col4.number_input("volume13")
x26 = col4.number_input("staff13")
if col4.button("Check Staffing - General Sort A"):
    staff_needed = x25 / (d * bank)
    col4.write(f"Staff Needed: {staff_needed:.2f}")
    col4.write("✅ You have enough staff" if x26 >= staff_needed else "❌ You do not have enough staff")

# Bank B
col4.subheader("Bank B")
x27 = col4.number_input("volume14")
x28 = col4.number_input("staff14")
if col4.button("Check Staffing - General Sort B"):
    staff_needed = x27 / (d * bank)
    col4.write(f"Staff Needed: {staff_needed:.2f}")
    col4.write("✅ You have enough staff" if x28 >= staff_needed else "❌ You do not have enough staff")

# Bank C
col4.subheader("Bank C")
x29 = col4.number_input("volume15")
x30 = col4.number_input("staff15")
if col4.button("Check Staffing - General Sort C"):
    staff_needed = x29 / (d * bank)
    col4.write(f"Staff Needed: {staff_needed:.2f}")
    col4.write("✅ You have enough staff" if x30 >= staff_needed else "❌ You do not have enough staff")

# Bank D
col4.subheader("Bank D")
x31 = col4.number_input("volume16")
x32 = col4.number_input("staff16")
if col4.button("Check Staffing - General Sort D"):
    staff_needed = x31 / (d * bank)
    col4.write(f"Staff Needed: {staff_needed:.2f}")
    col4.write("✅ You have enough staff" if x32 >= staff_needed else "❌ You do not have enough staff")


