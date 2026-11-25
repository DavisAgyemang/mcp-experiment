import subprocess
import unittest
from pathlib import Path


class LoopTest(unittest.TestCase):
    def test_prints_one_through_five(self) -> None:
        script = Path(__file__).with_name("loop.js")
        output = subprocess.check_output(["node", script], text=True)
        self.assertEqual(output.splitlines(), ["1", "2", "3", "4", "5"])
