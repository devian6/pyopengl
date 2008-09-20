'''OpenGL extension INTEL.texture_scissor

This module customises the behaviour of the 
OpenGL.raw.GL.INTEL.texture_scissor to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.INTEL.texture_scissor import *
### END AUTOGENERATED SECTION