from docplex.cp.model import CpoModel
from decimal import *
from sys_logger import sys_log
import matplotlib.pyplot as plt
import math
import time


logfile = 'tsd-attack.log'
logger1 = sys_log(logfile, 'tsd-attack', 0)

# This file generates the results, i.e., the ASRs regarding the tsd-attack, shown in Table 1


'''
Function create_list_of_all_plausible_traces creates all plausible traces corresponding to all wallet balances within 
the wallet range [w_l, w_u]
'''


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


'''
Function create_model creates Inequality 5 in the paper based on the toll prices and the lower and upper bound of
the wallet range
'''


def create_model(list_of_cycle_price, billing_period_, lower_wallet_, upper_wallet_):
    imodel = CpoModel(name='test')
    length = len(list_of_cycle_price)
    num_of_variables = range(length)
    q = imodel.integer_var_dict(num_of_variables)

    # Add constraints for each variable in the linear equation

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


# 2018 toll prices

list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]
list_lower_wallet = [1, 10, 20]
list_upper_wallet = [10, 20, 40]


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
    all_sols = imodel.start_search()

    dict_wallet_sols = create_list_of_all_plausible_traces(length_of_toll_prices, q, all_sols)
    list_of_wallets = dict_wallet_sols.keys()
    list_of_wallets = list(list_of_wallets)
    number_of_all_wallets = len(list_of_wallets)
    list_of_num_of_sols = []
    for wallets, list_of_solutions in dict_wallet_sols.items():
        number_of_sols = len(list_of_solutions)
        list_of_num_of_sols.append(number_of_sols)

    list_of_success_rates = []
    percentage_success_rate_number_of_all_points_freq_sols = []
    for num_of_sols in list_of_num_of_sols:
        success_rate = 1 / num_of_sols
        list_of_success_rates.append(success_rate)

        success_rate = round(success_rate * 100, 2)
        percentage_success_rate_number_of_all_points_freq_sols.append(success_rate)

    logger1.debug("---------------------------------------------------------------------------------------------")

    logger1.debug("The information about the wallet range " + f"{wallet_range}")
    logger1.debug("The information about the wallet range " + f"{wallet_range}")
    average_success_rate = sum(percentage_success_rate_number_of_all_points_freq_sols)/len(percentage_success_rate_number_of_all_points_freq_sols)
    average_success_rate= math.ceil(average_success_rate)
    logger1.debug("average_success_rate (ASR): " + f"{average_success_rate}%")
    logger1.debug("list_of_plausible_wallets: " + f"{list_of_wallets}")
    logger1.debug("number_of_all_plausible_wallets: " + f"{number_of_all_wallets}")
    list_of_wallets, percentage_success_rate_number_of_all_points_freq_sols = zip(*sorted(zip(list_of_wallets, percentage_success_rate_number_of_all_points_freq_sols)))
    list_of_wallets = list(list_of_wallets)
    percentage_success_rate_number_of_all_points_freq_sols = list(percentage_success_rate_number_of_all_points_freq_sols)

    percentage_success_rate_number_of_all_points_freq_sols.clear()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))

