import logging

logging.basicConfig(filename="./log/debug.log", level=logging.DEBUG)

logging.debug("DEBUG_TEST")
logging.info("INFO_TEST")
logging.warning("WARNING_TEST")
logging.error("ERROR_TEST")
logging.critical("CRITICAL_TEST")
