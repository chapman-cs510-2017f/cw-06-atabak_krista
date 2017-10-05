#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###
# Name: Krista, Atabak
# Student ID: KristaIDHere, AtabakIDHere
# Email:  kristaEmailHere , AtabakEmail
# Course: CS510 Fall 2017
# Assignment: Classwork 6
###
"""
import cplane_np as cplane
import pandas as pd
from pandas.util.testing import assert_frame_equal

def test_plane():
    """
    test function
    :return:
    :rtype:
    """
    c_plane = cplane.ArrayComplexPlane(0, 3, 3, 0, 3, 3)
    ans = pd.DataFrame([[0.0+0.j  , 1.5+ 0.j  , 3.0+0.j],
                         [0.0+1.5j , 1.5+1.5j , 3.0+1.5j],
                         [0.0+3.j  , 1.5+3.j ,  3.0+3.j ]])
    assert_frame_equal(c_Plane.plane, ans)

