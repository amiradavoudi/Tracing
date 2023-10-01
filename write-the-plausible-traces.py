from docplex.cp.model import CpoModel
from decimal import *
import math
import subprocess
import shutil
import os


'''
This file generates all plausible trace within the range [w_l, w_u], written to the file "plausible_traces.txt". By 
running the file the results will be written to the *cd-attack.log* file. The results show the average success rate
(ASR) w.r.t the wallet ranges: [0, 10], [10, 20], [20, 40].
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
    if lower_wallet_ == 0:
        lower_wallet_ = lower_wallet_ + 1
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

# 2018 toll prices


list_lower_wallet = [0, 10, 20]
list_upper_wallet = [10, 20, 40]


for lower_bound_wallet, upper_bound_wallet in zip(list_lower_wallet, list_upper_wallet):
    wallet_range = [lower_bound_wallet, upper_bound_wallet]
    str_folder_name = "Wallet-range" + str(wallet_range)

    list_of_toll_price = [4.55, 2.68, 2.84, 1.72, 4.09, 5.46, 5.11, 5.11, 3.19]
    length_of_toll_prices = len(list_of_toll_price)
    max_frq = math.ceil(upper_bound_wallet / min(list_of_toll_price))
    billing_period_ = max_frq
    imodel, q = create_model(list_of_toll_price, billing_period_, lower_bound_wallet, upper_bound_wallet)
    imodel.print_information()
    all_sols = imodel.start_search()
    dict_wallet_sols = create_list_of_all_plausible_traces(length_of_toll_prices, q, all_sols)

    # Open the file plausible_traces.txt in the default path
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

    # ===============================================
    # We specify the JavaScript file that we want to run
    js_file = "create_partitions.js"

    try:
        subprocess.run(["node", js_file], check=True)
        print(f"Successfully executed {js_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {js_file}. Error code:", e.returncode)

    # ===============================================
    # We specify the Python file that we want to run
    py_file = "cd-attack.py"

    try:
        subprocess.run(["python", py_file], check=True)
        print(f"Successfully executed {py_file}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute {py_file}. Error code:", e.returncode)

    '''
    The generated files plausible_traces.txt, partitions.txt , and distribution-SR.txt will be saved to subfolders in 
    the folder 'CD-attack-data'. File 'plausible_traces.txt' includes all plausible traces,  file 'partitions.txt' 
    includes all partitions, and file 'distribution-SR.txt' includes all success rates. These files are generated w.r.t 
    the wallet range [w_l, w_u]. 
    '''

    file_path = os.getcwd()
    dest_dir = f"CD-attack-data\\{str_folder_name}"

    src_path = os.path.join(file_path, "plausible_traces.txt")
    dst_path = os.path.join(file_path, dest_dir, "plausible_traces.txt")
    shutil.move(src_path, dst_path)

    src_path = os.path.join(file_path, "partitions.txt")
    dst_path = os.path.join(file_path, dest_dir, "partitions.txt")
    shutil.move(src_path, dst_path)

    src_path = os.path.join(file_path, "distribution-SR.txt")
    dst_path = os.path.join(file_path, dest_dir, "distribution-SR.txt")
    shutil.move(src_path, dst_path)