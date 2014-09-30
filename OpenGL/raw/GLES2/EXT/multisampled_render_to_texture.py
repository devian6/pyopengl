'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_EXT_multisampled_render_to_texture'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_EXT_multisampled_render_to_texture',error_checker=_errors._error_checker)
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT=_C('GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_SAMPLES_EXT',0x8D6C)
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT=_C('GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT',0x8D56)
GL_MAX_SAMPLES_EXT=_C('GL_MAX_SAMPLES_EXT',0x8D57)
GL_RENDERBUFFER_SAMPLES_EXT=_C('GL_RENDERBUFFER_SAMPLES_EXT',0x8CAB)
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLuint,_cs.GLint,_cs.GLsizei)
def glFramebufferTexture2DMultisampleEXT(target,attachment,textarget,texture,level,samples):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei)
def glRenderbufferStorageMultisampleEXT(target,samples,internalformat,width,height):pass