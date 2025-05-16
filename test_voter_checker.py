import unittest
from voter_checker import is_eligible_to_vote


class TestVoterEligibility(unittest.TestCase):

    def test_valid_voter(self):
        self.assertTrue(is_eligible_to_vote(18, True))

    def test_underage_voter(self):
        self.assertFalse(is_eligible_to_vote(17, True))

    def test_non_citizen_voter(self):
        self.assertFalse(is_eligible_to_vote(25, False))

    def test_underage_non_citizen_voter(self):
        self.assertFalse(is_eligible_to_vote(16, False))

    def test_exactly_18_and_non_citizen(self):
        self.assertFalse(is_eligible_to_vote(18, False))

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            is_eligible_to_vote(-5, True)


if __name__=="__main__":  # type: ignore
    unittest.main () 
    