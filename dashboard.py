import streamlit as st
import json
import time
from datetime import datetime
import pandas as pd

# Page config
st.set_page_config(
    page_title="Real-Time Orders Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title and description
st.title("📈 Real-Time Order Analytics Dashboard")
st.markdown("""This dashboard shows real-time analytics of order processing system.""")

# Initialize session state for historical data
if 'historical_data' not in st.session_state:
    st.session_state.historical_data = []

# Create columns for metrics
col1, col2 = st.columns(2)

# Create placeholders for charts
chart_placeholder = st.empty()
history_placeholder = st.empty()

while True:
    try:
        # Read current stats
        with open('order_stats.json') as f:
            stats = json.load(f)
            
            # Update metrics
            with col1:
                st.metric(
                    "Orders (Last 10s)",
                    stats["orders"],
                    delta=None
                )
            
            with col2:
                st.metric(
                    "Revenue",
                    f"${stats['revenue']:.2f}",
                    delta=None
                )
            
            # Add to historical data
            st.session_state.historical_data.append({
                'timestamp': datetime.strptime(stats['timestamp'], '%Y-%m-%d %H:%M:%S'),
                'orders': stats['orders'],
                'revenue': stats['revenue']
            })
            
            # Keep only last 30 minutes of data
            if len(st.session_state.historical_data) > 180:  # 30 minutes * 6 data points per minute
                st.session_state.historical_data.pop(0)
            
            # Create DataFrame for visualization
            df = pd.DataFrame(st.session_state.historical_data)
            
            # Plot time series charts
            with chart_placeholder.container():
                st.subheader("📊 Real-Time Metrics")
                
                # Orders chart
                st.line_chart(
                    df.set_index('timestamp')['orders'],
                    use_container_width=True,
                    height=200
                )
                
                # Revenue chart
                st.line_chart(
                    df.set_index('timestamp')['revenue'],
                    use_container_width=True,
                    height=200
                )
            
            # Show recent history in table
            with history_placeholder.container():
                st.subheader("📝 Recent History")
                st.dataframe(
                    df.tail(5).sort_index(ascending=False),
                    use_container_width=True
                )
                
    except FileNotFoundError:
        st.warning("⏳ Waiting for data... Please start the order processor.")
    except json.JSONDecodeError:
        st.error("❌ Error reading data. The data file might be corrupted.")
    except Exception as e:
        st.error(f"❌ An unexpected error occurred: {str(e)}")
    
    time.sleep(5)

