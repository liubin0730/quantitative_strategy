import logging
import logging.config
import unittest

logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


class MyTestCase(unittest.TestCase):
    def test_luis(self):
        f = open("./price", "w", encoding='utf-8')
        # line = f.readline()
        # print(line)

        f.write("0.9")
        f.close()

if __name__ == '__main__':
    logging.info("wo")
