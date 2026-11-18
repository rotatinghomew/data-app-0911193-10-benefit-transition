import csv
import unittest
from pathlib import Path


class FixtureShapeTests(unittest.TestCase):
    def test_fixture_files_have_headers_and_records(self):
        fixture_dir = Path(__file__).parents[1] / "fixtures"
        files = list(fixture_dir.glob("*.csv"))
        self.assertGreaterEqual(len(files), 3)
        for path in files:
            with path.open(newline="", encoding="utf-8") as stream:
                rows = list(csv.reader(stream))
            self.assertGreaterEqual(len(rows), 2, path.name)
            self.assertTrue(all(rows[0]), path.name)
            self.assertTrue(all(len(row) == len(rows[0]) for row in rows[1:]), path.name)


if __name__ == "__main__":
    unittest.main()
