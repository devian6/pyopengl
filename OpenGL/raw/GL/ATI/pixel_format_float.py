'''OpenGL extension ATI.pixel_format_float

Overview (from the spec)
	
	This extension adds pixel formats with floating-point RGBA color
	components.
	
	The size of each float components is specified using the same
	WGL_RED_BITS_ARB, WGL_GREEN_BITS_ARB, WGL_BLUE_BITS_ARB and
	WGL_ALPHA_BITS_ARB pixel format attributes that are used for
	defining the size of fixed-point components.  32 bit floating-
	point components are in the standard IEEE float format.  16 bit
	floating-point components have 1 sign bit, 5 exponent bits,
	and 10 mantissa bits. 
	
	In standard OpenGL RGBA color components are normally clamped to
	the range [0,1].  The color components of a float buffer are
	clamped to the limits of the range representable by their format.
	

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ATI/pixel_format_float.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_pixel_format_float'
GL_TYPE_RGBA_FLOAT_ATI = constant.Constant( 'GL_TYPE_RGBA_FLOAT_ATI', 0x8820 )
GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = constant.Constant( 'GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI', 0x8835 )
glget.addGLGetConstant( GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI, (4,) )


def glInitPixelFormatFloatATI():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
