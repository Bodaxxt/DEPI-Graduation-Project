import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# تحميل البيانات
data = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Sidebar
st.sidebar.header("Customer Attrition Dashboard")
st.sidebar.markdown("---")
st.sidebar.write("Created with ❤️ by Eng. Abdallah Ayman")

st.sidebar.markdown("---")

# خيارات الشريط الجانبي
show_data_overview = st.sidebar.checkbox("Show Data Overview")
show_data_info = st.sidebar.checkbox("info about data")
show_visualizations = st.sidebar.checkbox("\Visualizations")
show_eda = st.sidebar.checkbox("(EDA)")

# عنوان التطبيق
st.title("Customer Attrition Analysis Dashboard")

# نظرة عامة على البيانات
if show_data_overview:
    st.header("how Data Overview")
    st.write(data.head(100))

# معلومات عن البيانات
if show_data_info:
    st.header("nfo about data")
    st.write(data.info())

# الرسوم البيانية
if show_visualizations:
    st.header("Visualizations")

    # اختيار نوع الرسم البياني
    chart_type = st.sidebar.selectbox(
        "اختر نوع الرسم البياني",
        ["Barplot - Gender vs Churn", "Countplot - SeniorCitizen", "Countplot - OnlineSecurity", 
         "Countplot - Contract", "Histplot - Tenure", "Lineplot - Churn vs Tenure", 
         "Piechart - PaymentMethod", "Countplot - DeviceProtection", "Countplot - PhoneService", 
         "Piechart - InternetService", "Countplot - InternetService", "Countplot - TechSupport", 
         "Histplot - MonthlyCharges", "Histplot - TotalCharges"]
    )

    if chart_type == "Barplot - Gender vs Churn":
        st.subheader("Barplot - Gender vs Churn")
        fig, ax = plt.subplots()
        sns.barplot(data=data, x="gender", y='Churn', palette='pastel', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Countplot - SeniorCitizen":
        st.subheader("Countplot - SeniorCitizen")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='SeniorCitizen', palette='pastel', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Countplot - OnlineSecurity":
        st.subheader("Countplot - OnlineSecurity")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='OnlineSecurity', hue='Churn', palette='pastel', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Countplot - Contract":
        st.subheader("Countplot - Contract")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='Contract', hue='Churn', palette='pastel', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histplot - Tenure":
        st.subheader("Histplot - Tenure")
        fig, ax = plt.subplots()
        sns.histplot(data=data, x='tenure', bins=30, kde=True, color='skyblue', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Lineplot - Churn vs Tenure":
        st.subheader("Lineplot - Churn vs Tenure")
        churn_tenure = data.groupby('tenure')['Churn'].value_counts().unstack().fillna(0)
        fig, ax = plt.subplots(figsize=(10, 6))
        churn_tenure.plot(kind='line', colormap='Accent', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Piechart - PaymentMethod":
        st.subheader("Piechart - PaymentMethod")
        payment_counts = data['PaymentMethod'].value_counts()
        data1 = payment_counts.values
        labels = payment_counts.index
        colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
        fig, ax = plt.subplots()
        ax.pie(data1, labels=labels, colors=colors, autopct='%.0f%%', startangle=90)
        st.pyplot(fig)

    elif chart_type == "Countplot - DeviceProtection":
        st.subheader("Countplot - DeviceProtection")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='DeviceProtection', hue='Churn', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Countplot - PhoneService":
        st.subheader("Countplot - PhoneService")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='PhoneService', hue='Churn', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Piechart - InternetService":
        st.subheader("Piechart - InternetService")
        Internet_count = data['InternetService'].value_counts()
        data2 = Internet_count.values
        index = Internet_count.index
        colors = ['#ff9999','#66b3ff','#99ff99']
        fig, ax = plt.subplots()
        ax.pie(data2, labels=index, colors=colors, autopct='%.0f%%', startangle=90)
        st.pyplot(fig)

    elif chart_type == "Countplot - InternetService":
        st.subheader("Countplot - InternetService")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='InternetService', hue='Churn', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Countplot - TechSupport":
        st.subheader("Countplot - TechSupport")
        fig, ax = plt.subplots()
        sns.countplot(data=data, x='TechSupport', hue='Churn', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histplot - MonthlyCharges":
        st.subheader("Histplot - MonthlyCharges")
        fig, ax = plt.subplots()
        sns.histplot(data=data, x='MonthlyCharges', kde=True, bins=30, color='lightgreen', ax=ax)
        st.pyplot(fig)

    elif chart_type == "Histplot - TotalCharges":
        st.subheader("Histplot - TotalCharges")
        fig, ax = plt.subplots()
        sns.histplot(data=data, x='TotalCharges', bins=30, kde=True, color='lightcoral', ax=ax)
        st.pyplot(fig)

# تحليل إضافي (EDA)
if show_eda:
    st.header("تحليل إضافي (EDA)")

    # عرض توزيع البيانات
    st.subheader("توزيع البيانات")
    selected_column = st.sidebar.selectbox("اختر عمودًا لعرض توزيعه", data.columns)
    fig, ax = plt.subplots()
    sns.histplot(data[selected_column], kde=True, ax=ax)
    st.pyplot(fig)

    # عرض علاقة بين عمودين
    st.subheader("علاقة بين عمودين")
    col1 = st.sidebar.selectbox("اختر العمود الأول", data.columns)
    col2 = st.sidebar.selectbox("اختر العمود الثاني", data.columns)
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=col1, y=col2, hue='Churn', ax=ax)
    st.pyplot(fig)