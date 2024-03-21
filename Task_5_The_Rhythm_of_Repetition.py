#Task1

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    track_number = i + 1
    print(f"Track {track_number}: Genre is {genres[i]}")


#Task2

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

track_number = 1
i = 0

while i < len(genres) and genres[i] != "Hip-hop":
    print(f"Track {track_number}: Genre is {genres[i]}")
    i += 1
    track_number += 1


#Task 3
    
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    track_number = i + 1
    
    if genres[i] == 'Classical':
        print(f"Track {track_number}: {genres[i]} genre is not suitable for the light show.")
        continue  
    
    print(f"Track {track_number}: Light show is ready for {genres[i]}")

