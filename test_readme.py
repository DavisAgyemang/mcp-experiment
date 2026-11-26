from pathlib import Path
from unittest import TestCase


class ReadmeTest(TestCase):
    def test_documents_mcp_announcement_date(self) -> None:
        readme = Path(__file__).with_name("README.md").read_text(encoding="utf-8")
        self.assertIn("November 25, 2024", readme)
