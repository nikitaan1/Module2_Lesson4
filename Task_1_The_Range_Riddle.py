import random

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["Happy", "Sad", "Energetic", "Calm"]

for days in days_of_week:
    mood = random.choice(moods)
    print(f"On {days} you were feeling {mood}")