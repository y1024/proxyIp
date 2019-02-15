import logging


class Logger:
    def __init__(self, filename):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler('/data/log/%s' % filename, mode='w')
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(
            logging.Formatter(
                fmt='%(asctime)s %(levelname)s:%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
        )
        self.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(
            logging.Formatter(
                fmt='%(asctime)s %(levelname)s:%(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
        )
        self.logger.addHandler(console_handler)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)
