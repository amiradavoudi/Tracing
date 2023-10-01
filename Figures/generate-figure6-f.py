from docplex.cp.model import CpoModel
from decimal import *
from sys_logger import sys_log
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time


logfile = 'figure6-f.log'
logger1 = sys_log(logfile, 'figure6-f', 0)

'''
This file generates Figure 6(f) showing the average success rate for each number of toll stations.
To facilitate the quick generation of Figure6(f), we provide the file *generate-figure6-f-condensed.py* 
Please refer to Section 8 and Appendix G for the details of the evaluation.
'''


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


def if_int(num_):
    rem = num_ - int(num_)
    if rem == 0:
        return True


def generate_flat_rand_num(low_val, high_val):
    num_ = round(random.uniform(low_val, high_val), 2)
    if low_val != high_val:
        while(if_int(num_)):
            logger1.debug("num_ is:" + str(num_))
            num_ = round(random.uniform(low_val, high_val), 2)
        return num_
    else:
        return num_


list_of_period_counter = []
list_of_avg_success_rate = []

# 2018 toll prices

list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]
list_lower_wallet = [1, 10, 20]
list_upper_wallet = [10, 20, 40]
list_of_percentage_success_rate_number_of_all_points_freq_sols = []
counter = 0
plt.figure()
plt.grid()
list_of_toll_stations = []
list_of_list_of_avg_success_rates = []
start = time.time()
for lower_wallet, upper_wallet in zip(list_lower_wallet, list_upper_wallet):
    wallet_range = f"[${lower_wallet}, ${upper_wallet}]"
    logger1.debug("wallet range: " + f"{wallet_range}")
    for j in range(0, 1):
        list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]
        low_val = min(list_of_toll_price)
        high_val = max(list_of_toll_price)
        '''
        The index i denotes the number of toll stations we add to the Brisbane ETC system
        '''
        for i in range(0, 12):
            random.seed(i + j)
            if i != 0:
                random_price = generate_flat_rand_num(low_val, high_val)
                list_of_toll_price.append(random_price)
            max_frq = math.ceil(upper_wallet / min(list_of_toll_price))
            billing_period_ = max_frq
            length_of_toll_price = len(list_of_toll_price)
            list_of_toll_stations.append(length_of_toll_price)
            logger1.debug("-----------------------------------------------------------")
            logger1.debug("number of toll stations: " + str(length_of_toll_price))
            imodel, q = create_model(list_of_toll_price, billing_period_, lower_wallet, upper_wallet)
            imodel.print_information()
            all_sols = imodel.start_search()

            dict_wallet_sols = create_list_of_all_plausible_traces(length_of_toll_price, q, all_sols)
            list_of_wallets = dict_wallet_sols.keys()
            list_of_wallets = list(list_of_wallets)
            number_of_all_wallets = len(list_of_wallets)

            list_of_num_of_sols = []
            for wallets, list_of_solutions in dict_wallet_sols.items():
                number_of_sols = len(list_of_solutions)
                list_of_num_of_sols.append(number_of_sols)

            list_of_success_rates = []
            log_success_rate_number_of_all_cycle_type_freq_sols = []
            for num_of_sols in list_of_num_of_sols:
                success_rate = 1 / num_of_sols
                list_of_success_rates.append(success_rate)
                success_rate = round(success_rate * 100, 2)
                log_success_rate_number_of_all_cycle_type_freq_sols.append(success_rate)

            avg_success_rate = sum(list_of_success_rates) / len(list_of_success_rates)
            avg_success_rate = round(avg_success_rate * 100, 2)
            logger1.debug("list_of_wallets: " + str(list_of_wallets))
            logger1.debug("average success rate: " + str(avg_success_rate))
            list_of_avg_success_rate.append(avg_success_rate)

        logger1.debug("=============================================")
        logger1.debug("list_of_toll_price: " + str(list_of_toll_price))
        logger1.debug("list of avg success rates:" + str(list_of_avg_success_rate))
        colors = ['r', 'g', 'b', "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
        plt.plot(list_of_toll_stations, list_of_avg_success_rate, '--', color=colors[j], marker='o', markerfacecolor='black', markersize=4, linewidth=1.5)
        labels1 = np.arange(9, 21, 1)
        plt.xticks(labels1, labels1)
        plt.xlim(9, 20)

        labels2 = np.arange(0, 101, 10)
        plt.yticks(labels2, labels2)
        max_y_range = 101
        plt.ylim(0, max_y_range)

        plt.xlabel('Number of toll stations')
        plt.ylabel('Success rate (%)')
        list_of_toll_stations.clear()
        list_of_avg_success_rate.clear()
        list_of_toll_price.clear()
        logger1.debug("---------------------------------------------------------------------------------------------")
plt.savefig("figure6-f.pdf", format="pdf", bbox_inches="tight")
plt.show()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))


