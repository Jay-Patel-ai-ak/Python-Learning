# 6. Weather Transportation Suggestion
#Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car)

distance = 10  # in miles

if distance < 3:
    transportation = "Walk"
elif distance < 15:
    transportation = "Bike"
elif distance > 15:
    transportation = "Car"
else:
    transportation = "Plane"
    
print(f"For a distance of {distance} miles, you should: {transportation}")