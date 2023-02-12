# Water Turbidity Analyzer

### Purpose
One of the goals of this project is to determine the turbidity of the water after collecting samples from different sites on Mars, to conclude whether the water is within a safe threshold for use. The data of the samples is supplied through the [link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json), a JSON dictionary with the key `turbidity_data`. Taking the data, the current water turbidity is determined by taking the average of the 5 most recent measurements of the calibration constant and ninety degree detector current, and a conclusion is made if the water is safe for use. This is all done within the file *turbidity_analyzer.py*. Afterwards, the functions written in the analyzer file will be tested from the file *test_turbidity_analyzer.py*. A main objective of this project is to learn how to work with the Python `requests` library and the `pytest` unit testing framework. These two libraries allow for the expansion of standard Python library to work with additional data sets as well as to automate testing of the programs written. With the utilization of these two libraries in the industry, it is important to become fimiliar with them in understanding how powerful and capable they are.

### Code Scripts
In the *turbidity_analyzer.py* file, lines 7-18 `def current_water_turbidity...` is the function which takes arguments of the calibration constant and ninety degree detector current to determine the water turbidity of the sample. The function after, `def time_required...` in lines 20-32, the minimum time required is determined utilizing the current water turbidity as the argument. Within lines 35-53 in `def main()`, line 37
```
turbidity_data = requests.get(url='https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json')
```
utilizes the `requests` library to retrieve the water data from the [URL](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json). Next in lines 38-45,
```
i = len(turbidity_data.json()['turbidity_data']) - 5
water_turbidity = 0
while (i < (len(turbidity_data.json()['turbidity_data']))):
    a0 = turbidity_data.json()['turbidity_data'][i]['calibration_constant'] 
    I90 = turbidity_data.json()['turbidity_data'][i]['detector_current'] 
    water_turbidity += current_water_turbidity(a0, I90)
    i += 1
water_turbidity = water_turbidity/5
```
the while loop iterates through the 5 most recent measurements and the calculates the current water turbidity. Lastly, lines 48-53
```
if ts < water_turbidity:
        print("*UNSAFE WARNING* Turbidity is above the threshold for safe use")
        print("Minimum time required to return below a safe threshold:", round(time_required(water_turbidity), 2), "hours")
    else:
        print("*SAFE* Turbidity is below the threshold for safe use")
        print("Minimum time required to return below a safe threshold: 0 hours")
```
determines whether the water is above or below the threshold for safe use, issues a warning if above, and outputs the minimum time required for the water to reach below the threshold.

In the *test_turbidity_analyzer.py* file, lines 7-9
```
def test_current_water_turbidity(): 
    assert current_water_turbidity(2.0, 3.0) == 6.0
    assert current_water_turbidity(5.0, 1.0) == 5.0
```
test the `current_water_turbidity()` function in the source file. Lines 11-13
```
def test_time_required(): 
    assert time_required(1.9) == 31.770686774033962
    assert time_required(1.05) == 2.415030985828419
```
test the `time_required()` function, determining if the output value is correct.

### Running the Code
First, the source files of *turbidity_analyzer.py* and *test_turbidity_analyzer.py* must be placed in the same directory for the program to function properly. Next, the Python3 'requests' library will need to be installed in the top level directory, which is done by the line:
> pip3 install --user requests

This is required as the data set for the water is from the [URL](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json). Additionally, the 'pytest' unit testing framework will need to be installed for the *test_turbidity_analyzer.py* file to run properly. This is done by the line:
> pip3 install --user pytest

After the installations, the program can now be ran with the line:
> python3 turbidity_analyzer.py 

This will output the current turbidity of the water, based upon the average of the 5 most recent measurements. On the second line, a statement of whether the water is safe will be output based upon if the turbidity is above or below the threshold. Lastly, if the water is above the threshold and unsafe, the time required to wait until the water reaches below the threshold will be shown in hours. If the turbidity is less than 1.0 NTU, it is deemed safe for use immediately. Otherwise, it is required to wait mimimum time, given in hours, for the turbidity to reach a safe level. An example of the output may look like:
```
-----WATER TURBIDITY ANALYZER-----

Current water turbidity (based on average of 5 recent measurements): 1.13657 NTU
*UNSAFE WARNING* Turbidity is above the threshold for safe use
Minimum time required to return below a safe threshold: 6.34 hours
```

After the *turbidity_analyzer.py* file has been ran, the next step is to run the *test_turbidity_analyzer.py* to determine if the functions within the former file are correct. This can be done by the line: 
> pytest

The output will show whether the 2 functions within the *turbidity_analyzer.py* file have passed the tests in the *test_turbidity_analyzer.py*. If the output result in the word "passed," the functions are correct, otherwise incorrect. An example output may be:
```
======================================================================================================== test session starts =========================================================================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/pa8729/coe-332/homework03
collected 2 items                                                                                                                                                                                                                    

test_turbidity_analyzer.py ..                                                                                                                                                                                                  [100%]

========================================================================================================= 2 passed in 0.07s ==========================================================================================================
```