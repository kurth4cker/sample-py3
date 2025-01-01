# SPDX-License-Identifier: ISC
# SPDX-FileCopyrightText: 2025 kurth4cker <kurth4cker@gmail.com>

def sand_clock(number):
    result = []
    for i in range(1, number + 1):
        result.append(list(range(i, number + 1)))

    for i in range(number - 1, 0, -1):
        result.append(list(range(i, number + 1)))

    return result
