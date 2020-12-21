"""
measure.py
Performs measurements of various properties
"""

import numpy as np


def calculate_angle(rA, rB, rC, degrees=False):
    """
    Calculate angle between three points.

    Parameters
    ----------
    rA, rB, rC : np.ndarray
        Coordinates of each point.

    degrees : bool, Optional, default=False
        Set whether or not to use degrees.

    Returns
    -------
    theta : float
        Angle between three points
    """

    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta


def calculate_distance(rA, rB):
    """
    Calculate distance between two points.

    Parameters
    ----------
    rA, rB : np.ndarray
        Coordinates of each point.

    Returns
    -------
    dist : float
        Distance between two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 1, 0])
    >>> calculate_distance(r1, r2)
    1.0
    """

    d = rA - rB
    dist = np.linalg.norm(d)
    return dist
