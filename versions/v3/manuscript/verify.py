"""Independent exact checks for the A378495 difference note, Python 3.10+."""

import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path


MAXIMUM_SIZE = 80
ENUMERATION_MAXIMUM = 9


def cycle_lengths(permutation):
    visited = [False] * len(permutation)
    lengths = []
    for start in range(len(permutation)):
        if visited[start]:
            continue
        current = start
        length = 0
        while not visited[current]:
            visited[current] = True
            current = permutation[current]
            length += 1
        lengths.append(length)
    return lengths


def recurrence_column(forbidden, maximum):
    counts = [1] + [0] * maximum
    for size in range(1, maximum + 1):
        counts[size] = sum(
            math.comb(size - 1, length - 1)
            * math.factorial(length - 1)
            * counts[size - length]
            for length in range(2, size + 1)
            if length != forbidden
        )
    return counts


def sequence_b(index):
    return Fraction((-1) ** index * math.factorial(index + 3), 2 * (index + 1))


def run_checks():
    columns = {
        forbidden: recurrence_column(forbidden, MAXIMUM_SIZE)
        for forbidden in range(2, MAXIMUM_SIZE + 1)
    }
    derangements = recurrence_column(None, MAXIMUM_SIZE)
    enumeration_total = 0
    enumeration_rows = {}
    for size in range(1, ENUMERATION_MAXIMUM + 1):
        counts = [0] * (size + 1)
        for permutation in itertools.permutations(range(size)):
            enumeration_total += 1
            lengths = cycle_lengths(permutation)
            if 1 in lengths:
                continue
            for forbidden in range(2, size + 1):
                if forbidden not in lengths:
                    counts[forbidden] += 1
        enumeration_rows[str(size)] = counts[1:]
        for forbidden in range(2, size + 1):
            assert counts[forbidden] == columns[forbidden][size]
    assert enumeration_rows['4'] == [0, 6, 9, 3]
    assert enumeration_rows['5'] == [0, 24, 24, 44, 20]
    original_failures = []
    long_cycle_checks = 0
    for size in range(3, MAXIMUM_SIZE + 1):
        row = [0] + [columns[forbidden][size] for forbidden in range(2, size + 1)]
        assert math.gcd(*row) == size - 1
        assert all(value % (size - 1) == 0 for value in row)
        for forbidden in range(2, size + 1):
            if 2 * forbidden > size:
                excluded = (
                    math.comb(size, forbidden)
                    * math.factorial(forbidden - 1)
                    * derangements[size - forbidden]
                )
                assert derangements[size] - columns[forbidden][size] == excluded
                long_cycle_checks += 1
        if size >= 5:
            adjacent = columns[size - 1][size] - columns[size - 2][size]
            terminal = columns[size - 2][size] - columns[size][size]
            assert adjacent == Fraction(math.factorial(size), 2 * (size - 2))
            assert adjacent == abs(sequence_b(size - 3))
            assert terminal == Fraction(math.factorial(size - 3) * (size - 4) * (size - 1), 2)
            assert adjacent != abs(sequence_b(size - 4))
            original_failures.append(size)
    assert columns[3][4] - columns[2][4] == abs(sequence_b(0)) == 3
    assert columns[2][4] - columns[4][4] == 3
    assert columns[4][5] - columns[3][5] == 20
    assert abs(sequence_b(1)) == 6
    certificate = {
        'schema_version': 1,
        'status': 'all assertions passed',
        'methods': ['exhaustive permutation enumeration', 'last-label cycle recurrence'],
        'enumeration_range': [1, ENUMERATION_MAXIMUM],
        'permutations_enumerated': enumeration_total,
        'recurrence_range': [0, MAXIMUM_SIZE],
        'difference_formula_range': [5, MAXIMUM_SIZE],
        'row_gcd_range': [3, MAXIMUM_SIZE],
        'long_cycle_instances_checked': long_cycle_checks,
        'literal_adjacent_conjecture_fails_at_every_checked_size': original_failures,
        'first_column_convention': 'T(n,1)=0 as displayed in OEIS, not literal cycle avoidance',
        'enumeration_rows': enumeration_rows,
        'counterexample': {'size': 5, 'T(5,3)': 24, 'T(5,4)': 44, 'actual': 20, 'conjectured': 6},
        'scope': 'Exact finite checks: permutation enumeration through n=9; cycle recurrence through n=80. Unbounded difference identities have written proofs; the row-gcd equality is Su, Theorem 7.3.',
        'verification_source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    destination = Path(__file__).with_name('checks.json')
    destination.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps({key: value for key, value in certificate.items() if key != 'enumeration_rows'}, indent=2))


if __name__ == '__main__':
    run_checks()
