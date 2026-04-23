"""
Program: Brown_app.py
Author: David Brown
Date: 4/22/26
Purpose: build a Streamlit dashboard to analyze hospital admission trends
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


"""
Dashboard title
"""
st.title("Cardiology Patient Dashboard")


"""
Upload hospital dataset
"""
uploaded_file = st.file_uploader(
    "Upload your dataset (CSV or Excel file)",
    type=["csv", "xlsx"]
)


if uploaded_file is not None:

    """
    Read uploaded file
    """
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")


    """
    Show first few rows
    """
    st.subheader("First Few Data Samples")
    st.dataframe(df.head())


    """
    Show last few rows
    """
    st.subheader("Last Few Data Samples")
    st.dataframe(df.tail())


    """
    Added summary statistics for numerical data
    """
    st.subheader("Summary of Statistical Properties")
    st.dataframe(df.describe())


    """
    Added monthly admissions count table
    """
    st.subheader("Admissions per Month")

    if "month year" in df.columns:
        monthly = df.groupby("month year").size().reset_index(name="Admissions")
        st.dataframe(monthly)


        """
        Added monthly admissions chart
        """
        fig, ax = plt.subplots()
        ax.plot(monthly["month year"], monthly["Admissions"])
        ax.set_ylabel("Number of Admissions")
        ax.set_xlabel("Month - Year")
        ax.set_title("Admissions Over Time")
        plt.xticks(rotation=45)

        st.pyplot(fig)

    else:
        st.error("Column 'month year' not found in dataset.")

else:
    st.info("Please upload a dataset to begin.")
