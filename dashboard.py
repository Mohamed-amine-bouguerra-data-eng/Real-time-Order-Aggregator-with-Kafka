import streamlit as st
import json
import time

st.set_page_config(page_title="Real-Time Orders Dashboard")

st.title("📈 Real-Time Order Stats")

stats_placeholder = st.empty()

while True:
    try:
        with open('order_stats.json') as f:
            stats = json.load(f)
            stats_placeholder.metric("Orders (last 10s)", stats["orders"])
            stats_placeholder.metric("Revenue", f"${stats['revenue']}")
    except Exception:
        st.write("Waiting for data...")

    time.sleep(5)

