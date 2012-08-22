'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_texture_storage_multisample'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_texture_storage_multisample',False)

@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTexStorage2DMultisample( target,samples,internalformat,width,height,fixedsamplelocations ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTexStorage3DMultisample( target,samples,internalformat,width,height,depth,fixedsamplelocations ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureStorage2DMultisampleEXT( texture,target,samples,internalformat,width,height,fixedsamplelocations ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLsizei,_cs.GLenum,_cs.GLsizei,_cs.GLsizei,_cs.GLsizei,_cs.GLboolean)
def glTextureStorage3DMultisampleEXT( texture,target,samples,internalformat,width,height,depth,fixedsamplelocations ):pass


def glInitTextureStorageMultisampleARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )