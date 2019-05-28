#!/usr/bin/env python

"""Base classes for handling continuous-time stochastic processes"""
import numpy as np


class Checks(object):
    """Class checks that the various inputs are correct and reasonable"""
    
    def _check_increments(self, n):
        if not isinstance(n, int):
            raise TypeError("Number of increments must be an integer.")
        if n <= 0:
            raise ValueError("Number of increments must be positive.")

def _check_number(self, value, name):
    if not isinstance(value, (int, float)):
        raise TypeError(name + " value must be a number.")

    def _check_positive_number(self, value, name):
        self._check_number(value, name)
        if value <= 0:
            raise ValueError(name + " value must be positive.")

def _check_nonnegative_number(self, value, name):
    self._check_number(value, name)
        if value < 0:
            raise ValueError(name + " value must be nonnegative.")
                
                def _check_zero(self, zero):
                    if not isinstance(zero, bool):
raise TypeError("Zero inclusion flag must be a boolean.")


class Continuous(Checks):
    """Base class encompassing the properties for continuous time stochastic processes."
        """
    
    def __init__(self, t=1):
        self.t = t
        self._n = None
        self._times = None
    
    @property
    def t(self):
        """End time of the process."""
        return self._t
    
    @t.setter
    def t(self, value):
        self._check_positive_number(value, "Time end")
        self._t = float(value)
    
    def _check_times(self, n, zero):
        if self._n != n:
            self._n = n
            self._times = self.times(n, zero)

def _check_time_sequence(self, times):
    increments = np.diff(times)
        if np.any([t < 0 for t in times]):
            raise ValueError("Times must be nonnegative.")
    if np.any([t <= 0 for t in increments]):
        raise ValueError("Times must be strictly increasing.")
        return increments

def _linspace(self, end, n, zero=True):
    """Generate a linspace from 0 to end for n increments."""
        if zero:
            return np.linspace(0, end, n + 1)
    else:
        return np.linspace(1.0 * end / n, end, n)
