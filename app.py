import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Airline Loyalty Analytics",
    page_icon="✈",
    layout="wide"
)

# ------------------------
# Load Data
# ------------------------
data_main = pd.read_csv("data_main.csv")
retention_df = pd.read_csv("retention_dashboard.csv")
feature_importance = pd.read_csv("feature_importance.csv")
relative_profile = pd.read_csv(
    "relative_segment_profile.csv",
    index_col=0
)

# ------------------------
# Sidebar
# ------------------------
st.sidebar.title("✈ Airline Loyalty Analytics")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Customer Segmentation",
        "Churn Prediction",
        "Smart Retention",
        "Business Insights"
    ]
)

# =========================================================
# HOME
# =========================================================
if page == "Home":

    st.title("✈ Airline Loyalty Analytics Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Customers",
        len(data_main)
    )

    col2.metric(
        "Champions",
        len(
            data_main[
                data_main["Customer_Segment"] ==
                "Champions / Premium Travelers"
            ]
        )
    )

    col3.metric(
        "Dormant Customers",
        len(
            data_main[
                data_main["Customer_Segment"] ==
                "Dormant Customers"
            ]
        )
    )

    col4.metric(
        "Churn Rate %",
        round(
            data_main["Hard_Churn"].mean()*100,
            2
        )
    )

    st.markdown("---")

    st.subheader("Customer Segment Distribution")

    fig = px.pie(
        data_main,
        names="Customer_Segment",
        title="Customer Segments"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# CUSTOMER SEGMENTATION
# =========================================================
elif page == "Customer Segmentation":

    st.title("Customer Segmentation")

    st.subheader("Segment Counts")

    fig = px.histogram(
        data_main,
        x="Customer_Segment",
        color="Customer_Segment"
    )

    st.subheader("Normalized Segment Profile Heatmap")

    fig2, ax = plt.subplots(figsize=(12,6))

    sns.heatmap(
            relative_profile,
            annot=True,
            cmap='RdYlBu_r',
            center=1,
            fmt='.2f',
            linewidths=0.5,
            ax=ax
       )

    plt.title(
        "Relative Segment Profiles\n(1 = Average Customer)"
     )

    st.pyplot(fig2)

# =========================================================
# CHURN PREDICTION
# =========================================================
elif page == "Churn Prediction":

    st.title("Customer Churn Risk")

    customer = st.selectbox(
        "Select Customer",
        retention_df.index
    )

    row = retention_df.loc[customer]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Churn Probability",
        f"{row['Churn_Probability']*100:.1f}%"
    )

    col2.metric(
        "Risk Level",
        row["Risk_Level"]
    )

    col3.metric(
        "Segment",
        row["Customer_Segment"]
    )

    st.success(
        f"Recommended Action: {row['Recommended_Action']}"
    )

# =========================================================
# SMART RETENTION
# =========================================================
elif page == "Smart Retention":

    st.title("Smart Retention Dashboard")

    risk_filter = st.multiselect(
        "Filter Risk Level",
        retention_df["Risk_Level"].unique(),
        default=retention_df["Risk_Level"].unique()
    )

    temp = retention_df[
        retention_df["Risk_Level"].isin(risk_filter)
    ]

    st.dataframe(
        temp.sort_values(
            by="Churn_Probability",
            ascending=False
        )
    )

    st.download_button(
        label="Download Retention Actions",
        data=temp.to_csv(index=False),
        file_name="retention_dashboard.csv",
        mime="text/csv"
    )

# =========================================================
# BUSINESS INSIGHTS
# =========================================================
elif page == "Business Insights":

    st.title("Business Insights")

    st.subheader("Feature Importance")

    fig3 = px.bar(
        feature_importance,
        x="Importance",
        y="Feature",
        orientation="h",
        color="Importance"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    st.subheader("Key Findings")

    st.info("""
### Key Findings

- XGBoost achieved the best performance with ROC-AUC = 0.963.
- Total Bookings, Booking Trend and Recency Months are the strongest drivers of churn.
- Behavioral variables are more important than demographic variables.
- Four customer segments were identified:
    - Champions / Premium Travelers
    - Active Regular Customers
    - Occasional Flyers
    - Dormant Customers

### Recommendations

✅ Reward Champions with VIP benefits.

✅ Increase engagement among Occasional Flyers.

✅ Maintain loyalty among Active Regular Customers.

✅ Launch win-back campaigns for Dormant Customers.
""")