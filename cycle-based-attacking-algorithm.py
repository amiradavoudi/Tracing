from sys_logger import sys_log

'''
The toll-based-attacking algorithm
'''

logfile = 'cycle-based-algo.log'
logger1 = sys_log(logfile, 'cycle-based-algo', 0)


'''
File cycle-based-attacking-algorithm.py computes the ASR based on the partitions written to the file "partitions.txt".
'''


def compute_avg_succ_rate():
    # Opening file
    file1 = open('partitions.txt', 'r')
    all_number_of_plausible_cycles = file1.read().splitlines()
    file1.close()
    list_of_prob = []
    for num_plaus_cycles in all_number_of_plausible_cycles:
        list_num_plaus_cycles = num_plaus_cycles.split(',')
        print(list_num_plaus_cycles)
        length_plaus_trace = len(list_num_plaus_cycles)
        probability = 0
        for num_cycle in list_num_plaus_cycles:
            a = (1 / length_plaus_trace)
            b = (1 / int(num_cycle))
            probability = probability + a * a * b

        probability = round(probability * 100, 2)
        list_of_prob.append(probability)
    print("list of probability is: {}".format(list_of_prob))
    avg_prob = sum(list_of_prob) / len(list_of_prob)
    avg_prob = round(avg_prob, 2)
    return avg_prob, list_of_prob


ASR, list_of_prob_ = compute_avg_succ_rate()
logger1.debug("average success rate: " + f"{ASR}")
# f = open("distribution-SR.txt", "a")
# str_list_of_prob = str(list_of_prob)
# f.write(str_list_of_prob + "\n")
# f.close()
# print("avg_prob is: {}".format(ASR))