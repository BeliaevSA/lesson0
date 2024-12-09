from module_12.module_12_1.module_12_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner('Test name')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner('Test name 2')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_1 = Runner('Name 1')
        runner_2 = Runner('Name 2')
        for _ in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)


if __name__ == '__main__':
    unittest.main()
