from docplex.cp.model import CpoModel
from decimal import *
from sys_logger import sys_log
import matplotlib.pyplot as plt
import numpy as np
import math
import time

'''
Generates the graph concerning Run-time (ms) per wallet balance. 
It should be noted that the resulted run-times depend on the system on 
which the source code is run. The source code is performed on Windows 
Server 2019 Standard (64-bit), with 96.0 GB RAM, with x64-based CPU 3.70 GHz,
Intel(R) Xeon(R) E-2288G. 
'''

logfile = 'figure2(b).log'
logger1 = sys_log(logfile, 'figure2(b)', 0)


def create_list_of_all_sols_cycle_type_freq(len_of_price_, q_, all_sols):
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


def create_list_of_all_sols_points_type_freq(len_of_price_, q_, all_sols):
    list_of_all_sols = []
    one_solution = []
    for sol in all_sols:
        for i in range(len_of_price_):
            if sol[q_[i]] != 0:
                tuple_index_sol_value = (i, sol[q_[i]])
                one_solution.append(tuple_index_sol_value)
        list_of_all_sols.append(one_solution.copy())
        one_solution.clear()
    return list_of_all_sols


def create_model_inequality(list_of_cycle_price, billing_period_, lower_wallet_, upper_wallet_):
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


def create_model_equation(list_of_cycle_price, billing_period_, wallet_):

    imodel = CpoModel(name='test1')
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

    imodel.add_constraint(imodel.sum((q[i]) * list_of_cycle_price[i] for i in num_of_variables) == (wallet_))
    return imodel, q

'''
2018 toll prices
'''
list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]

length_of_toll_prices = len(list_of_toll_price)
list_of_num_of_sols = []

'''
The list "list_lower_wallet" takes the lower bounds of the wallet ranges, namely [1, 10], [10, 20], and [20, 40]. The
list "list_upper_wallet" takes the upper bounds of the mentioned wallet ranges.
'''

list_lower_wallet = [1, 10, 20]
list_upper_wallet = [10, 20, 40]
list_of_percentage_success_rate_number_of_all_points_freq_sols = []
counter = 0
plt.figure()
plt.grid()

list_of_times = []
list_of_list_of_times = []
for lower_wallet, upper_wallet in zip(list_lower_wallet, list_upper_wallet):
    wallet_range = f"[${lower_wallet}, ${upper_wallet}]"
    length_of_toll_prices = len(list_of_toll_price)
    max_frq = math.ceil(upper_wallet / min(list_of_toll_price))
    billing_period_ = max_frq
    imodel, q = create_model_inequality(list_of_toll_price, billing_period_, lower_wallet, upper_wallet)
    imodel.print_information()
    all_sols = imodel.start_search()
    dict_wallet_sols = create_list_of_all_sols_cycle_type_freq(length_of_toll_prices, q, all_sols)
    list_of_wallets = dict_wallet_sols.keys()
    list_of_wallets = list(list_of_wallets)
    number_of_all_wallets = len(list_of_wallets)
    list_of_wallets.sort()

    for wallet_ in list_of_wallets:
        start = time.time()
        logger1.debug("start time: " + str(start))
        logger1.debug("Solving the equation for the wallet: " + str(wallet_))
        imodel, q = create_model_equation(list_of_toll_price, billing_period_, wallet_)
        imodel.print_information()
        all_sols = imodel.start_search()
        list_of_all_types_sols = create_list_of_all_sols_points_type_freq(length_of_toll_prices, q, all_sols)
        end = time.time()
        logger1.debug("end time: " + str(end))
        elapsed_time = (end - start) * 1000
        elapsed_time = round(elapsed_time, 2)
        list_of_times.append(elapsed_time)
        logger1.debug("elapsed_time for solving: " + str(elapsed_time))
        logger1.debug("--------------------------------")
    logger1.debug("wallet range: " + f"{wallet_range}")
    logger1.debug('list of times in ms: ' + str(list_of_times))
    colors = ['r', 'b', 'g']
    plt.plot(list_of_wallets, list_of_times, '.', color=colors[counter], markersize=.8)

    labels1 = np.arange(0, 41, 5)
    plt.xticks(labels1, labels1)
    plt.xlim(0, 40)

    plt.xlabel('Wallet balances (in dollar)')
    plt.ylabel('Run-time (ms)')
    list_of_list_of_times.append(list_of_times)
    list_of_times.clear()
    counter = counter + 1
logger1.debug("list of wallets: " +  str(list_of_wallets))
plt.savefig("runtimes.pdf", format="pdf", bbox_inches="tight")
plt.show()