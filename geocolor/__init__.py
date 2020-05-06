"""Geocolor Compositor"""

from satpy.composites import GenericCompositor
from satpy.dataset import combine_metadata


class GeoColor(GenericCompositor):
    """GeoColor Compositor"""
    def __call__(self, projectables, **kwargs):
        """Generate GeoColor"""
        # Check that the datasets match
        b01, b02, b03, b04, b13, sat_azm, sat_zen, sun_azm, sun_zen = self.match_data_arrays(projectables)
        return super(GeoColor, self).__call__((b01, b02, b03) **kwargs)
