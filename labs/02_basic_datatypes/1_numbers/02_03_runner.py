'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

seconds_in_hour = 60*60
runner_seconds = (30*60)+30
average_speed_mph = 10*seconds_in_hour/runner_seconds
average_speed_kph = average_speed_mph*1.6

print(average_speed_kph)
