import streamlit as st
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


@st.cache_resource
def load_documents():
    """Load and process documents from the documents directory"""
    try:
        # Check if documents directory exists
        if not os.path.exists("./documents/"):
            os.makedirs("./documents/")
            # Create sample documents for demonstration
            create_sample_documents()

        # Load documents from a directory
        loader = DirectoryLoader("./documents/", glob="**/*.txt", loader_cls=TextLoader)
        documents = loader.load()

        if not documents:
            st.warning("No documents found. Using sample documents.")
            create_sample_documents()
            documents = loader.load()

        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        doc_chunks = text_splitter.split_documents(documents)

        return doc_chunks
    except Exception as e:
        st.error(f"Error loading documents: {e}")
        return []


def create_sample_documents():
    """Create sample documents for demonstration purposes"""
    # Create directories if they don't exist
    os.makedirs("./documents/wind_turbines/", exist_ok=True)
    os.makedirs("./documents/gas_turbines/", exist_ok=True)
    os.makedirs("./documents/general/", exist_ok=True)

    # Sample Wind Turbine documents
    with open("./documents/wind_turbines/maintenance.txt", "w") as f:
        f.write("""
Wind Turbine Maintenance Guide

Routine Maintenance Schedule:
1. Weekly inspection of blades for damage or debris
2. Monthly check of electrical connections and systems
3. Quarterly inspection of gearbox and lubrication systems
4. Semi-annual check of structural integrity
5. Annual full inspection and component replacement as needed

Common Issues:
- Blade damage from debris or lightning strikes
- Gearbox failure due to inadequate lubrication
- Electrical system faults from power surges
- Yaw system misalignment affecting efficiency

Maintenance Tips:
- Always conduct inspections during low wind conditions
- Use drones for initial blade inspections to identify issues
- Maintain proper lubrication schedules for all moving parts
- Keep detailed maintenance logs for each turbine
- Monitor vibration patterns to detect early signs of failure
        """)

    with open("./documents/wind_turbines/optimization.txt", "w") as f:
        f.write("""
Wind Turbine Optimization Strategies

Efficiency Optimization:
1. Blade Pitch Control: Adjust blade pitch angles to optimize performance across different wind speeds
2. Yaw Alignment: Ensure turbine is facing directly into the wind to maximize energy capture
3. Cut-in and Cut-out Speeds: Optimize turbine operation parameters based on local wind patterns
4. Wake Effect Management: Position turbines to minimize wake effects on downstream turbines

Performance Monitoring:
- Track power curve to identify deviations from expected performance
- Monitor wind speed and direction correlation with power output
- Analyze vibration data to detect inefficiencies
- Compare actual vs. theoretical output based on wind conditions

Advanced Optimization Techniques:
- Machine learning algorithms for predictive maintenance
- Dynamic adjustment of parameters based on real-time data
- SCADA system integration for centralized monitoring and control
- Seasonal adjustment of operating parameters based on historical data
        """)

    # Sample Gas Turbine documents
    with open("./documents/gas_turbines/maintenance.txt", "w") as f:
        f.write("""
Gas Turbine Maintenance Guide

Maintenance Schedule:
1. Daily visual inspections and performance monitoring
2. Weekly check of fuel systems and filters
3. Monthly inspection of combustion chamber and turbine blades
4. Quarterly analysis of lubricating oil and filter replacement
5. Annual hot gas path inspection and component replacement

Critical Components:
- Compressor: Check for blade fouling, erosion, or damage
- Combustion Chamber: Inspect for hotspots, cracks, or fuel nozzle issues
- Turbine Section: Check for blade erosion, cooling passage blockages
- Exhaust System: Inspect for corrosion or thermal fatigue
- Bearings and Seals: Check for wear and proper lubrication

Recommended Practices:
- Implement water washing procedures to remove compressor deposits
- Regular borescope inspections to identify early signs of damage
- Monitor exhaust temperature spreading to detect combustion issues
- Track vibration patterns to identify bearing or alignment problems
- Maintain proper fuel quality and filtration to prevent nozzle problems
        """)

    with open("./documents/gas_turbines/optimization.txt", "w") as f:
        f.write("""
Gas Turbine Optimization Strategies

Performance Optimization:
1. Inlet Air Cooling: Increase mass flow and power output during high ambient temperatures
2. Combustion Tuning: Optimize fuel-air ratio for efficiency and emissions
3. Compressor Washing: Maintain clean compressor blades for optimal efficiency
4. Heat Recovery: Implement combined cycle systems to utilize exhaust heat

Efficiency Factors:
- Inlet air temperature and pressure
- Compression ratio optimization
- Turbine inlet temperature control
- Exhaust back pressure management
- Part-load operation strategies

Advanced Monitoring:
- Real-time heat rate calculations
- Compressor efficiency tracking
- Turbine section efficiency monitoring
- Combustion dynamics analysis
- Emissions monitoring and control

Optimization Tools:
- Digital twins for performance comparison
- Predictive analytics for maintenance scheduling
- Automated control systems for parameter adjustment
- Machine learning algorithms for operational optimization
        """)

    # Sample General documents
    with open("./documents/general/best_practices.txt", "w") as f:
        f.write("""
Turbine Operation Best Practices

General Guidelines:
1. Implement proper startup and shutdown procedures to minimize thermal stress
2. Maintain comprehensive documentation of all maintenance activities
3. Train operators in optimal control strategies and emergency procedures
4. Establish clear communication protocols between field and control room staff
5. Develop and maintain equipment-specific operating procedures

Data Management:
- Implement robust data collection and storage systems
- Establish key performance indicators (KPIs) for each turbine
- Regularly analyze historical data to identify trends and opportunities
- Use data visualization tools to communicate performance metrics
- Implement automated alerts for performance deviations

Safety Considerations:
- Develop and enforce lockout/tagout procedures
- Conduct regular safety training for all personnel
- Implement confined space entry protocols
- Establish emergency response procedures
- Maintain up-to-date safety equipment and systems

Continuous Improvement:
- Regularly review and update operating procedures
- Benchmark performance against industry standards
- Incorporate lessons learned from incidents and near-misses
- Implement regular performance reviews and improvement initiatives
- Stay current with industry advancements and best practices
        """)

    with open("./documents/general/troubleshooting.txt", "w") as f:
        f.write("""
Turbine Troubleshooting Guide

Common Issues and Solutions:

1. Decreased Power Output
   - Check for inlet air restrictions or filter fouling
   - Verify proper fuel quality and pressure
   - Inspect turbine blades for deposits or damage
   - Check control system for improper settings
   - Verify exhaust system for blockages or back pressure

2. Excessive Vibration
   - Check for rotor imbalance or misalignment
   - Inspect bearings for wear or damage
   - Verify proper lubrication levels and quality
   - Check for loose components or mounting issues
   - Inspect for foreign object damage

3. High Exhaust Temperature
   - Check for combustion system issues
   - Verify fuel quality and proper fuel-air ratio
   - Inspect cooling systems for blockages
   - Check for turbine section damage or deposits
   - Verify proper control system operation

4. Control System Malfunctions
   - Check power supply and electrical connections
   - Verify sensor calibration and operation
   - Inspect for software issues or outdated parameters
   - Check communication links between components
   - Verify proper grounding and shielding

Diagnostic Approach:
- Start with the simplest explanations before complex troubleshooting
- Use trend data to identify when the problem began
- Compare current performance with historical baseline data
- Isolate variables by changing one parameter at a time
- Document all troubleshooting steps and outcomes
        """)