# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:55:09 2025

@author: marti
"""

from ._implementacion import _calculo_complejo

def sumar_y_multiplicar(a, b, c):
    return a + b + _calculo_complejo(b, c)