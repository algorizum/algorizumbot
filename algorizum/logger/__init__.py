import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

fileHandler = logging.FileHandler('./algorizum_log.log')
streamHandler = logging.StreamHandler()

# logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
