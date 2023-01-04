#!/usr/bin/python3
for i in range(97,123):
	if i == 101:
		i += 1
		continue

	if i == 113:
		i += 1
		continue

	print(("{}".format(chr(i)), end="")
