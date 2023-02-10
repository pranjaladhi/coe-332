#Pranjal Adhikari pa8729

import json
import requests

def current_water_turbidity(numData):
    i = numData - 5
    t = 0
    for i in range (numData):
        a0 = turbidity['turbidity_data'][i][calibration_constant]
        I90 = turbidity['turbidity_data'][i][detector_current]
        t += calculate_turbidity(a0, I90)
    return (t/5)

def calculate_turbidity(a0, I90):
    return (a0 * I90)

# def min_time:





def main():
    turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
    turbidity = turbidity_data.json()
    numData = len(turbidity['turbidity_data'])
    print(numData)




if __name__ == '__main__':
    main()