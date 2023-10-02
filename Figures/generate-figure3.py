from docplex.cp.model import CpoModel
from decimal import *
import matplotlib.pyplot as plt
import math
import time
import os.path
import sys
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(os.path.dirname(os.path.dirname(directory)))
from Tracing.sys_logger import sys_log
logfile = 'figure3.log'
logger1 = sys_log(logfile, 'figure3', 0)

'''
This file generates Figure 3 showing the distribution of all success rates across all plausible wallets within the 
waller range [w_l, w_u]
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


# 2018 toll prices

list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]


'''
The list "list_lower_wallet" takes the lower bounds of the wallet ranges, namely [1, 10], [10, 20], and [20, 40]. 
The list "list_upper_wallet" takes the upper bounds of the mentioned wallet ranges.
'''

list_lower_wallet = [1, 10, 20]
list_upper_wallet = [10, 20, 40]


list_of_percentage_success_rate_number_of_all_points_freq_sols = []
counter = 0
list_of_list_distribution_of_success_rates = []
start = time.time()
for lower_wallet, upper_wallet in zip(list_lower_wallet, list_upper_wallet):
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

    list_of_success_rates = []
    percentage_success_rate_ = []
    for num_of_sols in list_of_num_of_sols:
        success_rate = 1 / num_of_sols
        list_of_success_rates.append(success_rate)
        success_rate = round(success_rate * 100, 2)
        percentage_success_rate_.append(success_rate)

    logger1.debug("---------------------------------------------------------------------------------------------")

    list_of_wallets, percentage_success_rate_ = zip(*sorted(zip(list_of_wallets, percentage_success_rate_)))
    list_of_wallets = list(list_of_wallets)
    percentage_success_rate_ = list(percentage_success_rate_)
    logger1.debug("sorted percentage_success_rate_" + str(percentage_success_rate_))
    list_of_list_distribution_of_success_rates.append(percentage_success_rate_.copy())


# Draw Box graph showing the distribution of success rates

label1 = [1, 2, 3]
list_wallet_range = ['[\$0 ,$10]', '[\$10, $20]', '[\$20, $40]']
len_label1 = len(label1)
fig, ax = plt.subplots()
plt.gcf().subplots_adjust(bottom=0.20)
bp = ax.boxplot(list_of_list_distribution_of_success_rates, patch_artist=True)
plt.xticks(label1, list_wallet_range, rotation=45)
plt.xlabel("Wallet ranges (in dollar)")

plt.ylabel("Success rate (%)")
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
for i in range(len_label1):
    colors.append(col)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.savefig("figure3.png", dpi=600, bbox_inches="tight")

plt.show()

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))