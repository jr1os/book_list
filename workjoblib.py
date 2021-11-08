from math import sqrt
from joblib import Parallel, delayed


my_list = Parallel(n_jobs=2)(delayed(sqrt)(i ** 2) for i in range(10))
print(my_list)
