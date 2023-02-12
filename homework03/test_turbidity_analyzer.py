#Pranjal Adhikari pa8729

from turbidity_analyzer import current_water_turbidity, time_required
import pytest

def test_current_water_turbidity():
    assert current_water_turbidity([{1.0}, {2.0}, {3.0}, {4.0}, {5.0}, {6.0}, {7.0}, {8.0}, {9.0}, {10.0}]) == 38.0

def test_time_required():
    assert time_required(1.9) == 31.770686774033962
