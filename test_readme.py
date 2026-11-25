import unittest
from pathlib import Path


class ReadmeTest(unittest.TestCase):
    def test_introduces_mcp(self) -> None:
        readme = Path(__file__).with_name("README.md").read_text(encoding="utf-8")
        self.assertIn("Model Context Protocol", readme)
