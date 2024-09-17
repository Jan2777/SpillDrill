import streamlit as st
import folium
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

# Sample data for demonstration purposes
def load_oil_spill_data():
    # Placeholder for loading actual data
    return pd.DataFrame({
        'Latitude': [10.0, 20.0, 30.0],
        'Longitude': [20.0, 30.0, 40.0],
        'Description': ['Spill A', 'Spill B', 'Spill C']
    })

def display_facts():
    st.title('Facts on Oil Spills')
    st.write("""
    - Oil spills can have devastating effects on marine life and coastal environments.
    - They can result from shipwrecks, drilling accidents, or pipeline leaks.
    - Cleanup operations are complex and can take years.
    """)

def display_map():
    st.title('Oil Spills Map')

    # Load and display the static map image
    image = Image.open(r"D:\Downloads\mapp.png")  # Update with your image file path
    st.image(image, caption='Oil Spills Map', use_column_width=True)

def prediction_page():
    st.title('Prediction Page')
    components.iframe("https://marinecadastre.gov/accessais/", height=800)
    st.write('Here you can add prediction algorithms for future oil spills.')

def nearby_shores_page():
    st.title('Historical and Statistical effects of Spills in nearby Coastal Regions')
    
    st.write('Oil spills have profound effects on coastal areas, leading to significant environmental, economic, and health impacts.')
    st.write('Exxon Valdez Spill (1989): Released approximately 11 million gallons of crude oil, causing extensive damage.')
    st.write('Deepwater Horizon Spill (2010): Discharged around 4.9 million barrels (205 million gallons) of oil, with severe consequences.')
    st.subheader('Impact on Coastal Areas:')
    st.write('Marine Life Devastation: The Exxon Valdez spill led to the death of over 100,000 marine animals, including seabirds, fish, and marine mammals. Long-term effects include persistent reproductive issues and habitat loss.')
    st.write('Economic Losses: The Deepwater Horizon spill resulted in approximately $6.2 billion in losses for the Gulf Coast seafood industry and significant declines in tourism revenue, affecting local economies.')
    st.write('Ecosystem Damage: Oil pollution can destroy critical coastal ecosystems such as mangroves and coral reefs. For instance, the Deepwater Horizon spill caused extensive damage to 1,300 miles of coastline.')
    st.write('Health Risks: Coastal communities exposed to oil spills face increased health risks, including respiratory problems and skin conditions. Studies have shown elevated rates of these health issues in affected populations.')
    routes = {
        "Persian Gulf to United States (Gulf of Mexico)": {
            "coasts": [
                "Persian Gulf", "Strait of Hormuz", "Arabian Sea", "Gulf of Aden", 
                "Red Sea", "Suez Canal", "Mediterranean Sea", "Strait of Gibraltar", 
                "Atlantic Ocean", "Gulf of Mexico"
            ],
            "spill_areas": [
                "Persian Gulf", "Strait of Hormuz", "Suez Canal", "Gulf of Mexico"
            ]
        },
        "West Africa (Nigeria) to Europe": {
        "coasts": [
            "Gulf of Guinea", "Cape Verde", "Canary Islands", "Strait of Gibraltar", 
            "Iberian Peninsula", "Bay of Biscay", "English Channel", "North Sea"
        ],
        "spill_areas": [
            "Gulf of Guinea", "Strait of Gibraltar", "Bay of Biscay", "North Sea"
        ]
    },
    "Middle East to China (East Asia)": {
        "coasts": [
            "Persian Gulf", "Arabian Sea", "Indian Ocean", "Strait of Malacca", 
            "South China Sea", "East China Sea", "Yellow Sea"
        ],
        "spill_areas": [
            "Strait of Malacca", "South China Sea", "East China Sea"
        ]
    },
    "Russia (Arctic) to Europe": {
        "coasts": [
            "Barents Sea", "Norwegian Sea", "North Sea", "English Channel", 
            "Celtic Sea", "Bay of Biscay"
        ],
        "spill_areas": [
            "Barents Sea", "North Sea", "Bay of Biscay"
        ]
    },
    "Canada (Alberta Oil Sands) to United States (California)": {
        "coasts": [
            "Vancouver Coast", "Pacific Ocean", "California Coast"
        ],
        "spill_areas": [
            "Vancouver Coast", "California Coast"
        ]
    },
    "Middle East to India": {
        "coasts": [
            "Persian Gulf", "Arabian Sea", "Indian Coastline (Mumbai)", "Bay of Bengal"
        ],
        "spill_areas": [
            "Arabian Sea", "Indian Coastline"
        ]
    },
    "North Sea (Norway) to the United States (East Coast)": {
        "coasts": [
            "North Sea", "English Channel", "Atlantic Ocean", "East Coast (USA)"
        ],
        "spill_areas": [
            "North Sea", "Atlantic Ocean", "U.S. East Coast"
        ]
    },
    "Mexico (Gulf of Mexico) to Japan": {
        "coasts": [
            "Gulf of Mexico", "Caribbean Sea", "Panama Canal", "Pacific Ocean", 
            "Japanese Archipelago"
        ],
        "spill_areas": [
            "Gulf of Mexico", "Panama Canal", "Pacific Ocean"
        ]
    },
    "South America (Brazil) to Europe": {
        "coasts": [
            "Brazilian Coast", "Atlantic Ocean", "Canary Islands", "Bay of Biscay", 
            "English Channel"
        ],
        "spill_areas": [
            "Brazilian Coast", "Bay of Biscay", "English Channel"
        ]
    },
    "Saudi Arabia to Australia": {
        "coasts": [
            "Persian Gulf", "Arabian Sea", "Indian Ocean", "Australian Western Coast"
        ],
        "spill_areas": [
            "Arabian Sea", "Indian Ocean", "Western Australia"
        ]
    },
    "Norway to Spain": {
        "coasts": [
            "North Sea", "English Channel", "Bay of Biscay", "Iberian Peninsula (Spain)"
        ],
        "spill_areas": [
            "North Sea", "English Channel", "Bay of Biscay"
        ]
    },
    "Angola to China": {
        "coasts": [
            "South Atlantic Ocean", "Cape of Good Hope", "Indian Ocean", "Strait of Malacca", 
            "South China Sea"
        ],
        "spill_areas": [
            "Cape of Good Hope", "Strait of Malacca", "South China Sea"
        ]
    },
    "Russia (Vladivostok) to South Korea": {
        "coasts": [
            "Sea of Japan", "Korean Peninsula"
        ],
        "spill_areas": [
            "Sea of Japan", "Korean Peninsula"
        ]
    },
    "Brazil to South Africa": {
        "coasts": [
            "Brazilian Coast", "South Atlantic Ocean", "South African Coast"
        ],
        "spill_areas": [
            "Brazilian Coast", "South Atlantic", "South African Coast"
        ]
    },
    "United States (Gulf Coast) to Western Europe": {
        "coasts": [
            "Gulf of Mexico", "Atlantic Ocean", "English Channel", "Western Europe"
        ],
        "spill_areas": [
            "Gulf of Mexico", "Atlantic Ocean", "English Channel"
        ]
    }
}

    selected_route = st.selectbox("Choose a shipping route:", list(routes.keys()))

    if selected_route:
        coasts = routes[selected_route]["coasts"]
        spill_areas = routes[selected_route]["spill_areas"]
    
        df_coasts = pd.DataFrame({"Coasts Crossed": coasts})
        df_spill_areas = pd.DataFrame({"Potential Spill Areas": spill_areas})

        st.subheader("Coasts Crossed:")
        st.table(df_coasts)
        st.subheader("Potential Spill Areas:")
        st.table(df_spill_areas)

def marine_life_impact_page():
    st.title('Marine Life Impact')
    st.write("Oil spills pose a significant threat to the environment, marine ecosystems, and coastal economies. Events like the Exxon Valdez and Deepwater Horizon spills have shown the immense costs of oil spills, both economically and environmentally. With clean-up costs often reaching billions of dollars, the need for real-time monitoring and prediction systems like SpillDrill has never been more urgent.")
    st.image("D:\Downloads\pbii.png", caption="Impact of Various Types of Oil Spills on Marine Birds and Mammals")
    st.title('AIS-Automatic Identification System')
    st.write("AIS enables early detection of oil spills by tracking ships in high-risk areas, allowing rapid response to minimize environmental impact. By predicting spill trajectories based on real-time data, it helps protect coastal communities and marine life. Additionally, AIS integration with satellite images ensures accurate spill verification and targeted clean-up efforts. Let's see it's working in a visualised mode below:")
    st.image("D:\Downloads\IMG-20240908-WA0012.jpg",caption="Working of AIS system on cargo ships used for oil transportation")
    st.write("Combining AIS data with satellite imagery and pressure density measurements helps verify spills more precisely. This system models the potential spread of oil, factoring in environmental elements such as wind and ocean currents, providing critical insights for efficient containment and mitigation strategies.")
st.set_page_config(page_title="SpillDrill", page_icon=":oil_drum:", layout="wide")

# Sidebar menu with dropdown
with st.sidebar:
    st.image(r"D:\Downloads\logo-removebg-preview.png", width=200)
    st.title("SpillDrill")
    page = st.selectbox("Select a Page", ["Home", "Prediction", "Nearby Shores", "Marine Life Impact"])

# Apply color themes
st.markdown("""
    <style>
        .stApp { background-color: #003366; }
        .css-1d391kg { background-color: #DCEBF7; }
        .css-1v0mbdj { background-color: #003366; color: white; }
    </style>
    """, unsafe_allow_html=True)

if page == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h1 style='text-align: left; color: white; font: Magical Mystery Tour'>Welcome to SpillDrill!</h1>", unsafe_allow_html=True)
    with col2:
        st.image("D:\Downloads\logoo-removebg-preview.png", width=200)  # Update the path to your logo file

    # Introduction
    st.markdown("""
        <h2>Empowering Ocean Conservation</h2>
        <p>Oil spills in the ocean critically disrupt marine ecosystems, pollute habitats, and lead to long-term environmental and economic damage.We provides a comprehensive platform for oil spill management, offering real-time monitoring, reporting, and alerts to ensure swift response and minimize environmental impact.We also integrate remedial measures to mitigate the damages caused. By integratting satellite image prediction along with AIS, we aim to provide alerts with atmost precision along with other necessary features.</p>
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
    display_map()
elif page == "Prediction":
    st.title("Prediction of Spread Over Time")
    st.write("Based on our analysis, it typically takes an average of 1-2 months to respond to and resolve an oil spill after an alert has been issued. To help you understand the seriousness of the situation, we provide predictions on how much the spread of oil spills could be in certain areas over the next few months")

    st.subheader("Factors Considered")
    st.write("""
        To make accurate predictions, we take into account:
        - **Average Wind Speed**: Wind can significantly affect the spread of oil spills.
        - **Historical Spill Data**: Analysis of past spills helps us understand potential future spread patterns.
        - **Geographic Factors**: Coastal geography and sea currents influence spill dynamics.
    """)
    prediction_page()
elif page == "Nearby Shores":
    nearby_shores_page()
elif page == "Marine Life Impact":
    marine_life_impact_page()
