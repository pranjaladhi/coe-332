#Pranjal Adhikari pa8729

import json
import requests
import math

turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
turbidity = turbidity_data.json()

def current_water_turbidity():
    i = len(turbidity['turbidity_data']) - 5
    t = 0
    while (i < (len(turbidity['turbidity_data']))):
        a0 = turbidity['turbidity_data'][i]['calibration_constant']
        I90 = turbidity['turbidity_data'][i]['detector_current']
        t += a0 * I90 # calculating turbidity
        i += 1
    return t/5

def time_required(t0):
    ts = 1.0
    d = .02
    return ts/(t0*(1-d))

def if_water_safe(turb):
    ts = 1.0
    if ts > turb:
        print("*UNSAFE WARNING* Turbidity is above the threshold for safe use")
        print("Minimum time required to return below a safe threshold:", round(time_required(turb), 2), "hours")
    else:
        print("*SAFE* Turbidity is below the threshold for safe use")


def main():
    print("\n-----WATER TURBIDITY ANALYZER-----\n")
    water_turbidity = current_water_turbidity()
    print("Current water turbidiy (based on average of 5 recent measurements):", round(water_turbidity, 5), "NTU")
    if_safe = if_water_safe(water_turbidity)


if __name__ == '__main__':
    main()