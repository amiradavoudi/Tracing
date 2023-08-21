from docplex.cp.model import CpoModel
from decimal import *
import math

'''
generates all plausible trace within the range [w_l, w_u], written to the file "plausible_traces.txt"
'''

def create_list_of_all_sols_cycle_type_freq(len_of_price_, q_, all_sols):
    list_of_all_sols = []
    one_solution = []
    dict_wallet_sols = {}
    for sol in all_sols:
        wallet = 0
        for i in range(len_of_price_):
            if sol[q_[i]] != 0:
                tuple_index_sol_value = (str(i), sol[q_[i]])
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


def create_model(list_of_cycle_price, billing_period_, lower_wallet_, upper_wallet_):
    imodel_ = CpoModel(name='test')
    length = len(list_of_cycle_price)
    num_of_variables = range(length)
    q = imodel_.integer_var_dict(num_of_variables)

    '''
    Add constraints for each variable in the linear equation
    '''
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


'''
2018 toll prices
'''

lower_bound_wallet = 0
upper_bound_wallet = 10
list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]

length_of_toll_prices = len(list_of_toll_price)
max_frq = math.ceil(upper_bound_wallet / min(list_of_toll_price))
billing_period_ = max_frq
imodel, q = create_model(list_of_toll_price, billing_period_, lower_bound_wallet, upper_bound_wallet)
imodel.print_information()
all_sols = imodel.start_search()
dict_wallet_sols = create_list_of_all_sols_cycle_type_freq(length_of_toll_prices, q, all_sols)

'''
Open the file plausible_traces.txt in the default path
'''

file1 = open("plausible_traces.txt", "w")
for wallets, list_of_traces in dict_wallet_sols.items():
    list_of_plausible_traces = []

    '''
    Write the plausible trace corresponding to a wallet balance in the following format:
    Example: [['s_1', f_1], ['s_2', f_2], ..., ['s_l', f_l]]
    The list of plausible traces of each individual wallet balance is seperated by a semicolon 
    in the file plausible_traces.txt.
    '''

    for trace in list_of_traces:
        list_of_traces = []
        for tuple_ in trace:
            list_format_tuple = list(tuple_)
            list_of_traces.append(list_format_tuple)
        list_of_plausible_traces.append(list_of_traces.copy())

    '''
    string_format_list_of_plausible_traces stores the set of plausible traces (correct format) for all wallets
    '''

    string_format_list_of_plausible_traces = str(list_of_plausible_traces)
    file1.write(string_format_list_of_plausible_traces + ";")
file1.close()

