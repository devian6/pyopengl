'''OpenGL extension INGR.blend_func_separate

This module customises the behaviour of the 
OpenGL.raw.GL.INGR.blend_func_separate to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.INGR.blend_func_separate import *
### END AUTOGENERATED SECTION