import logging
import os


current_dir_path = os.path.dirname(os.path.realpath(__file__))


def sys_log(log_file_name, logger_name, flag):

    log_file_path = os.path.join(current_dir_path, log_file_name)

    if not os.path.exists(log_file_path):
        with open(log_file_name, "a"):
            pass
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)

    if flag:
        logger.disabled = True
    return logger



