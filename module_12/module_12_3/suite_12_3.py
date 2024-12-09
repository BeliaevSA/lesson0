import unittest
from tests_runner import RunnerTest
from tests_tournament import TournamentTest

all_testST = unittest.TestSuite()
all_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
all_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(all_testST)
