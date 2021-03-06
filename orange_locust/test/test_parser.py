import unittest

from orange_locust.main import parse_options


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser, _, _ = parse_options()

    def test_default(self):
        opts, _ = self.parser.parse_args([])
        self.assertEqual(opts.reset_stats, False)
        self.assertEqual(opts.skip_log_setup, False)

    def test_reset_stats(self):
        args = [
            "--reset-stats"
        ]
        opts, _ = self.parser.parse_args(args)
        self.assertEqual(opts.reset_stats, True)

    def test_should_accept_legacy_no_reset_stats(self):
        args = [
            "--no-reset-stats"
        ]
        opts, _ = self.parser.parse_args(args)
        self.assertEqual(opts.reset_stats, False)

    def test_skip_log_setup(self):
        args = [
            "--skip-log-setup"
        ]
        opts, _ = self.parser.parse_args(args)
        self.assertEqual(opts.skip_log_setup, True)
