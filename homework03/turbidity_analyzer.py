#Pranjal Adhikari pa8729

import json
import requests
import math

def current_water_turbidity(turb_data: dict) -> float:
    """
    Calculates the turbidity of the water, utilizing the 5 most recent measurements of the calibration constant
    and the ninety degree detector current. The values are then averaged to determine the water turbidity.

    Args: 
        turb_data (dict): water turbidity data

    Returns:
        turbidity (float): average water turbidity
    """
    i = len(turb_data['turbidity_data']) - 5
    t = 0
    while (i < (len(turb_data['turbidity_data']))):
        a0 = turb_data['turbidity_data'][i]['calibration_constant'] #calibration constant
        I90 = turb_data['turbidity_data'][i]['detector_current'] #ninety degree detector current
        t += a0 * I90 #calculating turbidity
        i += 1
    return t/5

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
    return math.log(ts/turb, 1-d)


def main():
    print("\n-----WATER TURBIDITY ANALYZER-----\n")
    turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turbidity = turbidity_data.json()
    water_turbidity = current_water_turbidity(turbidity)
    print("Current water turbidity (based on average of 5 recent measurements):", round(water_turbidity, 5), "NTU")
    ts = 1.0 #turbidity threshold
    if ts < water_turbidity:
        print("*UNSAFE WARNING* Turbidity is above the threshold for safe use")
        print("Minimum time required to return below a safe threshold:", round(time_required(water_turbidity), 2), "hours")
    else:
        print("*SAFE* Turbidity is below the threshold for safe use")
        print("Minimum time required to return below a safe threshold: 0 hours")

if __name__ == '__main__':
    main()