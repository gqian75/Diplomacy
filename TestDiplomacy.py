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
    # ----
    # read
    # ----
    def test_diplomacy_solve1(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Support B")
        w = StringIO()
        diplomacy_solve(r, w)
        self.assertEqual(w.getvalue(), "A [dead]\nB Madrid\nC London\n")

    def test_diplomacy_solve2(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual(w.getvalue(), "A [dead]\nB [dead]\n")

    def test_diplomacy_solve3(self):
        r = StringIO("A Madrid Hold\nB Barcelona Move Madrid\nC London Move Madrid\nD Paris Support B")
        w = StringIO()
        diplomacy_solve(r,w)
        self.assertEqual(w.getvalue(), "A [dead]\nB Madrid\nC [dead]\nD Paris\n")



# ----
# main
# ----

if __name__ == "__main__":
    main()

""" #pragma: no cover
$ coverage run --branch TestDiplomacy.py >  TestDiplomacy.out 2>&1


$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK


$ coverage report -m                   >> TestDiplomacy.out



$ cat TestDiplomacy.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Diplomacy.py          12      0      2      0   100%
TestDiplomacy.py      32      0      0      0   100%
------------------------------------------------------------
TOTAL               44      0      2      0   100%
"""
