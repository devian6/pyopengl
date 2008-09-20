'''OpenGL extension NV.packed_depth_stencil

This module customises the behaviour of the 
OpenGL.raw.GL.NV.packed_depth_stencil to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.NV.packed_depth_stencil import *
### END AUTOGENERATED SECTION