'''OpenGL extension ARB.framebuffer_sRGB

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/framebuffer_sRGB.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_framebuffer_sRGB'
GL_FRAMEBUFFER_SRGB = constant.Constant( 'GL_FRAMEBUFFER_SRGB', 0x8DB9 )


def glInitFramebufferSrgbARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
