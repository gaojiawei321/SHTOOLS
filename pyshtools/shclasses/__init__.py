"""
Class interface for pyshtools.

pyshtools defines several classes that facilitate the interactive examination
of geographical gridded data and their associated spherical harmonic
coefficients. Superclasses are used to implement interface functions and
documentation and subclasses are used to handle different internal data types.

pyshtools class structure:

    SHCoeffs
        SHRealCoeffs
        SHComplexCoeffs

    SHGrid
        DHRealGrid
        DHComplexGrid
        GLQRealGrid
        GLQComplexGrid

    SHWindow
        SHWindowCap
        SHWindowMask

    Gravity classes
    ---------------
    SHGravCoeffs
        SHGravRealCoeffs
    SHGravGrid
    SHGravTensor
    SHGeoid

For more information, see the documentation for the top level classes.
"""

from __future__ import absolute_import as _absolute_import
from __future__ import division as _division
from __future__ import print_function as _print_function

from .shcoeffsgrid import SHCoeffs
from .shcoeffsgrid import SHRealCoeffs
from .shcoeffsgrid import SHComplexCoeffs

from .shcoeffsgrid import SHGrid
from .shcoeffsgrid import DHRealGrid
from .shcoeffsgrid import DHComplexGrid
from .shcoeffsgrid import GLQRealGrid
from .shcoeffsgrid import GLQComplexGrid

from .shwindow import SHWindow
from .shwindow import SHWindowCap
from .shwindow import SHWindowMask

from .shgravcoeffs import SHGravCoeffs
from .shgravcoeffs import SHGravRealCoeffs
from .shgravgrid import SHGravGrid
from .shgravtensor import SHGravTensor
from .shgeoid import SHGeoid
