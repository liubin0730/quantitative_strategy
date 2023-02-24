import logging
import logging.config
import unittest

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


class MyTestCase(unittest.TestCase):
    def test_luis(self):
        f = open("a", "w")
        line = f.readline()
        print(line)


if __name__ == '__main__':
    logging.info("wo")
