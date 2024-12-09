import unittest
from module_12.module_12_2.module_12_2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_forzen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner('Усейн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)


    @unittest.skipIf(is_forzen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        finishers = tournament.start()
        self.all_results.update(tournament_1=finishers)
        last_place = max(list(finishers.keys()))
        self.assertTrue(finishers[last_place] == 'Ник')


    @unittest.skipIf(is_forzen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        finishers = tournament.start()
        self.all_results.update(tournament_2=finishers)
        last_place = max(list(finishers.keys()))
        self.assertTrue(finishers[last_place] == 'Ник')


    @unittest.skipIf(is_forzen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        finishers = tournament.start()
        self.all_results.update(tournament_3=finishers)
        last_place = max(list(finishers.keys()))
        self.assertTrue(finishers[last_place] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)


if __name__ == '__main__':
    unittest.main()