from google.cloud import pubsub_v1
import pandas as pd
from sqlalchemy import create_engine
from time import sleep
import time
import json

# Database connection setup
db_user = 'postgres'
db_pass = 'ravish'
db_name = 'users'
db_host = '34.87.40.107'
db_port = '5435'
# PostgreSQL connection string
database_url = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = create_engine(database_url)

project_id = "raves-altostrat"
subscription_id = "ce_tech_day_leaderboard-sub"
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

def callback(message):
    print(f"Received message: {message}")
    data = message.data.decode("utf-8")
    data_dict = json.loads(data)
    timestamp_str = data_dict["curr_time"]
    timestamp = pd.to_datetime(timestamp_str, format='%d-%m-%Y %H:%M:%S')
    participant_id = data_dict['id']
    value = data_dict['step_num']
    df = pd.DataFrame({
        'participant_id': [participant_id],
        'step_number': [value],
        'timestamp': [timestamp]
    })
    print(df)
    df.to_sql('participant_data', con=engine, if_exists='append', index=False, schema='public')
    message.ack()

print("Listening for new messages on {}...".format(subscription_path))
streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

try:
    streaming_pull_future.result()
except KeyboardInterrupt:
    streaming_pull_future.cancel()  # Trigger the shutdown
    streaming_pull_future.result()  # Block until the shutdown is complete
