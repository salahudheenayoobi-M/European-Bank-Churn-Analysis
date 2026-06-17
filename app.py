import pandas as pd
import plotly.express as px
import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="European Bank Churn Analysis", layout="wide")
st.title("European Bank Churn Analysis Dashboard")

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("European_Bank.csv")
    return df

df = load_data()

# -----------------------------
# Sidebar filters
# -----------------------------
st.sidebar.header("Filters")

geography_options = sorted(df['Geography'].unique())
gender_options = sorted(df['Gender'].unique())
age_group_options = sorted(df['AgeGroup'].dropna().unique())

selected_geography = st.sidebar.multiselect(
    "Geography", options=geography_options, default=geography_options
)
selected_gender = st.sidebar.multiselect(
    "Gender", options=gender_options, default=gender_options
)
selected_age_group = st.sidebar.multiselect(
    "AgeGroup", options=age_group_options, default=age_group_options
)

# Apply filters
filtered_df = df[
    (df['Geography'].isin(selected_geography)) &
    (df['Gender'].isin(selected_gender)) &
    (df['AgeGroup'].isin(selected_age_group))
]

if filtered_df.empty:
    st.warning("No data matches the selected filters. Please adjust your selections.")
    st.stop()

# -----------------------------
# KPI Row
# -----------------------------
total_customers = len(filtered_df)
churned_customers = int(filtered_df['Exited'].sum())
retained_customers = total_customers - churned_customers
churn_rate = (churned_customers / total_customers) * 100 if total_customers > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Retained Customers", f"{retained_customers:,}")
col4.metric("Churn Rate", f"{churn_rate:.2f}%")

st.markdown("---")

# -----------------------------
# Helper function for churn-rate-by-segment tables
# -----------------------------
def churn_by_segment(data, column):
    grouped = data.groupby(column)['Exited'].agg(['sum', 'count']).reset_index()
    grouped.columns = [column, 'ChurnCount', 'TotalCount']
    grouped['ChurnRate'] = (grouped['ChurnCount'] / grouped['TotalCount'] * 100).round(2)
    return grouped

# -----------------------------
# Tabs for organization
# -----------------------------
tab1, tab2, tab3, tab4 = st.tabs(
    ["Overview", "Geography & Demographics", "Financial Profile", "Drill-Down Data"]
)

# ---- TAB 1: Overview ----
with tab1:
    st.subheader("Overall Churn Split")

    churn_labels = filtered_df['Exited'].map({0: 'Retained', 1: 'Churned'})
    churn_counts = churn_labels.value_counts().reset_index()
    churn_counts.columns = ['Status', 'Count']

    fig_overall = px.pie(
        churn_counts, names='Status', values='Count', hole=0.4,
        title='Overall Customer Churn',
        color_discrete_sequence=['#2ecc71', '#e74c3c']
    )
    st.plotly_chart(fig_overall, use_container_width=True)

# ---- TAB 2: Geography & Demographics ----
with tab2:
    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Churn by Geography")
        geo_churn = churn_by_segment(filtered_df, 'Geography')
        fig_geo = px.bar(
            geo_churn, x='Geography', y='ChurnRate', color='Geography',
            text='ChurnRate', title='Churn Rate by Geography'
        )
        st.plotly_chart(fig_geo, use_container_width=True)

        st.subheader("Churn by Age Group")
        Age_churn = churn_by_segment(filtered_df, 'AgeGroup')
        fig_age = px.bar(
            Age_churn, x='AgeGroup', y='ChurnRate', color='AgeGroup',
            text='ChurnRate', title='Churn Rate by Age Group'
        )
        st.plotly_chart(fig_age, use_container_width=True)

    with col_b:
        st.subheader("Churn by Gender")
        gender_churn = churn_by_segment(filtered_df, 'Gender')
        fig_gender = px.bar(
            gender_churn, x='Gender', y='ChurnRate', color='Gender',
            text='ChurnRate', title='Churn Rate by Gender'
        )
        st.plotly_chart(fig_gender, use_container_width=True)

        st.subheader("Churn by Tenure Group")
        tenure_churn = churn_by_segment(filtered_df, 'TenureGroup')
        fig_tenure = px.bar(
            tenure_churn, x='TenureGroup', y='ChurnRate', color='TenureGroup',
            text='ChurnRate', title='Churn Rate by Tenure Group'
        )
        st.plotly_chart(fig_tenure, use_container_width=True)

# ---- TAB 3: Financial Profile (High-Value Customer Explorer) ----
with tab3:
    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("Churn by Credit Score Band")
        credit_churn = churn_by_segment(filtered_df, 'CreditBand')
        fig_credit = px.bar(
            credit_churn, x='CreditBand', y='ChurnRate', color='CreditBand',
            text='ChurnRate', title='Churn Rate by Credit Band'
        )
        st.plotly_chart(fig_credit, use_container_width=True)

    with col_d:
        st.subheader("Churn by Balance Segment")
        balance_churn = churn_by_segment(filtered_df, 'BalanceSegment')
        fig_balance = px.bar(
            balance_churn, x='BalanceSegment', y='ChurnRate', color='BalanceSegment',
            text='ChurnRate', title='Churn Rate by Balance Segment'
        )
        st.plotly_chart(fig_balance, use_container_width=True)

    st.markdown("---")
    st.subheader("High-Value Customer Explorer")

    high_value_df = filtered_df[filtered_df['BalanceSegment'] == 'High']
    hv_total = len(high_value_df)
    hv_churned = int(high_value_df['Exited'].sum())
    hv_rate = (hv_churned / hv_total * 100) if hv_total > 0 else 0

    hv_col1, hv_col2, hv_col3 = st.columns(3)
    hv_col1.metric("High-Balance Customers", f"{hv_total:,}")
    hv_col2.metric("High-Balance Churned", f"{hv_churned:,}")
    hv_col3.metric("High-Balance Churn Rate", f"{hv_rate:.2f}%")

# ---- TAB 4: Drill-Down Data ----
with tab4:
    st.subheader("Filtered Customer Data")
    st.write(f"Showing {len(filtered_df):,} customers matching current filters.")
    st.dataframe(filtered_df, use_container_width=True)

    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_churn_data.csv",
        mime="text/csv"
    )