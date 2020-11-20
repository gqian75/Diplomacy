#!/usr/bin/env python3

# -------------------------------
# projects/Diplomacy/TestDiplomacy.py
# Copyright (C) 2016
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_solve

# -----------
# TestDiplomacy
# -----------


class TestDiplomacy (TestCase):
    # Unittests for diplomacy_solve()
    def test_diplomacy_solve1(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(w.getvalue(), "A [dead]\nB Madrid\nC London\n")

    def test_diplomacy_solve2(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(w.getvalue(), "A [dead]\nB [dead]\n")

    def test_diplomacy_solve3(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")

    def test_diplomacy_solve4(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Support B\nD Austin Move London")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD [dead]\n")

    def test_diplomacy_solve5(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B\nE Austin Support A")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB [dead]\nC [dead]\nD Paris\nE Austin\n")

    def test_diplomacy_solve6(self):
        r = StringIO(
            "A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(
            w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")

    def test_diplomacy_solve7(self):
        r = StringIO("A Madrid Move Barcelona")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual(w.getvalue(), "A Barcelona\n")


# ----
# main
# ----
if __name__ == "__main__":
    main()
