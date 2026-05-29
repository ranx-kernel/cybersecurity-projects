import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Advanced Secure Coding Dashboard",
    layout="wide"
)

# -----------------------------
# DATA
# -----------------------------

data = {
    "Vulnerability": [
        "SQL Injection",
        "Command Injection",
        "Hardcoded Secret",
        "Flask Debug Mode"
    ],
    "Severity": [
        "Medium",
        "High",
        "Low",
        "High"
    ],
    "OWASP": [
        "A03 Injection",
        "A03 Injection",
        "A07 Authentication Failures",
        "A05 Security Misconfiguration"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# TITLE
# -----------------------------

st.title("Advanced Secure Coding Review Dashboard")

st.markdown("---")

# -----------------------------
# KPI METRICS
# -----------------------------

total_vulns = len(df)
high = len(df[df["Severity"] == "High"])
medium = len(df[df["Severity"] == "Medium"])
low = len(df[df["Severity"] == "Low"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Vulnerabilities", total_vulns)
col2.metric("High Severity", high)
col3.metric("Medium Severity", medium)
col4.metric("Low Severity", low)

st.markdown("---")

# -----------------------------
# TABLE
# -----------------------------

st.subheader("Detected Vulnerabilities")

st.dataframe(df, use_container_width=True)

# -----------------------------
# CHARTS
# -----------------------------

col5, col6 = st.columns(2)

# Pie Chart
fig1 = px.pie(
    df,
    names="Severity",
    title="Severity Distribution",
    hole=0.4
)

col5.plotly_chart(fig1, use_container_width=True)

# Bar Chart
fig2 = px.histogram(
    df,
    x="OWASP",
    color="Severity",
    title="OWASP Category Distribution"
)

col6.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# RISK SCORE
# -----------------------------

st.markdown("---")

st.subheader("Application Risk Score")

risk_score = 85

st.progress(risk_score)

st.write(f"Overall Risk Score: {risk_score}%")

# -----------------------------
# TIMELINE
# -----------------------------

timeline_data = pd.DataFrame({
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Detected Vulnerabilities": [1, 2, 4, 3, 4]
})

fig3 = px.line(
    timeline_data,
    x="Day",
    y="Detected Vulnerabilities",
    markers=True,
    title="Vulnerability Detection Timeline"
)

st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.success("Secure Coding Review Completed Successfully")