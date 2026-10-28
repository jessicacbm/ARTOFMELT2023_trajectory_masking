import xarray as xr
import pandas as pd
import numpy as np
from global_land_mask import globe

"""
Ice masking functions
"""

def closest_icecoord(value, search_array):   
    """
    Find the closest value in a given array (search_array) to a single value given by the user (x).
    For use in conjunction with apply_ufunc.
    Inputs:
    - values: the array of values that you want to 
    - search_array: the array that contains the values that you want to find the closest value of.
    Outputs:
    - an array 
    """
    value_dif = np.abs(value - search_array)
    closest_value = search_array[np.argmin(value_dif)]
    return closest_value

def determine_ice_coord(closest_x, closest_y, ice_data):
    """
    Determine the ice coodrdinate at that location from the ice data.
    Inputs:
    - closest_x, closest_y: the closest x and y coordinates held in the ice data netCDF file.
    Outputs:
    - z: the ice coordinate that corresponds to these coordinates.
    """
    z = ice_data['z'].sel(x=closest_x, y=closest_y).values
    return z

def ice_interpolation(x,y):
    """
    Finding the squared distance of an x-y coordinate in the stereographic projection from the origin (which is 0,0).
    """
    return np.sqrt(x**2 + y**2)

def ice_mask(closest_x, closest_y, z, thresh):
    """
    Actually perform the ice masking. If the coordinate is within a certain radiaus and is NaN, assume it is ice (fill in the hole at the North Pole
    from the satellite data), and if not return a 1 if it is sufficiently icy (75% ice) and a 0 if it is not!
    Inputs:
    - closest_x, closest_y, the closest ice coordinate to the trajectory coordinate.
    - z: the corresponding ice coordinate
    Outputs:
    - 1 if attributed to sea-ice, 0 if not sea-ice.
    """
    near_pole = ice_interpolation(closest_x, closest_y) < 325052.227135
   # pole_hole = near_pole & np.isnan(z)
    return (near_pole | (z >= thresh)).astype(int)

"""
Land masking functions
"""

def land_mask(lat, lon):
    """
    Check if a coordinate is land or not using global-land-mask. Global-land-mask cannot be vectorized.
    Inputs:
    - lat, lon: the latitude and longitude coordinate of the point in question
    Outputs:
    - 1 if land and 0 if ocean.
    """
    mask = globe.is_land(lat, lon)
    return mask.astype(int)

"""
Boundary layer masking function
"""

def bl_mask(alt, bl_height):
    """
    Mask to see if the air parcel is above or below the boundary layer.
    Inputs:
    - alt, the simulated altitude of the air parcel
    - bl_height: the simulated altitude of the boundary layer height
    Returns:
    - mask of same dimensions as inputs with 1 where alt > bl_height and 0 otherwise.
    """
    mask = (alt  > bl_height)
    return mask.astype(int)