
# Keep the main thread alive to listen to messages.
import streamlit as st
st.set_page_config(layout="wide")
import os
import pandas as pd
import numpy as np
import time
from google.cloud import firestore
import pydeck as pdk
from shapely import wkt
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium
import psycopg2
from sqlalchemy import create_engine
import json

if not "sleep_time" in st.session_state:
    st.session_state.sleep_time = 30

if not "auto_refresh" in st.session_state:
    st.session_state.auto_refresh = True

auto_refresh = st.sidebar.checkbox('Auto Refresh?', st.session_state.auto_refresh)

if auto_refresh:
    number = st.sidebar.number_input('Refresh rate in seconds', value=st.session_state.sleep_time)
    st.session_state.sleep_time = number

# Database connection setup
db_user = 
db_pass = 
db_name = 
db_host = 
db_port = 
# PostgreSQL connection string
database_url = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = create_engine(database_url)

start_wkt = "POINT (-0.152564 51.503921)"
end_wkt = "POINT (-0.152628 51.503938)"

x_start, y_start = wkt.loads(start_wkt).coords.xy
x_end, y_end = wkt.loads(end_wkt).coords.xy

# Streamlit app title
st.title('CE TECH DAY 2024 - LEADERBOARD')
st.write("")
# Function to fetch participant locations
def get_participants_location():
    participants_ref = db.collection('race_participants')
    docs = participants_ref.stream()

    data = {
        'latitude': [],
        'longitude': [],
        'participant_id': []
    }

    for doc in docs:
        doc_data = doc.to_dict()
        data['latitude'].append(doc_data['latitude'])
        data['longitude'].append(doc_data['longitude'])
        data['participant_id'].append(doc.id)

    return pd.DataFrame(data)

m = folium.Map(zoom_start=10)
folium.Marker(location=(y_start[0], x_start[0]),
  icon=folium.Icon(color="green", icon="flag"), popup="Start").add_to(m)
folium.Marker(location=(y_end[0], x_end[0]),
  icon=folium.Icon(color="red", icon="flag"), popup="Finish").add_to(m)

x = [-0.152564,-0.152757,-0.152886,-0.153251,-0.15368,-0.154924,-0.156469,-0.158207,-0.160289,-0.163422,-0.168014,-0.171039,-0.174515,-0.174708,-0.174687,-0.174687,-0.174301,-0.173764,-0.173271,-0.17312,-0.172992,-0.172691,-0.172477,-0.172112,-0.171769,-0.171125,-0.170588,-0.170009,-0.16958,-0.169022,-0.167155,-0.164344,-0.163958,-0.163679,-0.163143,-0.162542,-0.161533,-0.160933,-0.160117,-0.156233,-0.153294,-0.152779,-0.152628]
x_geo = [-0.152564,-0.152757,-0.152886,-0.153251,-0.15368,-0.154924,-0.156469,-0.158207,-0.160289,-0.163422,-0.168014,-0.171039,-0.174515,-0.174708,-0.174687,-0.174687,-0.174301,-0.173764,-0.173271,-0.17312,-0.172992,-0.172691,-0.172477,-0.172112,-0.171769,-0.171125,-0.170588,-0.170009,-0.16958,-0.169022,-0.167155,-0.164344,-0.163958,-0.163679,-0.163143,-0.162542,-0.161533,-0.160933,-0.160117,-0.156233,-0.153294,-0.152779,-0.152628]
y = [51.503921,51.503574,51.503413,51.50328,51.50316,51.50312,51.502906,51.502799,51.502612,51.502398,51.502225,51.502198,51.502171,51.502412,51.502692,51.503213,51.503881,51.504535,51.505283,51.505617,51.505884,51.506232,51.506525,51.506806,51.506752,51.506592,51.506432,51.506272,51.506111,51.506018,51.506018,51.506031,51.506018,51.506005,51.505911,51.505871,51.505697,51.505537,51.50535,51.504589,51.504095,51.503961,51.503938]
y_geo = [51.503921,51.503574,51.503413,51.50328,51.50316,51.50312,51.502906,51.502799,51.502612,51.502398,51.502225,51.502198,51.502171,51.502412,51.502692,51.503213,51.503881,51.504535,51.505283,51.505617,51.505884,51.506232,51.506525,51.506806,51.506752,51.506592,51.506432,51.506272,51.506111,51.506018,51.506018,51.506031,51.506018,51.506005,51.505911,51.505871,51.505697,51.505537,51.50535,51.504589,51.504095,51.503961,51.503938]

loc = [(point[1], point[0]) for point in zip(x_geo, y_geo)]
lat = sum([point[0] for point in loc]) / len(loc)
lon = sum([point[1] for point in loc]) / len(loc)
#folium.PolyLine(loc, color='red', weight=2, opacity=0.8).add_to(m)

loc = [(point[1], point[0]) for point in zip(x, y)]
lat = sum([point[0] for point in loc]) / len(loc)
lon = sum([point[1] for point in loc]) / len(loc)
route = folium.PolyLine(loc, color='red', weight=3, opacity=0.7).add_to(m)

m.fit_bounds(route.get_bounds())

def get_participants_location():
    file = 'step_track.csv'
    headers = ['step_number','lon','lat']
    df = pd.read_csv(file,names=headers,header=None)
    return df

#st_data = st_folium(m, height=500,width=750)
# Function to render the map with pydeck

df_front = get_participants_location()
df_front = df_front.drop(df_front.index[0])
df_front['lat'] = pd.to_numeric(df_front['lat'],errors='coerce')
df_front['lon'] = pd.to_numeric(df_front['lon'],errors='coerce')
print(df_front)

conn = engine.connect()
sql_query = """
WITH RankedParticipants AS (
  SELECT
    participant_id,
    step_number,
    timestamp,
    ROW_NUMBER() OVER (PARTITION BY participant_id ORDER BY timestamp DESC) AS rn
  FROM
    participant_data
)
SELECT
  participant_id,
  step_number,
  timestamp
FROM
  RankedParticipants
WHERE
  rn = 1;
"""
df_db = pd.read_sql_query(sql_query, conn)
conn.close()
print(df_db)

merged_df = pd.merge(df_db, df_front[['step_number', 'lat', 'lon']], on='step_number', how='left')
print(merged_df.dtypes)
print(merged_df)

def load_icon_mapping(file_path):
    """Load the icon mapping from a JSON file."""
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_icon_mapping(mapping, file_path):
    """Save the icon mapping to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(mapping, file)

def assign_icons_to_participants(participants, icon_dir, base_url, mapping_file):
    """
    Assign icons to participants and update the mapping file.
    
    Args:
    - participants: List of participant IDs.
    - icon_dir: Directory where icons are stored.
    - base_url: Base URL where icons are accessible.
    - mapping_file: Path to the JSON file storing the mapping.
    """
    mapping = load_icon_mapping(mapping_file)
    available_icons = sorted(os.listdir(icon_dir))
    icon_index = len(mapping)  # Start from the next available icon index
    
    for participant in participants:
        if participant not in mapping:
            # Assign the next available icon to the new participant
            icon_file = available_icons[icon_index % len(available_icons)]
            icon_url = f"{base_url}/{icon_file}"
            mapping[participant] = icon_url
            icon_index += 1
    
    save_icon_mapping(mapping, mapping_file)
    return mapping

icon_dir = 'icons'  # Server directory where icons are stored
base_url = 'icons'  # URL to access icons
mapping_file = 'participant_icon_mapping.json'  # JSON file to store mapping
participants = merged_df.participant_id
icon_mapping = assign_icons_to_participants(participants, icon_dir, base_url, mapping_file)

marker_cluster = MarkerCluster().add_to(m)

for participant_id, step_number, lat, lon in zip(merged_df.participant_id, merged_df.step_number, merged_df.lat.values, merged_df.lon.values):
    for participant, icon_url in icon_mapping.items():
        if participant_id == participant:
            folium.Marker(
                location=(lat, lon),
                icon=folium.CustomIcon(icon_url, icon_size=(30, 30)),  # Removed color customization here; consider using a custom icon if needed.
                popup=f'{participant_id} at checkpoint:{step_number}',
                tooltip=f'{participant_id} at checkpoint:{step_number}'
            ).add_to(marker_cluster)

st_data = st_folium(m, 
#    feature_group_to_add=fg,
    height=800,
    width=1500,
)
leaderboard_df = merged_df[['participant_id','step_number']]
leaderboard_df.rename(columns={'step_number':'Current_Step'},inplace=True)
leaderboard_df.rename(columns={'participant_id':'Participant_ID'},inplace=True)
leaderboard_df['Total_Step_Count'] = '15'
st.dataframe(leaderboard_df)

if auto_refresh:
    time.sleep(number)
    st.rerun()
