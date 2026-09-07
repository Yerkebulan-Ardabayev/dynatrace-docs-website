#!/usr/bin/env python3
"""Regression tests for the reversible subscription-provider switch."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS_DIR))

import translate_docs_groq as translator


class TranslateProviderTest(unittest.TestCase):
    def setUp(self) -> None:
        self.provider = translator.AI_TRANSLATE_PROVIDER
        self.codex_available = translator.codex_available
        self.claude_available = translator.claude_available
        self.subprocess_run = translator.subprocess.run
        self.claude_translate = translator.translate_via_claude_cli

    def tearDown(self) -> None:
        translator.AI_TRANSLATE_PROVIDER = self.provider
        translator.codex_available = self.codex_available
        translator.claude_available = self.claude_available
        translator.subprocess.run = self.subprocess_run
        translator.translate_via_claude_cli = self.claude_translate

    def test_codex_route_reads_last_message_file(self) -> None:
        seen: dict[str, object] = {}

        def fake_run(command: list[str], **kwargs: object) -> object:
            seen["command"] = command
            seen["prompt"] = kwargs["input"]
            output_path = Path(command[command.index("--output-last-message") + 1])
            output_path.write_text("Тестовый перевод", encoding="utf-8")
            return type("Result", (), {"returncode": 0, "stdout": "", "stderr": ""})()

        translator.codex_available = lambda: True
        translator.subprocess.run = fake_run

        result = translator.translate_via_codex_cli("Hello", "Сохрани структуру")

        self.assertEqual(result, "Тестовый перевод")
        command = seen["command"]
        self.assertIn("--output-last-message", command)
        self.assertIn("--ignore-user-config", command)
        self.assertIn("--ignore-rules", command)
        self.assertIn("Сохрани структуру", seen["prompt"])

    def test_claude_route_remains_selectable(self) -> None:
        translator.AI_TRANSLATE_PROVIDER = "claude"
        translator.claude_available = lambda: True
        translator.translate_via_claude_cli = lambda text, rules: f"claude:{text}:{rules}"

        self.assertTrue(translator.primary_available())
        self.assertEqual(translator.primary_model(), translator.CLAUDE_MODEL)
        self.assertEqual(
            translator.translate_via_primary_cli("source", "rule"),
            "claude:source:rule",
        )


if __name__ == "__main__":
    unittest.main()
