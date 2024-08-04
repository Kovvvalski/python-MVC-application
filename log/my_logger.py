import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler('log.log')

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)
