# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 12:00:46 2025

@author: marti
"""

from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Mi primer paquete de Python'
LONG_DESCRIPTION = 'Mi primer paquete de Python con una descripción ligeramente más larga'

# Configurando
setup(
       # el nombre debe coincidir con el nombre de la carpeta 	  
       #'modulomuysimple'
        name="PRACTICA1", 
        version=VERSION,
        author="Martin Gonzalez",
        author_email="<tuemail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # añade cualquier paquete adicional que debe ser
        #instalado junto con tu paquete. Ej: 'caer'
        
        keywords=['python', 'primer paquete'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)