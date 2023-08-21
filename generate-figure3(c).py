from docplex.cp.model import CpoModel
from decimal import *
from sys_logger import sys_log
import matplotlib.pyplot as plt
import numpy as np
import math
import random
import time

logfile = 'figure3(c).log'
logger1 = sys_log(logfile, 'figure3(c)', 0)


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


def create_model(list_of_cycle_price, billing_period_, wallet_):
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
    imodel.add_constraint(imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables) <= wallet_)
    imodel.add_constraint(20 < imodel.sum(q[i] * list_of_cycle_price[i] for i in num_of_variables))
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


def create_random_toll_price(low_val, high_val, number_of_toll_prices_, seed_):
    random.seed(seed_)
    list_of_random_toll_price = []
    for i in range(0, number_of_toll_prices_):
        list_of_random_toll_price.append(generate_flat_rand_num(low_val, high_val))
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
for upper_bound_price in range(1, max_price + 1, 1):
    logger1.debug("upper_bound_price: " + str(upper_bound_price))
    list_of_upper_bound_prices.append(upper_bound_price)
    counter = counter + 1
    for seed in range(1, 51):
        list_of_toll_price = create_random_toll_price(min_price, upper_bound_price, number_of_toll_prices, seed + counter)

        max_frq = math.ceil(wallet_ / min(list_of_toll_price))
        billing_period_ = max_frq
        logger1.debug("billing_period_: " + str(billing_period_))
        logger1.debug("list_of_toll_price: " + str(list_of_toll_price))
        length_of_toll_prices = len(list_of_toll_price)
        imodel, q = create_model(list_of_toll_price, billing_period_, wallet_)
        imodel.print_information()
        all_sols = imodel.start_search()

        dict_wallet_sols = create_list_of_all_sols_cycle_type_freq(length_of_toll_prices, q, all_sols)
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
bp = ax.boxplot(list_of_list_of_avg_success_rates, patch_artist=True)
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

plt.show()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))