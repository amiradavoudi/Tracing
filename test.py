from docplex.cp.model import CpoModel
import matplotlib.pyplot as plt
import numpy as np
from sys_logger import sys_log
import random
import math
from decimal import *
import time


'''
The toll-based-attacking algorithm
'''

logfile = 'toll-based-algo.log'
logger1 = sys_log(logfile, 'toll-based-algo', 0)


def create_model(list_of_cycle_price, billing_period_, lower_wallet_, upper_wallet_):
    imodel = CpoModel(name='test')
    length = len(list_of_cycle_price)
    num_of_variables = range(length)
    q = imodel.integer_var_dict(num_of_variables)

    '''
    Add constraints for each variable in the linear equation
    '''
    for index_, price_ in enumerate(list_of_cycle_price):
        num_of_trans_per_agent_upper_bound = billing_period_
        if price_ != 0:
            imodel.add_constraint(q[index_] <= num_of_trans_per_agent_upper_bound)
            imodel.add_constraint(0 <= q[index_])
        else:
            imodel.add_constraint(q[index_] == 0)
    imodel.add_constraint(imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables) <= upper_wallet_)
    imodel.add_constraint(lower_wallet_ < imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables))
    return imodel, q


list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]
plt.figure()
plt.grid()
start = time.time()
billing_period_ = 10
imodel, q = create_model(list_of_toll_price, billing_period_, 0, 10)
imodel.print_information()
all_sols = imodel.start_search()
print(all_sols)

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))

x = Decimal('0.1')
y = Decimal('0.1')
s = x + y
print(s)

ceil_ = math.ceil(2.3)
print(ceil_)

print(random.uniform(20, 30))

x = np.arange(1, 6)
y = 2 * x
plt.title("Matplotlib demo")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.show()