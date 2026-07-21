import pandas as pd
import unittest
from cleaning.missing import missing_value_report, fill_missing


class TestMissing(unittest.TestCase):
    def test_fill_missing_median(self):
        df = pd.DataFrame({"a": [1, 2, None, 4]})
        result = fill_missing(df, strategy="median")
        self.assertFalse(result["a"].isnull().any())

    def test_missing_value_report(self):
        df = pd.DataFrame({"a": [1, None, 3], "b": [1, 2, 3]})
        report = missing_value_report(df)
        self.assertIn("a", report.index)
        self.assertNotIn("b", report.index)


if __name__ == "__main__":
    unittest.main()
