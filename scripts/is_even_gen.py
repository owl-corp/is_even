from pathlib import Path

with Path("is_even/is_even.py").open("w") as f:
    f.write("import random\n\ndef is_even(num: int) -> bool:\n")
    f.write("    if num == 0:\n        return True\n")
    f.writelines(
        [
            f"    if num == {n}:\n        return {n % 2 == 0}\n"
            for n in range(1, 1000000)
        ]
    )
    f.write("    return bool(random.getrandbits(1))\n")
