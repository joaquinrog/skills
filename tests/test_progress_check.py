"""Tests for skills/progress/scripts/progress_check.py (stdlib only: python3 -m unittest)."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "skills/progress/scripts/progress_check.py"
OK = f"{sys.executable} -c pass"
FAIL = f"{sys.executable} -c 'raise SystemExit(1)'"
SKIPS = f"{sys.executable} -c 'print(\"3 passed, 1 skipped\")'"


def story(key, state, verify, **extra):
    return {"key": key, "title": key, "state": state, "verify": verify, **extra}


class ProgressCheck(unittest.TestCase):
    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        self.file = self.dir / "progress.json"

    def write(self, stories):
        self.file.write_text(json.dumps({"name": "demo", "stories": stories}), encoding="utf-8")

    def run_check(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args, str(self.file)],
            cwd=self.dir, capture_output=True, text=True, check=False,
        )

    def stories(self):
        return {s["key"]: s for s in json.loads(self.file.read_text())["stories"]}

    def test_a_passing_verify_writes_passes_true_with_date(self):
        self.write([story("A-1", "in_progress", [OK])])
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stderr)
        s = self.stories()["A-1"]
        self.assertIs(s["passes"], True)
        self.assertTrue(s["verified_at"].endswith("Z"))

    def test_a_story_passes_only_if_every_command_passes(self):
        self.write([story("A-1", "in_progress", [OK, FAIL])])
        self.run_check()
        self.assertIs(self.stories()["A-1"]["passes"], False)

    def test_a_skipped_test_does_not_count_as_passing(self):
        self.write([story("A-1", "in_progress", [SKIPS])])
        self.run_check()
        self.assertIs(self.stories()["A-1"]["passes"], False)

    def test_a_failing_story_in_review_or_done_fails_the_check(self):
        self.write([story("A-1", "review", [FAIL]), story("A-2", "in_progress", [FAIL])])
        result = self.run_check()
        self.assertEqual(result.returncode, 1)
        self.assertIn("A-1", result.stdout)
        self.assertNotIn("A-2 ", result.stdout.split("bloquean")[-1])

    def test_a_failing_story_in_progress_is_recorded_but_does_not_block(self):
        self.write([story("A-1", "in_progress", [FAIL])])
        self.assertEqual(self.run_check().returncode, 0)
        self.assertIs(self.stories()["A-1"]["passes"], False)

    def test_a_story_without_verify_is_left_alone(self):
        self.write([story("A-1", "not_started", [], note="keep me")])
        self.run_check()
        s = self.stories()["A-1"]
        self.assertNotIn("passes", s)
        self.assertEqual(s["note"], "keep me")

    def test_a_hand_written_passes_is_overwritten(self):
        self.write([story("A-1", "done", [FAIL], passes=True)])
        self.run_check()
        self.assertIs(self.stories()["A-1"]["passes"], False)

    def test_dry_run_reports_but_does_not_write(self):
        self.write([story("A-1", "in_progress", [OK])])
        before = self.file.read_text()
        self.run_check("--dry-run")
        self.assertEqual(self.file.read_text(), before)

    def test_unknown_fields_are_kept(self):
        self.write([story("A-1", "in_progress", [OK], jira="EX-9")])
        self.run_check()
        self.assertEqual(self.stories()["A-1"]["jira"], "EX-9")


if __name__ == "__main__":
    unittest.main()
