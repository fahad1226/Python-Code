import numpy as np

height = [5.6,5.5,4.5,6,7,4.6]
weight = [1,2,3,45,5,6]
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print(bmi)
