# Water Turbidity Analyzer

### Purpose
One of the goals of this project is to determine the turbidity of the water after collecting samples from different sites on Mars. The data of the samples is supplied through this [link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json), a JSON dictionary with the key `turbidity_data`. Taking the data, the current water turbidity is determined by taking the average of the 5 most recent measurements of the calibration constant and ninety degree detector current. 
    The turbidity utilizing the two variables is calculated using the equation: T (turbidity) = a0 (calibration constant) * I90 (ninety degree detector current)


### Code Scripts


### Running the Code
First, the source files of *turbidity_analyzer.py* and *test_turbidity_analyzer.py* must be placed in the same directory for the program to function properly. Next, the Python3 'requests' library will need to be installed in the top level directory, which is done by the line:
> pip3 install --user requests

This is required as the data set for the water is from the [URL](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json). Additionally, the 'pytest' unit testing framework will need to be installed for the *test_turbidity_analyzer.py* file to run properly. This is done by the line:
> pip3 install --user pytest

After the installations, the program can now be ran with the line:
> python3 turbidity_analyzer.py 

This will output the current turbidity of the water, based upon the average of the 5 most recent measurements. On the second line, a statement of whether the water is safe will be output based upon if the turbidity is above or below the threshold. Lastly, if the water is above the threshold and unsafe, the time required to wait until the water reaches below the threshold will be shown in hours. If the turbidity is less than 1.0 NTU, it is deemed safe for use immediately. Otherwise, it is required to wait mimimum time, given in hours, for the turbidity to reach a safe level.

After the *turbidity_analyzer.py* file has been ran, the next step is to run the *test_turbidity_analyzer.py* to determine if the functions within the former file are correct. This can be done by the line: 
> pytest

The output will show whether the 2 functions within the *turbidity_analyzer.py* file have passed the tests in the *test_turbidity_analyzer.py*. If the output result in the word "passed," the functions are correct, otherwise incorrect.