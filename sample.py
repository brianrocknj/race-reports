import requests
import json

key = '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'

text = []

text.append("""
Race Report: Sometimes, you need to make mistakes for yourself
Race Report
Race Information
Name: Great Welsh Marathon

Date: March 16th, 2025

Distance: 26.2 miles

Location: South Wales, UK

Website: https://www.greatwelshmarathon.co.uk/

Time: 3:35:55

Goals
Goal	Description	Completed?
A	Sub 3:15	No
B	Negative split	No
C	Enjoy myself	No
Splits
Kilometer	Time
1	4:39
2	4:34
3	4:32
4	4:22
5	4:30
6	4:35
7	4:38
8	4:33
9	4:29
10	4:36
11	4:33
12	4:34
13	4:33
14	4:34
15	4:35
16	4:35
17	4:31
18	4:39
19	4:37
20	4:37
21	4:35
22	4:35
23	4:30
24	4:35
25	4:30
26	4:34
27	4:50
28	4:57
29	5:12
30	5:12
31	5:17
32	5:27
33	5:26
34	7:37
35	7:56
36	5:53
37	6:29
38	5:36
39	6:05
40	6:57
41	6:19
42	5:45
Training
Before signing up for this race, I had been an on-again, off-again runner for three years. In 2023, I ran the Cheltenham Half in 1:41 after a three month, entirely freestyled, unstructured training plan that essentially consisted of running whenever I fancied. Since that, my running was the odd 10k in what you might call "zone 3" - AKA as fast I could maintain for the distance.

I started running Parkruns with in summer 2024 and my love of running was truly ignited. I built up to 30-40km per week, and got my 5k time down from 23 to 20 mins by around September. At this point, one of my friends ran a marathon, and I decided it was time to face it myself.

I signed up for this marathon in October - a good five/six months in advance. My training started with five weeks or so on a Runna plan, before I decided it was too expensive and that I knew enough to design my own plan instead and save the money.

An important piece of context is that I have always, always, always hated going to the gym. One of the reasons I started running was because it seemed like a form of exercise where I could be competitive, and not be penalised because of my, *ahem*, slight build. Rather, I would have an advantage since I wouldn't be lugging extra weight around!

I have also never historically struggled with injury, and, despite the overwhelming advice I was seeing online, convinced myself that I could get away without strength training. You can probably see where this is going by now.

Throughout the block, I had various niggles - shin splints, ankle pain, hip tightness - all of which I managed. I felt comfortable that they were not anything serious, and all faded away in turn. This probably contributed further to my overconfidence.

After four months of training well, gradually building up to c. 60km/week by early February, I raced a half marathon in Cardiff as a tune up race. I set out at my 3:15 marathon goal pace, and felt so good after 15km that I sped right up and finished in just over 1:31. In hindsight, that day was probably when I peaked.

A week or two later, I started feeling a rubbing and clicking sensation in my right knee during easy runs. The next day, I had a bit of grief when walking down the office staircase. I thought nothing of it.

Then, I headed out on a hill sprint session. SNAP!

My knee was in serious pain. I hobbled home and started googling, before self-diagnosing with ITBS. Dang.

It was three weeks until race day, and I quickly realised that I was in serious danger of DNSing. I did my best to rest and rehabilitate, before trying my luck with some run-walk, easy jogs about a week before race day to see how it felt. The pain was there, but it was mild. The rest of the week, I vacillated back and forth between racing or pulling out.

Come race weekend, the weather was so stunning, I decided to travel to the race, rationalising that I could always just have a nice weekend in the South of Wales if I couldn't run. Before I knew it, I was at the start line.

Pre-race
I had the Reddit-recommended 6am-bagel-with-peanut-butter-and-banana breakfast. I then realised that I had forgotten the lid / sealer thingy for my hydration bladder, which I had already filled with an electrolyte/maltodextrin combination and was planning to sip during the race. After a few minutes of panic, I decided to try and "close" the bladder using safety pins that had arrived in my race pack. This... did not work.

I then made my way to the start line.

Race
I had a long time to wait in the corral, since there was a fifteen minute delay due to traffic congestion. I knew I wanted to go with a pace group, and there was a 3:15 pacer standing there, tempting me. 3:15 was my goal pace, but I had reservations about going slower to help manage the knee pain. Eventually, I decided to go with 3:15.

Almost immediately after the gun, the knee pain made itself known. It was mild, and I knew that I could deal with this if it did not get any worse. A big if.

Well, for the first 21k, the knee was not my biggest problem. My hydration bladder was leaking constantly down my back and onto my race shorts. This was no big deal until it started evaporating in the Welsh sunshine, leaving a sticky, salty residue on my legs back and shorts. My legs were adhering to my shorts, and it was far from comfortable to unstick them every few kilometers. At least it kept my mind off my knee, and I was feeling comfortable. The pace felt OK. My heart rate, according to my Garmin at least, disagreed, and I was hovering around 190bpm. My max is 205, and I would consider 190 fairly sustainable, but not for an entire marathon. I decided that my watch was probably wrong and I should just carry on. Probably unwise.

The 25k mark was the turnaround point, both figuratively and literally. As I went round the 180 degree turn, my knee became fed up of not being the centre of attention, and sent me a massive jolt of pain. At this point, I was literally as far away from the start/finish line, where my bag was dropped, as could be. I would need to get back anyway, so I was pretty motivated to do it as part of the race, rather than trying to find a taxi or bus in rural Wales on a Sunday.

I hobbled back the last 17k to the finish. Some walking, some jogging - a lot of pain. Definitely unwise. Definitely uncomfortable.

When I eventually crossed the finish line in 3:35, it was not the heroic sprint over the finish I had dreamt about. It felt awful. I felt like a fool.

Post-race
Reflecting a few days later, there is some pride in the emotional mixture. I am pleased to have finished my first marathon, and have definitely learnt a lot about strength training, managing injury, preparing properly, and respecting the marathon.

The frustrating thing is that I had been warned about all of these things. From the good people of r/AdvancedRunning, to name one source. But I had let my arrogance convince myself that I knew better, that I could get away without strength training, that I could run a 3:15 first marathon with a knee injury after three weeks of no running.

I guess sometimes, you need to make mistakes for yourself.

Made with a new race report generator created by u/herumph.""")

text.append("""
Atlanta Marathon Race Report - My First Marathon
Race Report
Race Information
Name: Atlanta Marathon

Date: March 2, 2025

Distance: 26.2 miles

Location: Atlanta, GA

Website: https://www.atlantatrackclub.org/

Strava: https://www.strava.com/activities/13770407473

Time: 3:25:09

Goals
Goal	Description	Completed?
A	Finish	Yes
B	Sub 4	Yes
C	Sub 3:30	Yes
Splits
Mile	Time
1	8:02
2	7:41
3	7:30
4	7:28
5	7:33
6	7:28
7	7:08
8	7:15
9	7:37
10	7:12
11	7:33
12	7:32
13	7:19
14	7:41
15	7:38
16	7:36
17	7:28
18	7:45
19	7:42
20	7:56
21	7:58
22	8:10
23	8:27
24	8:39
25	10:07
26	9:02
27	2:49
Training
I started running somewhat regularly back in August of 2022, however at that time I was not particularly committed (or addicted, I should say), so I typically just ran 8 to 12 miles a week. From August '22 all the way until September of '23, I never once exceeded 15 miles in a week.

That marked a change in my attitude as I tried to consistently hit higher mileage after that. I started to prioritize exercising more and more, so from September 2023 until February of 2024, my weekly mileage oscillated between 19 to 32 miles a week (although I only hit 30+ twice during this time period)

By April of 2024 I had managed to start hitting 40 miles a week regularly. At this point my training became much more intentional - although perhaps not as effective as it could have been. I tried to incorporate weekly long runs as well as the occasional tempo or threshold run.

Unfortunately that lasted all of... 1 month. I dropped my mileage a ton during May 2024 and ended up getting a lingering hip injury that kept me from running almost the entire summer following.

At this point, I got pretty into Peloton, and started to regularly incorporate Peloton Power Zone classes into my weekly routine. Additionally, due to my schedule I have extra free-time in the Summer, so I started doing "doubles" with cross training (e.g 1 hour of treadmill, 1 hour biking).

I relied on RPE and heart rate to guide my efforts cross training - my primary focus was to maintain my fitness as much as possible. Fortunately, through extensive use of the Erg machine (rowing), the Elliptical, and in the Peloton, as well as the occasional aqua jog. I was able to generally manage 2 to 3 hours of exercise a day all Summer 2024.

It's worth mentioning that the only reason I had even started to get serious about exercise (running, before getting injured) was simply because I set the arbitrary goal to run a marathon on/near my 26th birthday (Late November). That may explain the sudden increase in intensity, consistency, and weekly mileage.

Anyway, I maintained consistent cross training as part of my regular routine from this point forward; even when returning to regular running (finally hitting 40 miles a week consistently again in late September '24). I did more research on actual plans and what sort of workouts to try and incorporate into my training. I took away lots of valuable information... and put into practice a small fraction of it.

Since October of '24, though more motivated, I was still not able to maintain 40+ miles a week for more than a month before needing to drop mileage substantially for a couple weeks at a time (although I was doing a SUBSTANTIAL amount of volume cross training to compensate) Suffice to say, I did not feel prepared for a marathon before the end of 2024. Knowing that I was "failing" my goal left me dealing with disappointment (and a non-insignificant amount of frustration) but came to terms with the fact that all the pressure I was experiencing was entirely placed upon myself; that running a marathon at a specific date or time was entirely arbitrary, and that I could simply... take more time to prepare before running. This prompted me to sign up for the Atlanta Marathon of this year.

Following this, I resolved to be consistent, even if it meant pushing through pains and discomforts that I would typically just let subside before resuming regular training (obviously not medical advice, please don't just read this and assume that's a good or smart decision - it's just all about knowing your body at the end of the day; I'm inclined to playing it safe, but there's lots more interesting conversation that could be had on this topic alone).

I ran the Polar Opposite Peachtree 10k January 2nd here in ATL. Initially, it was just intended as a tune-up workout, however I ended up running my 1 mile (6:07), 5k (19:46), and 10k (43:00) pb during the race. I felt pretty satisfied that I could perform well on a particularly hilly course. This deepened my resolve to train hard for the marathon (about 2 months away, at that point).

That more or less brings us to the race today - that being said, I will mention 3 things:

though my weekly mileage was low, I generally did about 8 to 12 hours of cardio a week - including the time spent running

I almost always did a long run each week - and averaged between 12 and 16 miles. I did manage to hit 20 miles one time (late January).

the area I run in is very hilly (in my opinion, at least - it's metro ATL, so I suppose it's all relative..)

I felt somewhat confident that I would be able to complete a marathon after that 20 mile long run (took about 2:44:00 to do) - but my lack of consistent high mileage, combined with having never practiced fueling or hydration during a run, I was certainly anxious the entire month of February as the marathon approached at an alarming pace.

I'll leave my "training" section there for now - I'm (all too) happy to further elaborate on more details if anyone is curious, though!

Pre-race
I planned to get up a few hours before the race started so I could just get the blood flowing and get some food. I ate a plain bagel with peanut butter and honey, and like one clementine. Got ready and headed over to the race. An hour before the race I ate a banana.

After that I just moseyed my way on over the starting area and waited in the cold (just had a very thin singlet and janji half tights on, + gloves).

As for a plan... I really just didn't know what to expect. I mainly did not want to absolutely hit the wall and bonk and need to walk the last 10k. Beyond that... I just figured I'd feel it out as I went, although internally, I suspected somewhere around 8:00/mile on the fast side and 9:00 on the slower side would be the pace for me to settle into.

Race
It was a cold day, but overall perfect weather for running. I was really only uncomfortable while waiting to start.

As we got going I felt pretty strong. I pretty much just started off at a pace that felt good and maybe perhaps possibly get a little carried away, as I covered the first 13.1 miles in 1:37:39. The logical side of me knew that this was too fast for a mull marathon, but I kinda decided to just not care and see how my body would handle that pace. After all, I felt strong and in control, so why not just send it?

This seemed like a prudent decision at the time... it was not. I don't know if I hit the "wall" exactly per se, as my cardio never felt particularly taxed, but my LEGS... entirely different story.

The race had 1500ft of elevation gain. Although there were hills pretty much the entire course, the first 8 miles were a net downhill. The rest of the course, however, was uphill with Atlanta's characteristic uncomfortably long gradual hills peppering pretty much each mile the whole way. No, I am totally not jealous of those who run in flatter areas, thanks for asking.

Anyways, I pretty much kept up this "uptempo" pace for the first 22 miles. By that point... my legs hurt more than I ever could have imagined. I also needed to pee pretty much the entire race - so there's that.

I did manage to get a few sips of Powerade and water throughout the race, but I didn't take any nutrition in terms of food or gels or candy, etc. etc.

Miles 22 through 24 were painful, but somehow manageable? I deluded myself into thinking that it wasn't really possible to hurt more than I did at that moment. This led me to a sort of zen acceptance of the pain I was in.

Unfortunately, this was a short lived enlightenment. By mile 25 all that pain made me slow to the point of essentially walking several times. I figured that if I could just make it to mile 25 that I would be able to finish strong.

That was... somewhat true, in hindsight. Although my last mile really did not feel like anything approaching my understanding of the word "strong"

I ended up crossing the line in 3:25:28. However, I guess the course may have been a bit longer than that - as my watch/strava recorded my finishing time to be 2:25:09.

Some "data" for all those that it may interest:

My heart-rate was low (about 150 bpm for the first few miles, but got up to 160 after that and it stayed between 160 to 165 the whole race, although I did briefly peak at 174 after one particular hill, towards the end of the race it went down again as my pace decreased drastically over the last 3 miles).

cadence averaged 187 spm - pretty consistent throughout the entire race

stride was 1.09m long, however it was about 1.12 until 22 miles, my stride started to shorten and become very inconsistent after that)

Ground contact time: 235ms; not entirely sure if this actually matters, however like everything else, I was much more efficient over the first 22 miles

Post-race
I immediately found the restroom. MY legs hurt and I walked with the confidence of an uncertain toddler. It was not a pretty site to see. To be honest I didn't feel the wave of strong emotions that I know some experience upon finish a marathon. It kinda just came and went. Honestly, if anything I'm glad it's over - I predict miles 24 - 26 will be in my legs all the rest of this week.

I'm uncertain if I want to continue to try training for marathons and get a fast time in on a flatter course or if maybe I just should focus on shorter distances. I definitely enjoy the 10k and half marathon distance more - I'm open to any advice, suggestions, feedback, or even opinions, while we're at it.

If you made it this far, thank you! This was as much a meditation for myself as a way to engage with the community - although I would truly appreciate any feedback or advice as towards what distance I should focus going forward and better ways to train.""")

text.append("""Wilmington Marathon Race Report
Race Report
Race Information
Name: Wilmington Marathon

Date: February 22, 2025

Distance: 26.2 miles

Location: Wilmington, NC

Website: https://wilmingtonncmarathon.com/

Time: 2:56

Goals
Goal	Description	Completed?
A	Sub 3	Yes
B	3:05	Yes
C	3:10	Yes
Splits
Mile	Time
1	7:02
2	6:51
3	6:37
4	6:58
5	6:49
6	6:48
7	6:50
8	6:57
9	6:50
10	6:53
11	6:55
12	6:57
13	6:46
14	6:50
15	6:46
16	6:42
17	6:54
18	6:49
19	6:36
20	6:27
21	7:19
22	6:41
23	6:44
24	6:46
25	6:49
26	6:28
Training
Ever since I got back into running during COVID, I've used the service/app TrainAsOne for my training planner. I basically uploaded a previous year of runs to it, told it my goal time and race day, and it lays out a plan to (hopefully) get you there. I had previously run a 3:05 marathon, and I was diehard to finish sub-3. I ran the Charlotte marathon in November and had a disappointing 3:18 finish after hitting the wall at around 17 miles. In reflecting why, I realized that I wasn't taking nutrition seriously enough and I simply ran out of fuel during the race. I was taking the same small number of gels during the race as I always had, but my pace was much faster so it simply wasn't enough. I'm probably lucky I didn't get injured based on how I was treating my body.

In any case, I educated myself on proper performance nutrition (I binged the 'Fuel for the Sole' podcast while running), and it made a HUGE difference in my speed. I fueled with Maurten gels, bought a Flip Belt to hold them all on my long runs, started managing my carb and protein intake, got my sweat tested via Levelen to see how much water/sodium I should be consuming, started taking Momentous protein powder after runs for recovery, and adjusted my eating habits. I gained a few pounds, but my runs got faster, easier, and I was less sore. I crushed through the last of my training, and felt pretty well through peak week, and was theoretically well prepared for a sub-3 finish. The 3 weeks before the taper each had about 60 miles in them, of various amount of speed work. My longest run was 20 miles.

Taper week was especially rough this time around. I felt bad the whole week, and it really took a toll on my confidence. I read in this subreddit that it's totally normal to feel this way, but man was it rough. Every little tweak made me worried, and I felt lazy and restless. TrainAsOne had me doing some sprint work during the taper, but I ignored it to prevent any injuries so close to the race. I made sure I got tons of sleep.

3 days before race day I carb loaded. I had 500g of carbs a day using "safe" foods that I knew my stomach could handle. It was a bit of a chore eating that much, but it really helped.

Pre-race
The Wilmington marathon is point-to-point starting at 7am, so I got a VRBO right near the starting line. I ate at bagel at 5am and a sports drink at 5:30 (Skratch). I geared up and was at the race start at 6:40. I took a 160 Maurten gel a few mins prior to the race, took a few pre-race photos, and began the race at 7.

Race
The Wilmington marathon is flat and fast. A cold front came in the day before, so it was a perfect 30 degrees at the start with the sun coming up. Even though my training pace was sub-3, I wanted to ensure that I didn't flame out too early so I ran the first 11 miles or so with the 1:30 half marathon pacers. At one point the course became narrow, so I took off in front of them and didn't see them again. I started slowly tapping the gas as I went, and kept it pretty consistent until around 18 miles. At that point I stopped listening to podcasts and switched to my running music, and ditched my water bottle. That was a big confidence boost, since I now felt lighter without my bottle and the music got me pumped up. I had diligently been taking Maurten gels every 30 mins, so I felt no inklings of hitting the wall, which was also a confident booster. I started speeding up and began a long series of passing other runners. I remember how absolutely dead I felt at the 18 mile mark just a few months ago, and it's crazy how much better I felt. I had tons of energy still, and was even air drumming at a few points, much to the amusement of the runners that had already made the turnaround and were running back my way.

I continued chasing down other runners for the last 6 miles, and had a really strong feeling that this was the race where I was finally going to break 3 hours. I gave it all I had the last mile and finished with a very pleasing 2:56! I never thought I'd be able to accomplish a time like that, but I did it. It was a 10 minute PR! Huzzah!

Post-race
Post race, I felt shockingly well. I was exhausted to be sure, but nothing like previous races. I was only mildly sore, and felt that I may have left some time on the race course. Maybe I should have started sprinting sooner? In any case, I felt surprisingly well and was in high spirits. Lots of pics afterwards and congrats from my ever supportive wife and family. Turns out I placed 3rd in my division and won some cash :)

Within 3 months, I went from a 3:18 to a 2:56 and felt fantastic. I attribute the majority of that improvement to my focus on nutrition and properly fueling for my training and race day. Other factors like weather, hilliness, and improved fitness played a role for sure, but I think the majority was due to my nutrition changes.

Thanks for reading. Keep on running!

Made with a new race report generator created by u/herumph.
""")

data = {
    "model": "deepseek/deepseek-chat-v3-0324:free",
    "messages": [
      {
        "role": "user",
        "content": "Read the following text and summarize it. Include a table that clearly identifies the race, the runner's gender, their age, the training plan they used, their peak weekly mileage, their finish time, and whether they met their goals."
      }
    ],
    
  }

for i in range(0,3):
    data['messages'][0]['content'] = f"Read the following text and summarize it. Include a table that clearly identifies the race, the runner's gender, their age, the training plan they used, their finish time, and whether they met their goals. {text[i]}"
    r = requests.post(
        url='https://openrouter.ai/api/v1/chat/completions',
        headers={
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        },
        data=json.dumps(data)
    )

    response = r.json()
    # print(response)
    choice = response['choices'][0]['message']['content']
    print(choice)


