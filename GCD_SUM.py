import re
from math import gcd
from functools import reduce


def parse_line(line: str) -> list[int] | None:
    """
    Returns list of 3 ints if line is valid, else None.
    Valid separators: single/multiple spaces, comma, comma+space.
    No extra characters permitted.
    """
    # Strip trailing whitespace only; leading spaces = invalid
    stripped = line.strip()

    # Split on valid separators: commas (with optional space) or spaces
    parts = re.split(r',\s*|\s+', stripped)

    # Must be exactly 3 parts
    if len(parts) != 3:
        return None

    # Each part must be a bare integer (optional leading minus, digits only)
    integers = []
    for part in parts:
        if not re.fullmatch(r'-?\d+', part):
            return None
        integers.append(int(part))

    return integers


def compute_gcd(nums: list[int]) -> int:
    return reduce(gcd, map(abs, nums))


def process_telemetry(stream: str) -> int:
    total = 0
    for line in stream.strip().splitlines():
        parsed = parse_line(line)
        if parsed is not None:
            total += compute_gcd(parsed)
    return total


# --- Sample input ---
sample = """18 24 30 
7,14,21 
9, 27, 81 
100 200 300 
5 10 
8,16,24,32 
-12 -18 -24 
11, 22, abc 
0 0 5"""

print(process_telemetry(sample))  # Expected: 9