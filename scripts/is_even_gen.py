from random import shuffle

from pathlib import Path

with Path("is_even/is_even.py").open("w") as f:
    f.write("import ast\nimport random\n\n")
    f.write("# No magic numbers\nTRUE='True'\nFALSE='False'\n\n")
    f.write("INTERPRET = ast.literal_eval\n")
    f.write("IS_EVEN_BOOL = bool\n\n\n")
    f.write("def is_even(num: int) -> IS_EVEN_BOOL:\n")
    nums = list(range(1_000_000))
    shuffle(nums)
    f.writelines(
        [
            f"    if num == {n}:\n        return INTERPRET({'TRUE' if n % 2 == 0 else 'FALSE'})\n"
            for n in nums
        ]
    )
    f.write("    return bool(random.getrandbits(1))\n")
