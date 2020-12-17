"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np

def test_calculate_distance():
    """
    Simple test to check distance calculations.
    """

    r1 = np.array([0, 0, 0])
    r2 = np.array([1, 2, 3])

    expected_distance = np.sqrt(14)

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

def test_calculate_angle():
    """
    Simple test to check distance calculations.
    """

    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_angle == calculated_angle
