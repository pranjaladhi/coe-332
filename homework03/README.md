# Water Turbidity Analyzer

### Purpose
One of the goals of this project is to determine the turbidity of the water after collecting samples from different sites on Mars. The data of the samples is supplied through the [link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json)

### Code Scripts


### Running the Code
First, the source files of *turbidity_analyzer.py* and *test_turbidity_analyzer.py* must be placed in the same directory for the program to function properly. Next, the Python3 'requests' library will need to be installed in the top level directory, which is done by the line:
> pip3 install --user requests

This is required as the data set for the water is from the [URL](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json). Additionally, the 'pytest' unit testing framework will need to be installed for the *test_turbidity_analyzer.py* file. This is done by the line:
> pip3 install --user pytest

After the installations, the program can now be ran with the line:
> python3 turbidity_analyzer.py 

This will output the current turbidity of the water, based upon the average of the 5 most recent measurements. On the second line, a statement of whether the water is safe will be output based upon if the turbidity is above or below the threshold. Lastly, if the water is above the threshold and unsafe, the time required to wait until the water reaches below the threshold will be shown in hours. If the turbidity is less than 1.0 NTU, it is deemed safe for use immediately. Otherwise, it is required to wait mimimum time, given in hours, for the turbidity to reach a safe level. 