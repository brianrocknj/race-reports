import requests
import json
import os
import pandas as pd
import time
from google import genai

prompt = """You are a research assistant. Your job is to read race reports from marathon runners, summarize them, and answer questions. Our goal is to better understand the way that runners train and what makes them successful.
        After you read the report, answer the following questions:
        1. What is the name of the race? 
        2. Is the race a marathon, half marathon, 10k, 5k, or some other distance?
        3. What is the age of the runner? Guess if you have to. Give a specific number, rounding to the nearest 5 years.
        4. Is the runner male or female? Guess if you have to. Indicate male, female, non-binary, or unknown.
        4. What training plan did they follow? Jack Daniels 2Q, Pfitz 18 Week, Pfitz 12 Week, Hanson, Hal Higdon, or Other.
        4a. Important details about their training plan.
        5. What was their peak miles per week? Round to a specific number.
        6. What were the weather conditions like at their race?
        7. What was their finish time in the race?
        8. What was their main goal?
        8a.Did they reach their main goal?
        9. If they had a secondary goal, what was it?
        9a. Did they reach the secondary goal?
        10. Did they run any tune up races prior to the marathon? If so, what was the name of the race, the distance, and the time? Only include the most successful tuneup race.
        11. How many marathons have they previously run?
        12. Did they sustain injuries or have other similar problems during their training?
        Format your answer in JSON.
        Here's sample mark-up:
        {
          "race_name": "Name of Race",
          "distance": "Marathon",
          "runner_age": 35,
          "runner_gender": "Male",
          "training_plan": "Jack Daniels 2Q",
          "training_plan_details": "Modified with extra mileage.",
          "peak_miles_per_week": "100-105",
          "weather_conditions": "Showery, but no wind. Runner does not believe the weather significantly affected their race, but acknowledges it may have contributed to quad soreness.",
          "finish_time" : "2:57:39",
          "main_goal": "Sub 2:25",
          "main_goal_reached": true,
          "secondary_goal": "Just finish",
          "secondary_goal_reached": true,
          "tune_up_race: "Chester Marathon",
          "tune_up_distance": "Marathon",
          "tune_up_time": "2:28:42",
          "previous_marathons_run": 4,
          "problems": "No problems."
        }
          """

# apikey = os.environ['OPENROUTER_APIKEY']
api_key = os.environ['GEMINI_API_KEY']
client = genai.Client(api_key=api_key)
model = 'gemma-3-27b-it'
reports = pd.read_csv('Reports.csv')
reports = reports[reports['text'].notna()]
# reports = reports.sample(3)


for i, report in reports.iterrows():
  details = pd.read_csv('Details.csv')

  if report['id'] in details['id'].values:
    print(f"Already summarized this race report ({report['id']}). Skipping.")
    continue

  response = client.models.generate_content(
    model=model,
    contents=prompt + ' - ' + report['text']
  )

  # print(response.text)
  
  try:
    data = json.loads(response.text.strip()[7:-3])
    data = pd.DataFrame([data])
    data.insert(0, 'id', [report['id']])
  except:
    print(f'There was an error with {report['id']}.')
    print(response.text)
  else:
    if len(data) == 0:
      print(response)
    else:
      print(data.T)
      # print(data[['race_name', 'distance', 'runner_age', 'runner_gender', 'finish_time', 'main_goal_reached', 'weather_conditions', 'problems']])
    data.to_csv('Details.csv', mode='a', header=False, index=False)

  time.sleep(8)
