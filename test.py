from docplex.cp.model import CpoModel
import matplotlib.pyplot as plt
import numpy as np
from sys_logger import sys_log
import random
import math
from decimal import *
import time


'''
If all the required packages are installed properly, the log file *test.log* should be created, and outputs are written 
there, from *output1* to *output5*. Besides, the file *test-figure.pdf* should be created, showing a graph. 
'''


logfile = 'test.log'
logger1 = sys_log(logfile, 'test', 0)


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


def create_list_of_all_plausible_traces(len_of_price_, q_, all_sols):
    list_of_all_sols = []
    one_solution = []
    dict_wallet_sols = {}
    for sol in all_sols:
        wallet = 0
        for i in range(len_of_price_):
            if sol[q_[i]] != 0:
                tuple_index_sol_value = (i, sol[q_[i]])
                one_solution.append(tuple_index_sol_value)
                wallet = wallet + Decimal(str(sol[q_[i]])) * Decimal(str(list_of_toll_price[i]))
        wallet = float(wallet)
        if wallet not in dict_wallet_sols:
            dict_wallet_sols[wallet] = [one_solution.copy()]
        else:
            dict_wallet_sols[wallet].append(one_solution.copy())
        list_of_all_sols.append(one_solution.copy())
        one_solution.clear()
    return dict_wallet_sols

list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]
length_of_toll_prices = len(list_of_toll_price)
plt.figure()
plt.grid()
start = time.time()
billing_period_ = 10
imodel, q = create_model(list_of_toll_price, billing_period_, 0, 10)
imodel.print_information()
all_sols = imodel.start_search()
dict_plausible_traces = create_list_of_all_plausible_traces(length_of_toll_prices, q, all_sols)
logger1.debug("output1: " + str(dict_plausible_traces))
end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("output2: " + str(elapsed_time))

x = Decimal('0.1')
y = Decimal('0.1')
summation = x + y
logger1.debug("output3: " + str(summation))

ceil_ = math.ceil(2.3)
logger1.debug("output4: " + str(ceil_))


rand_number = random.uniform(20, 30)
logger1.debug("output5: " + str(rand_number))


x = np.arange(1, 6)
y = x
plt.title("Matplotlib demo")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x, y)
plt.savefig("test-figure.pdf", format="pdf", bbox_inches="tight")
plt.show()