from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from scripts.check_local_links import find_broken_links


class LocalLinkCheckTests(TestCase):
    def test_accepts_existing_external_and_fragment_links(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Guide](docs/guide.md) [Section](#section) "
                "[Website](https://example.org/resource)\n",
                encoding="utf-8",
            )

            self.assertEqual(find_broken_links(root), [])

    def test_reports_missing_target(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[Missing](docs/missing.md)\n", encoding="utf-8"
            )

            self.assertEqual(
                find_broken_links(root),
                ["README.md: missing target: docs/missing.md"],
            )

    def test_checks_reference_style_links(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "Read the [guide][guide].\n\n[guide]: docs/guide.md\n",
                encoding="utf-8",
            )

            self.assertEqual(
                find_broken_links(root),
                ["README.md: missing target: docs/guide.md"],
            )

    def test_rejects_path_outside_repository(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text(
                "[Outside](../outside.md)\n", encoding="utf-8"
            )

            self.assertEqual(
                find_broken_links(root),
                ["README.md: link escapes repository: ../outside.md"],
            )
