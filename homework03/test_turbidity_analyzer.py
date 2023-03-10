#Pranjal Adhikari pa8729

from turbidity_analyzer import current_water_turbidity, time_required
import pytest


def test_current_water_turbidity(): #test turbidity caluclating function
    assert current_water_turbidity(2.0, 3.0) == 6.0
    assert current_water_turbidity(5.0, 1.0) == 5.0

def test_time_required(): #test time needed to reach safe threshold function
    assert time_required(1.9) == 31.770686774033962
    assert time_required(1.05) == 2.415030985828419
