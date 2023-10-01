from docplex.cp.model import CpoModel
from decimal import *
from sys_logger import sys_log
import matplotlib.pyplot as plt
import numpy as np
import math
import time

logfile = 'figure4-a.log'
logger1 = sys_log(logfile, 'figure4-a.log', 0)


# This file generates the graph concerning the number of solutions per each wallet balance


'''
Function create_list_of_all_plausible_traces creates all plausible traces corresponding to all wallet balances within 
the wallet range [w_l, w_u]
'''


def create_list_of_all_plausible_traces(len_of_price_, q_, all_sols):
    list_of_all_sols = []
    one_solution = []
    dict_wallet_sols_ = {}
    for sol in all_sols:
        wallet = 0
        for i in range(len_of_price_):
            if sol[q_[i]] != 0:
                tuple_index_sol_value = (i, sol[q_[i]])
                one_solution.append(tuple_index_sol_value)
                wallet = wallet + Decimal(str(sol[q_[i]])) * Decimal(str(list_of_toll_price[i]))
        wallet = float(wallet)
        if wallet not in dict_wallet_sols_:
            dict_wallet_sols_[wallet] = [one_solution.copy()]
        else:
            dict_wallet_sols_[wallet].append(one_solution.copy())
        list_of_all_sols.append(one_solution.copy())
        one_solution.clear()
    return dict_wallet_sols_


'''
Function create_model creates Inequality 5 in the paper based on the toll prices and the lower and upper bound of
the wallet range
'''


def create_model(list_of_cycle_price, billing_period_, lower_wallet_, upper_wallet_):
    imodel_ = CpoModel(name='test')
    length = len(list_of_cycle_price)
    num_of_variables = range(length)
    q = imodel_.integer_var_dict(num_of_variables)

    # Add constraints for each variable in the linear equation

    for index_, price_ in enumerate(list_of_cycle_price):
        num_of_trans_per_agent_upper_bound = billing_period_
        if price_ != 0:
            imodel_.add_constraint(q[index_] <= num_of_trans_per_agent_upper_bound)
            imodel_.add_constraint(0 <= q[index_])
        else:
            imodel_.add_constraint(q[index_] == 0)
    imodel_.add_constraint(imodel_.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables) <= upper_wallet_)
    imodel_.add_constraint(lower_wallet_ < imodel_.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables))
    return imodel_, q


list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]

'''
The list "list_lower_wallet" takes the lower bounds of the wallet ranges, namely [1, 10], [10, 20], and [20, 40]. 
The list "list_upper_wallet" takes the upper bounds of the mentioned wallet ranges.
'''

list_lower_wallet = [1, 10, 20]
list_upper_wallet = [10, 20, 40]

list_of_percentage_success_rate_number_of_all_points_freq_sols = []
counter = 0
plt.figure()
plt.grid()

start = time.time()
for lower_wallet, upper_wallet in zip(list_lower_wallet, list_upper_wallet):
    wallet_range = f"[${lower_wallet}, ${upper_wallet}]"
    length_of_toll_prices = len(list_of_toll_price)
    max_frq = math.ceil(upper_wallet / min(list_of_toll_price))
    billing_period_ = max_frq
    imodel, q = create_model(list_of_toll_price, billing_period_, lower_wallet, upper_wallet)
    imodel.print_information()

    # Function imodel.start_search() solves the inequality in the model

    all_sols = imodel.start_search()
    dict_wallet_sols = create_list_of_all_plausible_traces(length_of_toll_prices, q, all_sols)
    list_of_wallets = dict_wallet_sols.keys()
    list_of_wallets = list(list_of_wallets)
    number_of_all_wallets = len(list_of_wallets)

    list_of_num_of_sols = []
    for wallets, list_of_solutions in dict_wallet_sols.items():
        number_of_sols = len(list_of_solutions)
        list_of_num_of_sols.append(number_of_sols)

    logger1.debug("---------------------------------------------------------------------------------------------")
    logger1.debug("wallet_range: " + f"{wallet_range}")
    list_of_success_rates = []
    list_of_wallets, list_of_num_of_sols = zip(*sorted(zip(list_of_wallets, list_of_num_of_sols)))
    list_of_wallets = list(list_of_wallets)
    list_of_num_of_sols = list(list_of_num_of_sols)
    logger1.debug("sorted list_of_plausible_wallets: " + str(list_of_wallets))
    logger1.debug("sorted list_of_num_of_sols" + str(list_of_num_of_sols))
    colors = ['r', 'b', 'g']
    plt.plot(list_of_wallets, list_of_num_of_sols, '.', color=colors[counter], markersize=.7)

    labels1 = np.arange(0, 41, 5)
    plt.xticks(labels1, labels1)
    plt.xlim(0, 40)

    plt.xlabel('Wallet balances (in dollar)')
    plt.ylabel('Number of solutions')
    list_of_num_of_sols.clear()
    list_of_wallets.clear()
    counter = counter + 1
plt.savefig("figure4-a.pdf", format="pdf", bbox_inches="tight")
plt.show()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))


