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
logfile = 'figure6-b.log'
logger1 = sys_log(logfile, 'figure6-b', 0)

'''
This file generates Figure 6(b) showing the average success rate for each toll price range w.r.t wallet range [10, 20].
Note: To facilitate the quick generation of Figure6(b), we provide the file *generate-figure6-b-condensed.py*. 
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
    imodel.add_constraint(10 < imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables))
    return imodel, q


def if_int(num_):
    rem = num_ - int(num_)
    if rem == 0:
        return True


'''
Function generate_float_rand_num generates random toll prices that are fractional (not integers). This function 
generates toll prices that resemble those used in Brisbane's ETC system.
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


'''
The function create_random_toll_price gets a toll price range, where low_val and high_val indicate the lower and 
upper bounds of the range. The function selects #number_of_toll_prices_ random toll prices within this range. 
Each experiment uses a different seed number, resulting in the generation of different random toll prices.
'''


def create_random_toll_price(low_val, high_val, number_of_toll_prices_, seed_):
    random.seed(seed_)
    list_of_random_toll_price = []
    for i in range(0, number_of_toll_prices_):
        list_of_random_toll_price.append(generate_float_rand_num(low_val, high_val))
    return list_of_random_toll_price


number_of_toll_prices = 9
min_price = 1
max_price = 10
wallet_ = 20

list_of_avg_success_rate = []
list_of_upper_bound_prices = []
list_of_list_of_avg_success_rates = []
counter = 0

start = time.time()

'''
To facilitate the quick generation of Figure6(b), we provide this file *generate-figure6-b-condensed.py*, which takes
the precomputed average success rates as input and generates the figure. We only precompute the ASRs for the toll price 
ranges [1,1], [1,2], [1,3] and [1,4] which takes quite large time of computation. The ASRs for the rest of the toll price 
ranges are generated through the below code. The precomputed average success rates are stored in the list, namely
list_precomputed_asr. 
'''

list_precomputed_asr = [[0.43, 0.71, 0.57, 0.33, 0.69, 0.59, 0.74, 0.44, 0.44, 0.35, 0.62, 0.42, 0.38, 0.37, 0.39, 0.74, 0.78, 0.69, 0.8, 0.53, 0.26, 0.53, 0.55, 0.22, 0.32, 0.7, 0.24, 0.3, 0.59, 0.72, 0.58, 0.63, 0.5, 0.43, 0.6, 0.47, 0.23, 0.36, 0.67, 0.65, 0.46, 0.63, 0.2, 0.79, 0.44, 0.57, 0.63, 0.49, 0.41, 0.27], [0.75, 0.36, 0.4, 1.31, 0.93, 0.23, 0.38, 0.41, 0.68, 0.75, 0.47, 0.46, 0.61, 0.72, 0.41, 0.67, 0.4, 0.45, 1.46, 0.71, 0.33, 0.6, 0.54, 0.72, 0.45, 0.68, 0.24, 0.55, 0.45, 0.21, 0.48, 0.99, 1.07, 3.56, 1.39, 0.82, 0.49, 0.33, 0.58, 0.64, 0.43, 0.39, 0.21, 0.16, 0.73, 0.29, 0.61, 0.24, 0.5, 0.65], [1.35, 1.55, 9.23, 6.08, 0.71, 1.43, 1.59, 3.78, 4.69, 2.08, 1.98, 3.05, 3.18, 1.77, 3.1, 1.77, 3.17, 14.83, 3.91, 1.23, 2.92, 2.27, 3.54, 2.57, 3.58, 0.79, 2.76, 1.92, 0.61, 2.09, 7.14, 7.56, 11.98, 11.44, 5.14, 2.25, 1.32, 3.94, 3.37, 1.75, 1.45, 0.56, 0.48, 4.15, 1.01, 3.0, 0.71, 1.62, 3.95, 4.97], [4.24, 26.74, 23.83, 1.66, 4.08, 4.62, 14.72, 16.8, 5.86, 7.24, 10.48, 8.78, 5.86, 10.75, 5.26, 10.84, 34.6, 14.03, 2.81, 9.66, 7.61, 12.03, 5.17, 9.84, 2.0, 9.14, 5.86, 1.55, 6.13, 22.74, 25.0, 31.94, 33.23, 16.63, 7.11, 3.81, 7.75, 13.25, 4.89, 4.06, 1.22, 0.91, 14.36, 2.77, 9.35, 1.6, 7.93, 12.71, 17.35, 37.28]]
list_of_upper_bound_prices = [1, 2, 3, 4]

'''
The loop below generates toll price ranges denoted as [1, upper_bound_price], where the upper_bound_price is at most
equal to max_price.
'''


for upper_bound_price in range(5, max_price + 1, 1):
    logger1.debug("upper_bound_price: " + str(upper_bound_price))
    list_of_upper_bound_prices.append(upper_bound_price)
    counter = counter + 1
    # We repeat the experiment 50 times
    for seed in range(1, 51):
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

plt.savefig("figure6-b.pdf", format="pdf", bbox_inches="tight")
plt.show()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))

