import logging

# we need to create an object that we will use to create logs - an obj that is responsible for logging everything.

def test_loggingDemo():
    logger = logging.getLogger(__name__)

# to define the file for logging and format - use addhandler or filehandler object

    fileHandler = logging.FileHandler('Logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)

    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Alert warning mode")
    logger.error("A major error happened")
    logger.critical("critical issue, system will stop execution")
