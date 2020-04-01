import bmi
import pytest

def test_bmi4():
    assert bmi.bmi(100,67)==16.039206950323013

def test_bmi1():
    assert bmi.bmi(167,56)==38.34183673469387
def test_bmi2():
    assert bmi.bmi(145,67)==23.256850077968366
def test_bmi3():
    assert bmi.bmi(166,55)== 39.51074380165289
    
    
    

