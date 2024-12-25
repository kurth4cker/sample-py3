# SPDX-License-Identifier: ISC
# SPDX-FileCopyrightText: 2024 kurth4cker <kurth4cker@gmail.com>

num = int(input("Bir sayı giriniz: "))
if num < 1:
    raise ValueError(f'{num} pozitif değil')

divider = 2
dividers = set()

while num != 1:
    if num % divider == 0:
        dividers.add(divider)
        num //= divider
    else:
        divider += 1

print(f'{num} sayısının tam bölenleri:', *dividers)
