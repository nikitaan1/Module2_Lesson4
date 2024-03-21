import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["Morning", "Afternoon", "Evening"]


for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
        print(F"On {day} {time} you were {mood}")