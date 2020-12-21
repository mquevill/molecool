"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import numpy as np
import pytest

import molecool


def test_calculate_distance():
    """
    Simple test to check distance calculations.
    """

    r1 = np.array([0, 0, 0])
    r2 = np.array([1, 2, 3])

    expected_distance = np.sqrt(14)

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert pytest.approx(expected_distance) == calculated_distance


@pytest.mark.parametrize(
    "p1, p2, p3, expected_angle",
    [
        (np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90),
        (
            np.array([np.sqrt(2) / 2, np.sqrt(2) / 2, 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            45,
        ),
        (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60),
        (
            np.array([np.sqrt(3) / 2, 1 / 2, 0]),
            np.array([0, 0, 0]),
            np.array([1, 0, 0]),
            30,
        ),
    ],
)
def test_calculate_angle(p1, p2, p3, expected_angle):
    calculated_angle = molecool.calculate_angle(p1, p2, p3, degrees=True)

    assert pytest.approx(expected_angle) == calculated_angle
