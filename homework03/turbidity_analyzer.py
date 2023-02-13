#Pranjal Adhikari pa8729

import json
import requests
import math

def current_water_turbidity(a0: float, I90: float) -> float:
    """
    Calculates the turbidity of the water, given calibration constant and the ninety degree detector current.

    Args: 
        a0 (float): calibration constant
        I90 (float): ninety degree detector current

    Returns:
        turbidity (float): average water turbidity
    """
    return a0*I90 #equation to calculate turbidity

def time_required(turb: float) -> float:
    """
    Given the turbidity of the water, calculates the minimum time (in hours) required to reach the threshold for the water
    to be safe. The equation used to caluclate the time is the standard exponential decay function.

    Args:
        turb (float): value of the turbidity of water
    Returns:
        minimum time (float): time required to reach threshold
    """
    ts = 1.0 #turbidity threshold for safe water
    d = .02  #decay factor per hour
    return math.log(ts/turb, 1-d) #standard exponential decay formula


def main():
    print("\n-----WATER TURBIDITY ANALYZER-----\n")
    turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json') #retrieving water data from the given url
    i = len(turbidity_data.json()['turbidity_data']) - 5 #starting from the 5th most recent measurement
    water_turbidity = 0
    while (i < (len(turbidity_data.json()['turbidity_data']))): #iterating from the 5th to the most recent measurement
        a0 = turbidity_data.json()['turbidity_data'][i]['calibration_constant'] #calibration constant
        I90 = turbidity_data.json()['turbidity_data'][i]['detector_current'] #ninety degree detector current
        water_turbidity += current_water_turbidity(a0, I90)
        i += 1
    water_turbidity = water_turbidity/5 #average of the 5 most recent measurements
    print("Current water turbidity (based on average of 5 recent measurements):", round(water_turbidity, 5), "NTU")
    ts = 1.0 #turbidity threshold
    if ts < water_turbidity: #below the threshold
        print("*UNSAFE WARNING* Turbidity is above the threshold for safe use")
        print("Minimum time required to return below a safe threshold:", round(time_required(water_turbidity), 2), "hours")
    else: #above the threshold
        print("*SAFE* Turbidity is below the threshold for safe use")
        print("Minimum time required to return below a safe threshold: 0 hours")

if __name__ == '__main__':
    main()