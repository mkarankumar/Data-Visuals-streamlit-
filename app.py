import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Plotting Functions
def histplot(x, data):
    fig, ax = plt.subplots()
    sns.histplot(data[x], ax=ax)
    ax.set_title(f"Histogram of {x}")
    plt.xticks(rotation=90)
    return fig

def countplot(x, data):
    fig, ax = plt.subplots()
    sns.countplot(x=data[x], ax=ax)
    ax.set_title(f"Countplot of {x}")
    plt.xticks(rotation=90)
    return fig

def boxplot(x, y, data):
    fig, ax = plt.subplots()
    sns.boxplot(x=x, y=y, data=data, ax=ax)
    ax.set_title(f"Boxplot: {x} vs {y}")
    plt.xticks(rotation=90)
    return fig

def barplot(x, y, data):
    fig, ax = plt.subplots()
    sns.barplot(x=x, y=y, data=data, ax=ax)
    ax.set_title(f"Barplot: {x} vs {y}")
    plt.xticks(rotation=90)
    return fig

def scatterplot(x, y, data):
    fig, ax = plt.subplots()
    sns.scatterplot(x=x, y=y, data=data, ax=ax)
    ax.set_title(f"Scatterplot: {x} vs {y}")
    plt.xticks(rotation=90)
    return fig

def lineplot(x, y, data):
    fig, ax = plt.subplots()
    sns.lineplot(x=x, y=y, data=data, ax=ax)
    ax.set_title(f"Lineplot: {x} vs {y}")
    plt.xticks(rotation=90)
    return fig

def multivariate_barplot(x, y, z, data):
    fig, ax = plt.subplots(figsize=(10, 5))
    grouped = data.groupby([x, y])[z].mean().unstack()
    grouped.plot(kind="bar", ax=ax)
    ax.set_title(f"{x} vs {y} (mean {z})")
    ax.set_ylabel(f"Mean {z}")
    plt.xticks(rotation=90)
    return fig

def piechart(x, data):
    fig, ax = plt.subplots()
    data[x].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
    ax.set_title(f"Pie Chart of {x}")
    ax.set_ylabel("")
    return fig

# Streamlit App
st.title("Multi-Chart Visualizer")

uploaded = st.file_uploader("Upload CSV or Excel File", type=["csv", "xlsx"])

if uploaded:
    # Load data
    if uploaded.name.endswith(".csv"):
        data = pd.read_csv(uploaded)
    else:
        data = pd.read_excel(uploaded)

    st.subheader("Preview of Data")
    st.dataframe(data)

    cat_cols = data.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
    num_cols = data.select_dtypes(include=["int64", "float64"]).columns.tolist()

    chart_types = [
        "Histogram (1 Num)",
        "Countplot (1 Cat)",
        "Boxplot (Cat vs Num)",
        "Barplot (Cat vs Num)",
        "Scatterplot (Num vs Num)",
        "Lineplot (Num vs Num)",
        "Multivariate Barplot (Cat, Cat, Num)",
        "Pie Chart (1 Cat)"
    ]

    for i in range(8):
        with st.expander(f"Chart Slot {i+1}", expanded=False):
            chart_type = st.selectbox(f"Select chart type for chart {i+1}", chart_types, key=f"chart_type_{i}")

            if chart_type == "Histogram (1 Num)":
                x = st.selectbox("Select Numerical Column", num_cols, key=f"hist_{i}")
                st.pyplot(histplot(x, data))

            elif chart_type == "Countplot (1 Cat)":
                x = st.selectbox("Select Categorical Column", cat_cols, key=f"count_{i}")
                st.pyplot(countplot(x, data))

            elif chart_type == "Boxplot (Cat vs Num)":
                x = st.selectbox("Select Categorical Column", cat_cols, key=f"box_x_{i}")
                y = st.selectbox("Select Numerical Column", num_cols, key=f"box_y_{i}")
                st.pyplot(boxplot(x, y, data))

            elif chart_type == "Barplot (Cat vs Num)":
                x = st.selectbox("Select Categorical Column", cat_cols, key=f"bar_x_{i}")
                y = st.selectbox("Select Numerical Column", num_cols, key=f"bar_y_{i}")
                st.pyplot(barplot(x, y, data))

            elif chart_type == "Scatterplot (Num vs Num)":
                x = st.selectbox("Select X Numerical Column", num_cols, key=f"scatter_x_{i}")
                y = st.selectbox("Select Y Numerical Column", num_cols, key=f"scatter_y_{i}")
                st.pyplot(scatterplot(x, y, data))

            elif chart_type == "Lineplot (Num vs Num)":
                x = st.selectbox("Select X Numerical Column", num_cols, key=f"line_x_{i}")
                y = st.selectbox("Select Y Numerical Column", num_cols, key=f"line_y_{i}")
                st.pyplot(lineplot(x, y, data))

            elif chart_type == "Multivariate Barplot (Cat, Cat, Num)":
                x = st.selectbox("Select 1st Categorical Column", cat_cols, key=f"multi_x_{i}")
                y = st.selectbox("Select 2nd Categorical Column", cat_cols, key=f"multi_y_{i}")
                z = st.selectbox("Select Numerical Column", num_cols, key=f"multi_z_{i}")
                st.pyplot(multivariate_barplot(x, y, z, data))

            elif chart_type == "Pie Chart (1 Cat)":
                x = st.selectbox("Select Categorical Column", cat_cols, key=f"pie_{i}")
                st.pyplot(piechart(x, data))
