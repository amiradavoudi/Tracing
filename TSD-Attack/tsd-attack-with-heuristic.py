from docplex.cp.model import CpoModel
from decimal import *
from sys_logger import sys_log
import math
import time


logfile = 'tsd-attack-with-heuristic.log'
logger1 = sys_log(logfile, 'tsd-attack-with-heuristic', 0)

# This file generates the ASRs and APDS regarding the tsd-attack using the first heuristic (see Table 2)

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
list_lower_wallet = [1, 10, 20, 40]
list_upper_wallet = [10, 20, 40, 60]
list_of_percentage_success_rate_number_of_all_points_freq_sols = []
counter = 0

start = time.time()
for lower_wallet, upper_wallet in zip(list_lower_wallet, list_upper_wallet):
    wallet_range = f"[${lower_wallet}, ${upper_wallet}]"
    logger1.debug("The information about the wallet range " + f"{wallet_range}")
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
    logger1.debug("number of all plausible wallets: " + str(number_of_all_wallets))

    '''
    The below code stores plausible traces in which a trace includes one or two or three toll stations. These traces 
    are stored in dict_wallet_sols_guarantee_at_least_tolls
    '''
    dict_wallet_sols_guarantee_at_least_tolls = {}
    for wallets, list_of_solutions in dict_wallet_sols.items():
        flag = 0
        for sol in list_of_solutions:
            if len(sol) == 1  or len(sol) == 2 or len(sol) == 3:
                flag = 1
                break
        if flag == 1:
            dict_wallet_sols_guarantee_at_least_tolls[wallets] = list_of_solutions.copy()
        else:
            pass

    list_of_updated_wallets = []
    list_of_updated_wallets = list(dict_wallet_sols_guarantee_at_least_tolls.keys())
    logger1.debug("list of plausible wallets: " + str(list_of_updated_wallets))
    # logger1.debug("=======================================")

    list_of_num_of_sols_before_threshold = []
    for wallets, list_of_solutions in dict_wallet_sols_guarantee_at_least_tolls.items():
        list_of_num_of_sols_before_threshold.append(len(list_of_solutions))

    # Given dict_wallet_sols_guarantee_at_least_tolls, we evaluate how threshold impact the AVG success rate.

    list_of_avg_success = []
    list_avg_reduction = []
    list_of_thresholds = []
    legend_list = []
    temp = []
    for threshold in range(3, 10):
        legend_list.append(str(threshold))
        # logger1.debug("threshold: " + str(threshold))
        list_of_thresholds.append(threshold)
        list_of_num_of_sols_after_threshold = []
        for wallets, list_of_solutions in dict_wallet_sols_guarantee_at_least_tolls.items():
            number_of_sols_after_threshold = 0
            for sol in list_of_solutions:
                if len(sol) <= threshold:
                    number_of_sols_after_threshold = number_of_sols_after_threshold + 1
            if number_of_sols_after_threshold == 0:
                temp.append(list_of_solutions)

            list_of_num_of_sols_after_threshold.append(number_of_sols_after_threshold)
        list_of_success_rates = []
        percentage_success_rate_after_threshold = []
        percentage_success_rate_before_threshold = []

        for num_of_sols in list_of_num_of_sols_before_threshold:
            success_rate = 1 / num_of_sols
            success_rate = round(success_rate * 100, 2)
            percentage_success_rate_before_threshold.append(success_rate)
        average_success_rate_before_threshold = sum(percentage_success_rate_before_threshold) / len(percentage_success_rate_before_threshold)
        average_success_rate_before_threshold = round(average_success_rate_before_threshold, 2)

        for num_of_sols in list_of_num_of_sols_after_threshold:
            success_rate = 1 / num_of_sols
            list_of_success_rates.append(success_rate)
            success_rate = round(success_rate * 100, 2)
            percentage_success_rate_after_threshold.append(success_rate)
        average_success_rate = sum(percentage_success_rate_after_threshold) / len(percentage_success_rate_after_threshold)
        average_success_rate = round(average_success_rate, 2)
        # logger1.debug("ASR: " + str(average_success_rate))
        list_of_avg_success.append(average_success_rate)
        list_of_updated_wallets1, percentage_success_rate_after_threshold1 = zip(*sorted(zip(list_of_updated_wallets, percentage_success_rate_after_threshold)))

        list_of_updated_wallets1, list_of_num_of_sols_before_threshold1 = zip(*sorted(zip(list_of_updated_wallets, list_of_num_of_sols_before_threshold)))
        list_of_updated_wallets2, list_of_num_of_sols_after_threshold2 = zip(*sorted(zip(list_of_updated_wallets, list_of_num_of_sols_after_threshold)))

        list_of_reduction = []
        for i, num_of_sol in enumerate(list_of_num_of_sols_before_threshold):
            diff = list_of_num_of_sols_before_threshold1[i] - list_of_num_of_sols_after_threshold2[i]
            reduction = diff / list_of_num_of_sols_before_threshold1[i]
            list_of_reduction.append(reduction)

        avg_reduction = sum(list_of_reduction)/len(list_of_reduction)
        avg_reduction = round(avg_reduction * 100, 2)
        # logger1.debug("APD: " + str(avg_reduction))
        list_avg_reduction.append(avg_reduction)
        # logger1.debug("---------------------------------------------------------------------------------------------")
    logger1.debug("list of thresholds: " + str(list_of_thresholds))
    logger1.debug("list of ASRs: " + str(list_of_avg_success))
    logger1.debug("list of APDs: " + str(list_avg_reduction))
    logger1.debug("---------------------------------------------------------------------------------------------")

end = time.time()
elapsed_time = (end - start)
elapsed_time = round(elapsed_time, 2)
logger1.debug("Execution time in seconds: " + str(elapsed_time))

