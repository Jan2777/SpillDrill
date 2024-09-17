import streamlit as st

# Define the layout
st.set_page_config(page_title="SPILLDRILL", page_icon=":oil_drum:")

# Add the app name and logo
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("<h1 style='text-align: left; color: #1f77b4;'>SpillDrill</h1>", unsafe_allow_html=True)
with col2:
    st.image("D:/Downloads/logo-removebg-preview.png", width=100)  # Update the path to your logo file

# Introduction
st.markdown("""
    <h2>Welcome to SPILLDRILL</h2>
    <p>SpillDrill provides a comprehensive platform for oil spill management, offering real-time monitoring, reporting, and alerts to ensure swift response and minimize environmental impact.</p>
""", unsafe_allow_html=True)

# Option buttons
st.markdown("<hr>", unsafe_allow_html=True)

# Buttons for different options
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Report a Spill"):
        st.session_state.option = "Report a Spill"
with col2:
    if st.button("Set Up Alerts"):
        st.session_state.option = "Set Up Alerts"
with col3:
    if st.button("Recent Spills"):
        st.session_state.option = "Recent Spills"

# Handle user selections
if 'option' not in st.session_state:
    st.session_state.option = ""

if st.session_state.option == "Report a Spill":
    st.subheader("Report a Spill")
    with st.form(key='spill_report'):
        name = st.text_input("Your Name")
        source = st.text_input("Source of Spill")
        area = st.text_input("Area of Spill")
        details = st.text_area("Details of Spill")
        submit_button = st.form_submit_button(label="Submit")
        if submit_button:
            st.success("Spill reported successfully!")

elif st.session_state.option == "Set Up Alerts":
    st.subheader("Set Up Alerts")
    st.write("This feature is coming soon! Stay tuned for updates.")

elif st.session_state.option == "Recent Spills":
    st.subheader("Recent Spills")
    spills = [
        ("Red Sea (September 2024)", "A spill threat is looming due to ongoing Houthi missile strikes near vital oil infrastructure in the Red Sea, with concerns of major environmental damage if the conflict escalates.", "IncidentNews"),
        ("Bayou Teche, Louisiana (August 2024)", "A pipeline leak led to a spill in the Bayou Teche area. Local authorities responded quickly, but the event has raised concerns about aging infrastructure in the region.", "IncidentNews"),
        ("Galveston, Texas (August 2024)", "A barge collision near Galveston resulted in a spill affecting coastal waters. Cleanup efforts were launched, but local marine life and fishing activities were impacted.", "Wikipedia"),
        ("North Sea, United Kingdom (August 2024)", "A small oil spill occurred from a North Sea oil platform. The spill was contained swiftly, but it sparked discussions about environmental regulations for offshore drilling.", "IncidentNews"),
        ("Gulf of Mexico (July 2024)", "An offshore rig reported a significant spill due to equipment failure. The incident affected marine ecosystems, and restoration efforts are ongoing.", "Wikipedia")
    ]
    
    for spill in spills:
        st.markdown(f"**{spill[0]}**: {spill[1]} ([Source]({spill[2]}))")
