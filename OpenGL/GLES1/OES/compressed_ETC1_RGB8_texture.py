'''OpenGL extension OES.compressed_ETC1_RGB8_texture

This module customises the behaviour of the 
OpenGL.raw.GLES1.OES.compressed_ETC1_RGB8_texture to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/compressed_ETC1_RGB8_texture.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLES1 import _types
from OpenGL.raw.GLES1.OES.compressed_ETC1_RGB8_texture import *
from OpenGL.raw.GLES1.OES.compressed_ETC1_RGB8_texture import _EXTENSION_NAME

def glInitCompressedEtc1Rgb8TextureOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION