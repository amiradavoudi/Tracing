from sys_logger import sys_log

logfile = 'cd-attack.log'
logger1 = sys_log(logfile, 'cd-attack', 0)

'''
This file computes the ASR of the cd-attack based on the partitions written to the file "partitions.txt" 
(generated by create_partitions.js).
'''

def compute_avg_succ_rate():
    file1 = open('partitions.txt', 'r')
    file2 = open('distribution-SR.txt', 'w')
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

    # The list of success rates will be written to distribution-SR.txt file.
    str_list_of_prob = str(list_of_prob)
    file2.write(str_list_of_prob)
    file2.close()

    avg_prob = sum(list_of_prob) / len(list_of_prob)
    avg_prob = round(avg_prob, 2)
    return avg_prob, list_of_prob

# The average success rate (ASR) of the cd attack will be written to 'distribution-SR.txt' file


ASR, list_of_prob_ = compute_avg_succ_rate()
logger1.debug("average success rate: " + f"{ASR}")

