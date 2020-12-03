import unittest
from algorithms.greedy_scheduling import greedy_sheduling
from algorithms.greedy_scheduling import diff, ratio

class TestGreedySchedule(unittest.TestCase):
    def test_case(self):
        with open('tests/problem13.4test.txt', 'r') as f:
            n = int(f.readline())
            jobs = []
            for i in range(n):
                w, l = f.readline().strip().split()
                jobs.append((int(w), int(l)))

            self.assertEqual(greedy_sheduling(jobs, diff), 68615)
            self.assertEqual(greedy_sheduling(jobs, ratio), 67247)

