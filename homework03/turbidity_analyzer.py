#Pranjal Adhikari pa8729

import json
import requests

turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
turbidity = turbidity_data.json()

def current_water_turbidity():
    i = len(turbidity['turbidity_data']) - 5
    t = 0
    while (i <= (len(turbidity['turbidity_data']))):
        a0 = turbidity['turbidity_data'][227]['calibration_constant']
        I90 = turbidity['turbidity_data'][227]['detector_current']
        t = calculate_turbidity(a0, I90)
        i += 1
    return t

def calculate_turbidity(a0, I90):
    return (a0 * I90)

# def min_time:





def main():
    water_turbidity = current_water_turbidity()
    print(water_turbidity)

if __name__ == '__main__':
    main()