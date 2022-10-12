import logging

formatter = logging.Formatter(
    fmt='[%(levelname)s] %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger("root")
logger.addHandler(handler)
