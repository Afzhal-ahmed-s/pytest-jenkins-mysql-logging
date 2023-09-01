import logging

# Configure the logging settings
log_file_path = 'my_log_file.log'
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, format='%(levelname)s: %(message)s')
#
# # Write log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Read and print the contents of the log file
with open(log_file_path, 'r') as log_file:
    content = log_file.read()
    print(content)
