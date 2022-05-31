#!/usr/bin/python3
for i in list(
        range(ord('a'), ord('q'))
        ) + list(
                range(ord('r'), ord('z') + 1)
                ):
            print('{:c}'.format(i), end="")
