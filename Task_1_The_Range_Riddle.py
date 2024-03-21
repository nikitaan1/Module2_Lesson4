import random

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for i in range(len(days_of_week)):
    days = days_of_week[i]
    mood = random.choice(moods)
    print(f"On {days} you were feeling {mood}")