from google.cloud import pubsub_v1
import pandas as pd
from sqlalchemy import create_engine
from time import sleep
import json

project_id = "raves-altostrat"
topic_id = "ce_tech_day_leaderboard"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

def publish_message(participant_id, step_num, curr_time):
    data = json.dumps({
        'id': participant_id,
        'step_num': step_num,
        'curr_time': curr_time,
    })
    future = publisher.publish(topic_path, data.encode("utf-8"))
    print(f"Published {data} to {topic_path}: {future.result()}")

# Example usage
publish_message('participant_1','1','02-03-2024 12:00:00')
sleep(30)
publish_message('participant_2','1','02-03-2024 12:00:00')
sleep(30)
publish_message('participant_1','2','02-03-2024 12:30:00')
sleep(30)
publish_message('participant_3','2','02-03-2024 12:30:00')
sleep(30)
publish_message('participant_4','2','02-03-2024 12:30:00')
sleep(30)
publish_message('participant_1','3','02-03-2024 12:45:00')
sleep(30)
publish_message('participant_2','2','02-03-2024 12:30:00')
sleep(30)
publish_message('participant_1','1','02-03-2024 13:00:00')
sleep(30)
publish_message('participant_3','1','02-03-2024 13:00:00')
sleep(30)
publish_message('participant_2','4','02-03-2024 13:00:00')
sleep(30)
publish_message('participant_1','7','02-03-2024 14:00:00')
sleep(30)
publish_message('participant_1','11','02-03-2024 14:30:00')
sleep(30)
publish_message('participant_4','1','02-03-2024 14:30:00')
sleep(30)
publish_message('participant_1','12','02-03-2024 15:15:00')
sleep(30)
publish_message('participant_1','12','02-03-2024 15:15:00')
sleep(30)
publish_message('participant_2','13','02-03-2024 15:30:00')
sleep(30)
publish_message('participant_3','9','02-03-2024 15:15:00')
sleep(30)
publish_message('participant_1','14','02-03-2024 15:15:00')
sleep(30)
publish_message('participant_1','15','02-03-2024 16:00:00')


