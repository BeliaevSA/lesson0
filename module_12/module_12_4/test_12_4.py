from module_12_4 import Runner
import unittest
import logging

logging.basicConfig(
    level=logging.INFO,
    filemode='a',
    filename='runner_tests.log',
    encoding='UTF-8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Test name', -10)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            runner = Runner(77, 20)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)



    def test_challenge(self):
        runner_1 = Runner('Name 1')
        runner_2 = Runner('Name 2')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
