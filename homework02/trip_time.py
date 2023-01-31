#Pranjal Adhikari pa8729

import json
import math

with open ('random_sites.json', 'r') as s: #utilizing the randomly generated data of the sites in 
    sites_d = json.load(s)

print("\n-----ROBOT SITES VISIT SUMMARY-----\n")

lat1 = 16.0 #initial coordinates of the robot (starting location)
lon1 = 82.0
max_speed = 10 #used to determine the time it takes for the robot to travel a given distance
mars_radius = 3389.5

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float: #calculate the distance between coordinates (lat1, lon1) and (lat2, lon2) on Mars
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

total_travel_time = 0
for i in range (len(sites_d['sites'])): #iterating (or traveling) through the 5 generated sites from the starting point of (lat1, lon1)
    lat2 = sites_d['sites'][i]['latitude']
    lon2 = sites_d['sites'][i]['longitude']
    
    time_to_site = calc_gcd(lat1, lon1, lat2, lon2) / max_speed #calculating the time taken by the robot to get to the site, from the prior site (or starting location)
    total_travel_time += time_to_site #adding the travel time to the site, to the total time of the sites investigation

    print("Leg", i+1, ":   time to travel =", round(time_to_site, 2), "hr,", end = " ")

    if sites_d['sites'][i]['meteorite composition'] == 'stony-iron': #stony-iron sample time
        total_travel_time += 3
        print("time to sample =", "3 hr")

    elif sites_d['sites'][i]['meteorite composition'] == 'iron': #iron sample time
        total_travel_time += 2
        print("time to sample =", "2 hr")

    else: #stony sample time
        total_travel_time += 1
        print("time to sample =", "1 hr")

    lat1 = lat2 #setting the new starting location of the robot, after it has reached a site and collected the respective sample
    lon1 = lon2

print("----------------------------------------------------------")
print("Number of legs =", len(sites_d['sites']), ", total travel time =", round(total_travel_time, 2), "hr") #printing the total time it takes for the investigation of the 5 sites to occur
print("----------------------------------------------------------")