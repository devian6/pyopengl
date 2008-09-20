'''OpenGL extension MESA.ycbcr_texture

This module customises the behaviour of the 
OpenGL.raw.GL.MESA.ycbcr_texture to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.MESA.ycbcr_texture import *
### END AUTOGENERATED SECTION