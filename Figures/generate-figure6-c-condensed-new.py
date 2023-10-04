from docplex.cp.model import CpoModel
from decimal import *
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time
import os.path
import sys
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(os.path.dirname(os.path.dirname(directory)))
from Tracing.sys_logger import sys_log
logfile = 'figure6-c.log'
logger1 = sys_log(logfile, 'figure6-c', 0)


'''
This file generates Figure 6(c) showing the average success rate for each toll price range w.r.t wallet range [20, 40].
To facilitate the quick generation of Figure6(c), we provide the file *generate-figure6-c-condensed.py* 
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


def create_model(list_of_cycle_price, billing_period_, wallet_):
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
    imodel.add_constraint(imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables) <= wallet_)
    imodel.add_constraint(20 < imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables))
    return imodel, q


def if_int(num_):
    rem = num_ - int(num_)
    if rem == 0:
        return True


'''
The function create_random_toll_price gets a toll price range, where low_val and high_val indicate the lower and 
upper bounds of the range. The function selects #number_of_toll_prices_ random toll prices within this range. 
Each experiment uses a different seed number, resulting in the generation of different random toll prices.
'''


def generate_float_rand_num(low_val, high_val):
    num_ = round(random.uniform(low_val, high_val), 2)
    if low_val != high_val:
        while(if_int(num_)):
            logger1.debug("num_ is:" + str(num_))
            num_ = round(random.uniform(low_val, high_val), 2)
        return num_
    else:
        return num_


def create_random_toll_price(low_val, high_val, number_of_toll_prices_, seed_):
    random.seed(seed_)
    list_of_random_toll_price = []
    for i in range(0, number_of_toll_prices_):
        list_of_random_toll_price.append(generate_float_rand_num(low_val, high_val))
    return list_of_random_toll_price


number_of_toll_prices = 9
min_price = 1
max_price = 10
wallet_ = 40

list_of_avg_success_rate = []
list_of_upper_bound_prices = []
list_of_list_of_avg_success_rates = []
counter = 0

start = time.time()


'''
The precomputed average success rates are stored in the list, namely list_of_list_of_avg_success_rates. We only 
precompute the ASRs for the toll price ranges [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], and[1,7] which takes quite 
large time of computation. The ASRs for the rest of the toll price ranges are generated through the below code.
'''

list_precomputed_asr = [[0.36, 1.69, 0.85, 0.27, 1.49, 0.21, 1.72, 0.3, 0.59, 0.7, 0.91, 0.44, 0.89, 0.96, 1.39, 0.7, 0.69, 0.3, 1.58, 0.94, 0.64, 1.15, 1.06, 1.37, 1.56, 0.34, 0.95, 0.59, 0.74, 1.01, 0.75, 1.59, 0.24, 1.13, 1.15, 1.31, 0.52, 0.23, 1.34, 1.79, 0.86, 1.14, 1.35, 1.39, 0.44, 1.59, 1.55, 1.5, 1.76, 1.73], [1.26, 1.26, 1.46, 2.03, 0.25, 2.22, 0.86, 0.57, 0.92, 1.19, 0.33, 1.08, 1.31, 1.25, 1.86, 1.92, 0.61, 1.67, 2.13, 2.17, 1.53, 2.24, 1.4, 1.92, 1.13, 2.09, 2.15, 0.77, 1.82, 0.31, 1.69, 1.16, 0.52, 1.55, 1.87, 1.28, 1.04, 1.95, 1.65, 0.77, 2.05, 0.78, 1.42, 2.29, 1.03, 2.19, 0.89, 0.53, 0.93, 1.19], [0.83, 1.41, 2.65, 0.26, 2.47, 1.8, 1.12, 1.29, 1.81, 1.5, 5, 2.58, 0.89, 1.37, 1.71, 0.96, 1.51, 2.51, 2.55, 0.23, 6, 2.43, 2.31, 1.38, 2.17, 0.67, 0.69, 2.57, 2.58, 2.28, 2.03, 2.5, 2.14, 2.42, 1.58, 2.05, 1.79, 0.5, 2.06, 1.6, 0.67, 1.52, 2.21, 1.13, 1.63, 0.93, 2.09, 1.66, 1.68, 2.67], [3.01, 2.05, 3.12, 3.27, 2.94, 0.85, 0.55, 0.89, 0.94, 0.82, 9, 0.54, 0.8, 0.53, 2.86, 3.06, 0.47, 1.52, 1.46, 1.9, 11, 2.44, 0.84, 0.87, 3.26, 1.47, 0.96, 3.25, 0.22, 3.13, 11, 2.06, 2.94, 2.33, 2.16, 3.01, 1.7, 1.36, 1.75, 2.14, 9, 2.51, 2.69, 2.34, 2.59, 2.48, 2.12, 1.58, 1.71, 1.55], [2.46, 3.11, 0.92, 3.37, 2.32, 0.5, 1.84, 1.3, 2.08, 0.96, 10, 1.86, 0.9, 0.71, 2.84, 0.51, 0.86, 2.75, 1.3, 1.62, 13, 0.3, 1.63, 3.5, 0.91, 3.61, 1.96, 3.22, 1.62, 2.87, 13, 0.2, 0.27, 1.92, 0.3, 0.76, 1.25, 2.99, 1.16, 2.64, 11, 2.82, 0.38, 3.78, 2.31, 2.9, 2.09, 2.97, 0.54, 1.86], [1.84, 4.03, 0.58, 2.59, 3.22, 3.44, 1.7, 0.75, 4.05, 3.83, 11, 2.23, 0.59, 2.5, 2.11, 1.47, 2.97, 4.08, 0.6, 1.3, 15, 0.38, 2.35, 1.06, 1.24, 3.57, 3.9, 2.32, 1.35, 2.62, 15, 2.6, 2.05, 3.24, 4.03, 4.23, 1.38, 1.45, 0.95, 2.36, 13, 4.23, 1.52, 1.64, 3.2, 4.2, 2.49, 1.09, 3.76, 0.84], [4.95, 0.86, 1.12, 15.31, 14.57, 0.29, 1.54, 1.01, 6.53, 8.51, 1.76, 2.05, 4.0, 2.41, 1.69, 3.28, 2.04, 4.81, 28.59, 7.33, 1.2, 3.0, 2.44, 4.43, 1.29, 3.43, 0.45, 3.45, 1.76, 0.21, 2.25, 14.54, 17.55, 23.29, 24.84, 8.77, 2.55, 1.18, 2.53, 10.69, 1.32, 1.24, 0.17, 0.12, 4.95, 0.61, 3.59, 0.24, 2.9, 5.14]]
list_of_upper_bound_prices = [1, 2, 3, 4, 5, 6, 7]


'''
The loop below generates toll price ranges denoted as [1, upper_bound_price], where the upper_bound_price is at most
equal to max_price.
'''


for upper_bound_price in range(8, max_price + 1, 1):
    logger1.debug("upper_bound_price: " + str(upper_bound_price))
    list_of_upper_bound_prices.append(upper_bound_price)
    counter = counter + 1
    # We repeat the experiment 50 times
    for seed in range(1, 2):
        list_of_toll_price = create_random_toll_price(min_price, upper_bound_price, number_of_toll_prices, seed + counter)

        max_frq = math.ceil(wallet_ / min(list_of_toll_price))
        billing_period_ = max_frq
        logger1.debug("billing_period_: " + str(billing_period_))
        logger1.debug("list_of_toll_price: " + str(list_of_toll_price))
        length_of_toll_prices = len(list_of_toll_price)
        imodel, q = create_model(list_of_toll_price, billing_period_, wallet_)
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

        list_of_success_rates = []
        percentage_success_rate_number_of_all_points_freq_sols = []
        for num_of_sols in list_of_num_of_sols:
            success_rate = 1 / num_of_sols
            list_of_success_rates.append(success_rate)
            success_rate = round(success_rate * 100, 2)

        avg_success_rate = sum(list_of_success_rates) / len(list_of_success_rates)
        avg_success_rate = round(avg_success_rate * 100, 2)

        logger1.debug("list_of_wallets: " + str(list_of_wallets))
        logger1.debug("number_of_all_wallets: " + str(number_of_all_wallets))
        logger1.debug("list_of_success_rates: " + str(list_of_success_rates))
        list_of_avg_success_rate.append(avg_success_rate)
        logger1.debug("list_of_avg_success_rate: " + str(list_of_avg_success_rate))
        logger1.debug("***")
        list_of_wallets.clear()

    list_of_list_of_avg_success_rates.append(list_of_avg_success_rate.copy())
    logger1.debug("list_of_list_of_avg_success_rates: " + str(list_of_list_of_avg_success_rates))
    list_of_avg_success_rate.clear()
    logger1.debug("---------------------------------------------------------------------------------------------")

logger1.debug("list_of_list_of_avg_success_rates: " + str(list_of_list_of_avg_success_rates))

updated_list_of_list_of_avg_success_rates = []
for list_asr in list_precomputed_asr:
    updated_list_of_list_of_avg_success_rates.append(list_asr)

for list_asr in list_of_list_of_avg_success_rates:
    updated_list_of_list_of_avg_success_rates.append(list_asr)


'''
Draw the graph
'''
list_format_upper_bound_price = []
for upper_bound_price in list_of_upper_bound_prices:
    a = [1, upper_bound_price]
    list_format_upper_bound_price.append(str(a))
logger1.debug("list_format_upper_bound_price: " + str(list_format_upper_bound_price))

len_list_of_upper_bound_prices = len(list_of_upper_bound_prices)
label = []

for i in range(len_list_of_upper_bound_prices):
    label.append(i + 1)

fig, ax = plt.subplots()
plt.gcf().subplots_adjust(bottom=0.17)
bp = ax.boxplot(updated_list_of_list_of_avg_success_rates, patch_artist=True)
plt.xticks(label, list_format_upper_bound_price, rotation=45)
plt.xlabel("Range of toll prices (in dollar)")

labels2 = np.arange(0, 101, 10)
plt.ylim(0, 102)
plt.yticks(labels2, labels2)
plt.ylabel("Average success rate (%)")
plt.grid()

for median in bp['medians']:
    median.set(color='red',
               linewidth=2)

for whisker in bp['whiskers']:
    whisker.set(color='#8B008B',
                linewidth=1.5,
                )

col = '#caff91'
colors = []
for i in range(len_list_of_upper_bound_prices):
    colors.append(col)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.savefig("figure6-c.pdf", format="pdf", bbox_inches="tight")
plt.show()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))