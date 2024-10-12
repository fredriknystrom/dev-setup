from flask import has_request_context, request
import logging
import os

def init_logger():
    # Ensure the logs directory exists
    log_directory = "logs"
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    print("init_logger")

    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    class CustomFormatter(logging.Formatter):
        def format(self, record):
            if has_request_context():
                record.url = request.url
            else:
                record.url = None
            return super().format(record)

    # Create a custom formatter object
    logFormatter = CustomFormatter("%(levelname)s:%(name)s:%(message)s")

    # Add console handler to the root logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    # Add file handler to the root logger
    fileHandler = logging.FileHandler(os.path.join(log_directory, "1.log"))
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    return logger