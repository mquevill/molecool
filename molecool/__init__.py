"""
molecool
analyzing and visualizing molecular coordinate files
"""

# Add imports here
from .functions import canvas

from .atom_data import atom_colors, atomic_weights
from .molecule import build_bond_list, calculate_molecular_mass

from .measure import calculate_angle, calculate_distance
from .visualize import draw_molecule, bond_histogram

from . import io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
