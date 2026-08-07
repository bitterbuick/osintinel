# tests/test_cli.py
"""Smoke tests: the CLI must load and every subcommand must be reachable
without the optional third-party packages installed."""

import importlib
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

from src.cli.cli import build_parser, main

EXPECTED_COMMANDS = {
    "dns", "geo", "emails", "whois",
    "twitter", "darkweb", "linkedin", "github",
}


class TestParser(unittest.TestCase):
    def test_every_command_is_registered(self):
        subparsers = build_parser()._subparsers._group_actions[0]
        self.assertEqual(set(subparsers.choices), EXPECTED_COMMANDS)

    def test_no_args_prints_help_and_exits_clean(self):
        self.assertEqual(main([]), 0)

    def test_help_does_not_import_optional_packages(self):
        with self.assertRaises(SystemExit) as cm:
            build_parser().parse_args(["--help"])
        self.assertEqual(cm.exception.code, 0)


class TestModulesImportable(unittest.TestCase):
    """Modules with no optional dependencies must always import — this is the
    check that would have caught the missing github_scraper module."""

    ALWAYS_IMPORTABLE = [
        "src.modules.dns_lookup",
        "src.modules.ip_geolocation",
        "src.modules.web_request",
        "src.modules.email_extractor",
        "src.modules.dark_web_monitor",
        "src.modules.github_scraper",
        "src.config",
    ]

    def test_core_modules_import(self):
        for name in self.ALWAYS_IMPORTABLE:
            with self.subTest(module=name):
                importlib.import_module(name)

    def test_cli_references_only_existing_modules(self):
        """Every src.modules.* import in cli.py must resolve to a real file."""
        import re

        cli_path = os.path.join(os.path.dirname(__file__), os.pardir, "src", "cli", "cli.py")
        with open(cli_path) as fh:
            referenced = set(re.findall(r"from (src\.modules\.\w+) import", fh.read()))

        self.assertTrue(referenced, "expected cli.py to import some modules")
        for name in referenced:
            with self.subTest(module=name):
                path = os.path.join(
                    os.path.dirname(__file__), os.pardir,
                    *name.split(".")[:-1], name.split(".")[-1] + ".py",
                )
                self.assertTrue(os.path.exists(path), f"{name} is imported but {path} does not exist")


class TestEmailExtractor(unittest.TestCase):
    def test_extracts_addresses(self):
        from src.modules.email_extractor import EmailExtractor

        html = "<p>Contact info@example.com or support@example.org</p>"
        self.assertEqual(
            EmailExtractor.extract_emails(html),
            ["info@example.com", "support@example.org"],
        )

    def test_returns_empty_when_none_present(self):
        from src.modules.email_extractor import EmailExtractor

        self.assertEqual(EmailExtractor.extract_emails("<p>nothing here</p>"), [])


if __name__ == "__main__":
    unittest.main()
