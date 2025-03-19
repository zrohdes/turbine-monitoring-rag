import streamlit as st
import pandas as pd
import numpy as np
import datetime


def display_dashboard():
    """Display the turbine monitoring dashboard"""
    st.subheader("Turbine Monitoring Dashboard")

    # Create tabs for different turbine types
    tab1, tab2 = st.tabs(["Wind Turbines", "Gas Turbines"])

    with tab1:
        display_wind_turbine_dashboard()

    with tab2:
        display_gas_turbine_dashboard()


def display_wind_turbine_dashboard():
    """Display the wind turbine dashboard"""
    # Create columns for metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Overall Efficiency", value="82.4%", delta="1.2%")

    with col2:
        st.metric(label="Power Output", value="4.2 MW", delta="0.3 MW")

    with col3:
        st.metric(label="Availability", value="98.7%", delta="-0.3%")

    # Generate sample data
    dates = pd.date_range(start=datetime.datetime.now() - datetime.timedelta(days=30),
                          end=datetime.datetime.now(), freq='D')

    power_data = pd.DataFrame({
        'Date': dates,
        'Turbine 1': np.random.normal(4.2, 0.5, len(dates)),
        'Turbine 2': np.random.normal(3.8, 0.4, len(dates)),
        'Turbine 3': np.random.normal(4.5, 0.6, len(dates))
    })

    # Create performance chart
    st.subheader("Power Output (Last 30 Days)")
    st.line_chart(power_data.set_index('Date'))

    # Create maintenance schedule
    st.subheader("Maintenance Schedule")
    maintenance_data = pd.DataFrame({
        'Turbine': ['Turbine 1', 'Turbine 2', 'Turbine 3', 'Turbine 1'],
        'Maintenance Type': ['Routine Inspection', 'Blade Replacement', 'Gearbox Service', 'Electrical System Check'],
        'Scheduled Date': ['2025-03-25', '2025-04-02', '2025-03-28', '2025-04-10'],
        'Status': ['Scheduled', 'Scheduled', 'In Progress', 'Scheduled']
    })

    st.dataframe(maintenance_data, use_container_width=True)


def display_gas_turbine_dashboard():
    """Display the gas turbine dashboard"""
    # Create columns for metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="Thermal Efficiency", value="45.8%", delta="-0.5%")

    with col2:
        st.metric(label="Power Output", value="25.4 MW", delta="1.2 MW")

    with col3:
        st.metric(label="Fuel Consumption", value="5.2 m³/h", delta="-0.3 m³/h", delta_color="inverse")

    # Generate sample data
    dates = pd.date_range(start=datetime.datetime.now() - datetime.timedelta(days=30),
                          end=datetime.datetime.now(), freq='D')

    efficiency_data = pd.DataFrame({
        'Date': dates,
        'Turbine A': np.random.normal(45.8, 1.5, len(dates)),
        'Turbine B': np.random.normal(44.2, 1.2, len(dates))
    })

    # Create performance chart
    st.subheader("Thermal Efficiency (Last 30 Days)")
    st.line_chart(efficiency_data.set_index('Date'))

    # Create alerts
    st.subheader("Recent Alerts")
    alert_data = pd.DataFrame({
        'Timestamp': ['2025-03-19 14:23', '2025-03-18 08:45', '2025-03-17 22:15', '2025-03-15 16:30'],
        'Turbine': ['Turbine A', 'Turbine B', 'Turbine A', 'Turbine B'],
        'Alert Type': ['High Exhaust Temperature', 'Vibration Warning', 'Low Lubricant Pressure', 'Startup Failure'],
        'Status': ['Active', 'Resolved', 'Active', 'Resolved']
    })

    st.dataframe(alert_data, use_container_width=True)