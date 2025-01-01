# SPDX-License-Identifier: ISC
# SPDX-FileCopyrightText: 2025 kurth4cker <kurth4cker@gmail.com>

from pytest import skip
from shapes import sand_clock

def test_sand_clock():
    assert sand_clock(3) == [
        [1, 2, 3],
        [2, 3],
        [3],
        [2, 3],
        [1, 2, 3],
    ]

def test_crown():
    skip("NOT IMPLEMENTED")

def test_is_armstrong():
    skip("NOT IMPLEMENTED")

def test_digitate():
    # assert digitate([23, 432, 1]) == [
    #     (2, 3),
    #     (4, 3, 2),
    #     (1, ),
    # ]
    skip("NOT IMPLEMENTED")

def test_reversed_diamond():
    # assert reversed_diamond(5) == """
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# """
    skip("NOT IMPLEMENTED")

def test_char_diamond():
    # assert char_diamond('F') == """
    #  A
    # B B
   # C   C
  # D     D
 # E       E
# F         F
 # E       E
  # D     D
   # C   C
    # B B
    #  A
# """
    skip("NOT IMPLEMENTED")
