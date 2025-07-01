import streamlit as st
import json
import time
from pathlib import Path

st.set_page_config(page_title="Real-Time Orders Dashboard")
st.title("📊 Live Order Window Stats")

placeholder = st.empty()

def load_history():
    path = Path("order_stats_history.json")
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []

while True:
    history = load_history()
    if history:
        placeholder.table(history[-10:])
    else:
        st.info("Waiting for data...")
    time.sleep(3)
