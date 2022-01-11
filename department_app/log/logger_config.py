"""
This module contains function, which create logger and logger instance
"""
import logging


def create_logger():
    """
    Configuring and returns logger
    """
    logger_instance = logging.getLogger("department_app")
    logger_instance.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler('department_app_logs.log')
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger_instance.addHandler(file_handler)
    return logger_instance


logger = create_logger()
