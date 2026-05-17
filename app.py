import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("Student Result Analyzer")

# Read CSV
df = pd.read_csv("students.csv")

# Calculations
df["Total"] = df["Math"] + df["Physics"] + df["Python"]

df["Percentage"] = df["Total"] / 3
df["Total"] = df["Math"] + df["Physics"] + df["Python"]

df["Percentage"] = df["Total"] / 3

# ADD HERE
df["Result"] = df["Percentage"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Show Data
st.subheader("Student Data")
st.dataframe(df)

# Topper
topper = df.loc[df["Percentage"].idxmax()]

st.success(f"Topper of Class: {topper['Name']}")

# Average
average = df["Percentage"].mean()

st.info(f"Class Average: {round(average,2)}")

# Graph
st.subheader("Performance Graph")

fig, ax = plt.subplots()

ax.bar(df["Name"], df["Percentage"])

ax.set_xlabel("Students")
ax.set_ylabel("Percentage")

st.pyplot(fig)
st.dataframe(df)
name = st.text_input("Enter Student Name")

if name:
    student = df[df["Name"] == name]

    st.write(student)
    st.pyplot(fig)

st.caption("Developed by gautham")