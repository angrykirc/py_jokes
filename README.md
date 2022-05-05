# Small, but funny programs in Python
* **obfuscator.py** -- obfuscates any given string by inserting random characters in given intervals, the resulting string can be reverted to its original form then by using Python slices.
* **rotation.py** -- simple and insecure rotational "cipher", akin to ROT-13.
* **rotation_xt.py** -- more advanced variation of the previous code, with custom alphabet which includes cyrillic characters, and longer key (0x0-0xFFF), which is implemented by dividing the actual key in two which are then used in parallel. Also not really secure.