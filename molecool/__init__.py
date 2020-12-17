"""
molecool
analyzing and visualizing molecular coordinate files
"""

# Add imports here
from .functions import (
    canvas,
    calculate_distance,
    open_pdb,
    open_xyz,
    write_xyz,
    draw_molecule,
    calculate_angle,
    bond_histogram,
    build_bond_list,
)


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
