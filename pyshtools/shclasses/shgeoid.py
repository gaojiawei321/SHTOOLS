"""
    Class for height of the geoid.
"""
from __future__ import absolute_import as _absolute_import
from __future__ import division as _division
from __future__ import print_function as _print_function

import numpy as _np
import matplotlib as _mpl
import matplotlib.pyplot as _plt
import copy as _copy

from .shcoeffsgrid import SHGrid as _SHGrid


class SHGeoid(object):
    """
    Class for the geoid height. The class is initialized using
    SHGravCoeffs.geoid(). Geoid heights are referenced to a flattened
    ellipsoid of semimajor axis a and flattening f.

    Attributes

    geoid          : SHGrid class instance of the geoid.
    gm             : Gravitational constant time the mass of the body.
    potref         : Potential of the chosen geoid.
    a              : Semimajor axis of the reference ellipsoid.
    f              : Flattening of the reference ellipsoid,
                     f=(R_equator-R_pole)/R_equator.
    omega          : Angular rotation rate of the body.
    r              : Reference radius of the Taylor expansion.
    order          : Order of the Taylor expansion.
    lmax           : The maximum spherical harmonic degree resolvable by the
                     grids.
    lmax_calc      : The maximum spherical harmonic degree of the gravitational
                     potential used in creating the grids.
    nlat, nlon     : The number of latitude and longitude bands in the grids.
    sampling       : The longitudinal sampling scheme of the grids: either 1
                     for nlong=nlat or 2 for nlong=2*nlat.

    Methods

    plot()        : Plot all three components of the gravity field with the
                    total gravity disturbance.
    copy()        : Return a copy of the class instance.
    info()        : Print a summary of the data stored in the SHGrid instance.
    """
    def __init__(self, geoid, gm, potref, a, f, omega, r, order, lmax,
                 lmax_calc):
        """
        Initialize the SHGeoid class.
        """
        self.geoid = _SHGrid.from_array(geoid, grid='DH')
        self.grid = self.geoid.grid
        self.sampling = self.geoid.sampling
        self.nlat = self.geoid.nlat
        self.nlon = self.geoid.nlon
        self.potref = potref
        self.gm = gm
        self.a = a
        self.f = f
        self.omega = omega
        self.order = order
        self.r = r
        self.lmax = lmax
        self.lmax_calc = lmax_calc

    def copy(self):
        """Return a deep copy of the class instance."""
        return _copy.deepcopy(self)

    def info(self):
        """
        Print a summary of the data stored in the SHGravGrid class instance.

        Usage
        -----
        x.info()
        """
        print(repr(self))

    def __repr__(self):
        str = ('grid = {:s}\n'.format(repr(self.grid)))
        if self.grid == 'DH':
            str += 'sampling = {:d}\n'.format(self.sampling)
        str += ('nlat = {:d}\n'
                'nlon = {:d}\n'
                'lmax = {:d}\n'
                'lmax_calc = {:d}\n'
                'gm (m3 / s2) = {:e}\n'
                'reference potential (m /s) = {:e}\n'
                'a (m)= {:e}\n'
                'f = {:e}\n'
                'omega (rad / s) = {:s}\n'
                'radius of Taylor expansion (m) = {:e}\n'
                'order of expansion = {:d}'
                .format(self.nlat, self.nlon, self.lmax, self.lmax_calc,
                        self.gm, self.potref, self.a, self.f, repr(self.omega),
                        self.r, self.order))
        return str

    def plot(self, colorbar=True, cb_orientation='vertical',
             cb_label='geoid, m', **kwargs):
        """
        Plot the geoid.

        Usage
        -----
        x.plot([tick_interval, ax, colorbar, cb_orientation, cb_label,
                    show, fname])

        Parameters
        ----------
        tick_interval : list or tuple, optional, default = [30, 30]
            Intervals to use when plotting the x and y ticks. If set to None,
            ticks will not be plotted.
        xlabel : str, optional, default = 'longitude'
            Label for the longitude axis.
        ylabel : str, optional, default = 'latitude'
            Label for the latitude axis.
        ax : matplotlib axes object, optional, default = None
            A single matplotlib axes object where the plot will appear.
        colorbar : bool, optional, default = False
            If True, plot a colorbar.
        cb_orientation : str, optional, default = 'vertical'
            Orientation of the colorbar; either 'vertical' or 'horizontal'.
        cb_label : str, optional, default = 'geoid, m'
            Text label for the colorbar.
        show : bool, optional, default = True
            If True, plot the image to the screen.
        fname : str, optional, default = None
            If present, and if axes is not specified, save the image to the
            specified file.
        kwargs : optional
            Keyword arguements that will be sent to the SHGrid.plot()
            and plt.imshow() methods.
        """
        self.geoid.plot(colorbar=colorbar, cb_orientation=cb_orientation,
                        cb_label=cb_label, **kwargs)
