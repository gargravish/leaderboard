# Prerequisites

### Python 3.7 or later
### Required Python Libraries: The following libraries are needed and can be installed using pip:
```
streamlit
pandas
numpy
google-cloud-pubsub
psycopg2 (if using PostgreSQL)
sqlalchemy
pydeck
folium
shapely
json
```

Create a Google Cloud Project: https://cloud.google.com/resource-manager/docs/creating-managing-projects

Enable the necessary APIs (Pub/Sub, postgres)

Set up service account credentials with appropriate permissions

Install and set up a CloudSQL  database instance: 

Create credentials for database access

Create a pubsub topic

## Project Structure

**leaderboard.py:** Contains the core Streamlit code for displaying the leaderboard and map.

**listen_data.py:** Subscribes to a Google Cloud Pub/Sub topic (or an alternative data source) to receive real-time updates on participant locations or step counts.

**publish_data.py (Optional):** A script for simulating/publishing participant data to the Pub/Sub topic for testing.

**step_track.csv:** A sample CSV file with pre-defined route coordinates.

## Setup

Install Python libraries:

```
pip install streamlit pandas numpy google-cloud-pubsub psycopg2 sqlalchemy pydeck folium shapely json
```
Use code with caution.

Replace database credentials:

Modify the database connection string in leaderboard.py and listen_data.py with your PostgreSQL database credentials (if using).

Set up Google Cloud credentials:

Obtain Google Cloud service account credentials as a JSON file.

Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of this JSON file. 

## Running the Demo

### Start the listener script:


```
python listen_data.py
```
Use code with caution.

This will start listening for new data from your chosen data source (e.g., Google Cloud Pub/Sub).

Start the Streamlit app:


```
streamlit run leaderboard.py
```
Use code with caution.

This will launch the leaderboard UI in your web browser, typically at http://localhost:8501.

Optional: Simulate Data


```
python publish_data.py
```
Use code with caution.

This will publish simulated participant data if you don't have a live data source yet.

## Customization

### Map Customization: 

Change the starting coordinates, zoom level, and map style within the folium code in leaderboard.py.

Route: Edit the step_track.csv file to modify the predefined route.
