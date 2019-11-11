import unittest

from parameterized import parameterized

from src.needleman_wunsch_solver import NeedlemanWunschSolver, CellCostComputer


class AlignmentPathsTests(unittest.TestCase):

    def setUp(self):
        self.solver = NeedlemanWunschSolver(CellCostComputer(
            same_cost=5,
            diff_cost=-5,
            gap_penalty=-2
        ))

    @parameterized.expand([
        [
            0,
            {("", "")},
            "", ""
        ],
        [
            5,
            {("A", "A")},
            "A", "A"
        ],
        [
            3,
            {("AA", "A-"), ("AA", "-A")},
            "AA", "A"
        ],
        [
            1,
            {("A-S", "AA-"), ("-AS", "AA-"), ("AS-", "A-A")},
            "AS", "AA"
        ],
        [
            -3,
            {("AAA-D", "--AS-"),
             ("A-AAD", "AS---"),
             ("AA-AD", "A-S--"),
             ("AAA-D", "A--S-"),
             ("AA-AD", "-AS--"),
             ("AAAD-", "A---S"),
             ("AAAD-", "--A-S"),
             ("AAAD-", "-A--S"),
             ("AAA-D", "-A-S-")},
            "AAAD", "AS"
        ],
        [
            -8,
            {("----", "AAAD")},
            "", "AAAD"
        ],
        [
            -10,
            {("AAAD-", "----S"),
             ("AA-AD", "--S--"),
             ("AAA-D", "---S-"),
             ("-AAAD", "S----"),
             ("A-AAD", "-S---")},
            "AAAD", "S"
        ],
        [
            6,
            {("ABCD", "A--D")},
            "ABCD", "AD"
        ]
    ])
    def test(self, expected_score, expected_alignments, seq_a, seq_b):
        score, alignment = self.solver.generate_alignments(a_seq=seq_a, b_seq=seq_b)
        self.assertSetEqual(alignment, expected_alignments)
        self.assertEqual(score, expected_score)
