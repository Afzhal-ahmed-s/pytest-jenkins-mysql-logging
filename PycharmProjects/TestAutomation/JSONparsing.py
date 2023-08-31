import json

workout = '{ "day1" : "Push A", "day2" : "Pull A", "day3" : "Shoulders A", "day4" : "Leg A (Quadraceps)" }'

workoutInJsonFormat = json.loads(workout)
print(workout)
print(workoutInJsonFormat)