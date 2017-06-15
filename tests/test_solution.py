from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        fpath = "./files/testfile.txt"
        solution(fpath)

        with open(fpath, 'r') as f:
            if '\n' in f.read():
                res = True
            else:
                res = False

        self.assertEqual(False, res)