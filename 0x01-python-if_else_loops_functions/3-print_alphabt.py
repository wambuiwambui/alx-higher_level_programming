#!/usr/bin/python3
ans = ""
for character in range(97, 123):
    if character != 101 and character != 113:
        ans += "{:c}".format(character)
print(ans, end="")
