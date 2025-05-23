
prompt = """You are a research assistant. Your job is to read race reports from marathon runners, summarize them, and answer questions. Our goal is to better understand the way that runners train and what makes them successful.
        After you read the report, answer the following questions:
        1. What is the name of the race? 
        2. Is the race a marathon, half marathon, 10k, 5k, or some other distance?
        3. What is the age of the runner? Guess if you have to. Give a specific number, rounding to the nearest 5 years.
        4. Is the runner male or female? Guess if you have to. Indicate male, female, non-binary, or unknown.
        4. What training plan did they follow?
        5. What was their peak miles per week? Round to a specific number.
        6. What were the weather conditions like at their race?
        7. What was their main goal?
        8.Did they reach their main goal?
        8. If they had a secondary goal, what was it?
        9. Did they reach the secondary goal?
        10. Did they run any tune up races prior to the marathon? If so, what was the name of the race, the distance, and the time?
        11. How many marathons have they previously run?
        Format your answer in JSON.
        Here's sample mark-up:
        {
          "race_name": "Name of Race",
          "distance": "Marathon",
          "runner_age": 35,
          "runner_gender": "Male",
          "training_plan": "Jack Daniels 2Q",
          "peak_miles_per_week": "100-105",
          "weather_conditions": "Showery, but no wind. Runner does not believe the weather significantly affected their race, but acknowledges it may have contributed to quad soreness.",
          "main_goal": "Sub 2:25",
          "main_goal_reached": true,
          "secondary_goal": "Just finish",
          "secondary_goal_reached": true,
          "tune_up_races": [
            {
              "race_name": "Chester Marathon",
              "distance": "Marathon",
              "time": "2:28:42"
            }
          ],
          "previous_marathons_run": 4
        }
          """

report = """
London Marathon - No shade? no problem
Race Report
Race Information

Name: London Marathon

Date: 27th April

Distance: 26.2 miles

Location: London, England

Strava: https://strava.app.link/fitgao2ZYSb

Time: 2:23:28

Goals

Goal Description Completed?

A Sub 2:25 Yes

B Just finish Yes

C If I can’t finish then go out on my mouth guard Yes

Training

After running a 2:28:42 at Chester marathon 6 months earlier (and gliding along the entire time), I knew that more of the same training is all I needed to keep improving. I immediately jumped straight back into marathon training and spent a few months at around 90 MPW, before upping that to 100-105 MPW as I approached the back end of my marathon block. My training is fairly simple, an interval session, a tempo session, and a hard long run every week, and on the other 4 days easy mileage (yes I don’t have rest days, I’m currently on 3 years and 8 months of a run streak). Over the last 12 months transitioning my long run from slow and steady, to hard has been an absolute game changer. I make this long run session around 32-36km at 5-10% slower than target MP, so this meant each week I was doing a long run in the 3:35-3:45km range. On some occasions I did run it slightly faster than this, but I realised that it was affecting my runs for 2-3 days after too much so I dialled it back into that 5-10% sweet spot.

4 weeks before London on what turned out to be my last long run, I inadvertently injured myself in what I thought was a pinched nerve in my back. The following 3 weeks I struggled, convincing myself that it will pass, before I eventually swallowed my pride and went to a physio. I got an appointment 9 days before London and he told me that I have a tight gluteus medius and that it’s pressing against my sciatic nerve which is causing me issues in my back, hip, and hamstring. He managed to relieve some of the pressure, and then gave me some stretches to do to loosen it up more in the little time I have before the marathon, but most importantly he gave me the green light to go ahead with London. 2 days before the marathon I still couldn’t run without pain, I was lying in bed asking myself if I’m making a terrible mistake by travelling down to London and attempting this race, but I told myself to just go for it and if I can’t finish it then to do myself proud and run for as long as I can the only way I know how, by fully sending it.

Pre-race

I woke up at 6am feeling really positive and left the hotel at 6:45am due to needing to catch 2 underground tubes and then a train to Blackheath. Once I was there and in the championship starting area the only thing on my mind was whether to carry my phone or not during the race. I decided it was sensible to keep it on me incase I have to pull out and use public transport to get to the finish line (I’m unfamiliar with London and wasn’t comfortable potentially being 15 miles away from the finish line with no phone). I was trying to not think about my injury, so I just enjoyed the atmosphere and the sun and relaxed. I put 5 gels in my pocket and ate another as I waited at the start line and saw Alex Yee & the GOAT himself Kipchoge jog past (seeing him in the flesh was surreal).

Race

As we started I didn’t expect to be so penned in for as long as I was. I was trying to find any gaps possible to move up the field and increase the pace slightly but there was no safe way to do this, so the first km I went through in 3:28 which was slightly slower than target pace but I knew it was probably for the best. I passed the 5k mark in 16:39 which was 25 seconds faster than I had planned, but I wanted to make the most of the downhills and ‘bank’ time (risky gameplan that shouldn’t be recommended). 25 minutes in I had my first gel, and my plan was to continue having a gel every 25 minutes alternating between caffeine and non caffeine. I crossed the halfway mark in 1:11:34 and felt fantastic, I said to myself out loud that I have a minute in the bank now for that sub 2:25 goal and that I can do this. Around this point I passed Nick Bester which completely thrown me off, I had to do a double take to make sure it was him because I couldn’t comprehend how I was ahead of him. I kept plodding along at a nice constant pace sticking to my plan, feeling great and then the 35km mark hit. At this point my quads were on fire, did I hit the downhills in the first half too hard? I knew I wasn’t in survival mode quite yet so there was no need to panic, but I was definitely starting to work out how long I had remaining. Once I looked at my watch and saw that I had been running for 2 hours 10 minutes I said to myself that the last 6 months of training have all been for this 15 minute block right now, this is why you put in the hard work every single day. It felt like I was slowing down but my average pace on my watch was remaining the same so I knew that the wheels hadn’t fell off quite yet. As I made that final turn and could see the finish line I knew that I could potentially get sub 2:24 and gave it one last push. As it turns out I had plenty of time in the bank, but as you know when you’re running hard your brain just doesn’t work how it should. I crossed that line in 2:23:28, and from 15km to the end I clocked every 5km split with an average pace of 3:23km according to the marathon app, so I paced it pretty much perfectly.

Post-race

My mum and sister had travelled down to London to meet me at the finish line, and we agreed to meet at the letter ‘S’ in the meet and greet area. The issue I was having though was where was ‘S’? Not because it wasn’t clearly marked out, but because there was a massive sign stating ‘P to Z this way’ and my brain was that fried I couldn’t figure out if S came after P in the alphabet (marathon brain fog ey). A woman interviewed me asking if I wanted a pair of crocs which confused me further but I swiftly refused and eventually found the ‘S’ station and met my family. Then it was a quick uber back to the hotel, shower, and then out for drinks and food and to watch Liverpool win the league!!! What an amazing day

I haven’t really touched on the weather throughout this, even though it has been a major talking point. If I’m being honest I don’t think it really affected me, I felt good in that regard throughout. I just made sure to take on more fluids than I usually would, and I ran wide at times to run through the showers (each time they were an amazing 0.5 seconds). Maybe potentially it affected me more than I think, and I’ve heard people saying it’s the reason why everyone’s quads including mine were trashed (from needing to work harder earlier on), but honestly I don’t think I could have ran much quicker at all so I’m not going to talk badly about the weather. I’m just grateful there was no wind to battle against.

My body and particularly my quads are still absolutely destroyed, but I’m looking forward to jumping straight back into an other marathon cycle and working towards that sub 2:20 barrier

Made with a new race report generator created by u/herumph."""


import requests
import json

apikey = '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'

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {apikey}",
    "Content-Type": "application/json",
    # "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    # "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "google/gemma-3-27b-it:free",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": prompt
          },
          {
            "type": "text",
            "text": report
          }
        ]
      }
    ],
    
  })
)

print(response.json()['choices'][0]['message']['content'].strip()[7:-3])
data = json.loads(response.json()['choices'][0]['message']['content'].strip()[7:-3])
print(data)
