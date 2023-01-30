import os
import sys
sys.path.append(r'C:\Users\Lenovo\OneDrive\Desktop\jenkins_pipeline_tests\src')
import math_func
#SET PYTHONPATH=C:\Users\Lenovo\OneDrive\Desktop\jenkins_pipeline_tests\src
value1 = int(os.getenv("value1"))
value2 = int(os.getenv("value2"))
def test_add():
    assert math_func.add(value1,value2) == 10
    assert math_func.add(value1) ==9
def test_product():
	assert math_func.product(value1,value2) == 25
	assert math_func.product(value1) ==10

#================
# import sys
# sys.path.append(r'C:\Users\Lenovo\OneDrive\Desktop\jenkins_pipeline_tests\src')
# import math_func
# #SET PYTHONPATH=C:\Users\Lenovo\OneDrive\Desktop\jenkins_pipeline_tests\src
#
# def test_add():
#     assert math_func.add(5,5) == 10
#     assert math_func.add(5) ==7
# def test_product():
# 	assert math_func.product(5,5) == 25
# 	assert math_func.product(5) ==10
#
# #print(sys.path)

#==============================================

