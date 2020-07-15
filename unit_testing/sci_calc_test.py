from sci_calc import SciCalc
my_sci_calc = SciCalc()

def test_find_sqrt():
    assert my_sci_calc.find_sqrt(100) == 10.0

#import math
#math.sqrt()


def test_find_ceil():
    assert my_sci_calc.find_ceil(12.7) == 13

#math.ceil()