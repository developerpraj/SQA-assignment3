import retirement
import pytest
def test_Retirement1():
    assert retirement.Retiremnet(65,100000,1000000,20)>100
def test_Retirement2():
    assert retirement.Retiremnet(55,100000,1000000,20)<=100
    

    
