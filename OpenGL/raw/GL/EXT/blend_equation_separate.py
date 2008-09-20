'''OpenGL extension EXT.blend_equation_separate

Overview (from the spec)
	
	EXT_blend_func_separate introduced separate RGB and alpha blend
	factors.  EXT_blend_minmax introduced a distinct blend equation for
	combining source and destination blend terms.  (EXT_blend_subtract &
	EXT_blend_logic_op added other blend equation modes.)  OpenGL 1.4
	integrated both functionalities into the core standard.
	
	While there are separate blend functions for the RGB and alpha blend
	factors, OpenGL 1.4 provides a single blend equation that applies
	to both RGB and alpha portions of blending.
	
	This extension provides a separate blend equation for RGB and alpha
	to match the generality available for blend factors.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/blend_equation_separate.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_blend_equation_separate'
GL_BLEND_EQUATION_ALPHA_EXT = constant.Constant( 'GL_BLEND_EQUATION_ALPHA_EXT', 0x883D )
glget.addGLGetConstant( GL_BLEND_EQUATION_ALPHA_EXT, (1,) )
glBlendEquationSeparateEXT = platform.createExtensionFunction( 
	'glBlendEquationSeparateEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum,),
	doc = 'glBlendEquationSeparateEXT( GLenum(modeRGB), GLenum(modeAlpha) ) -> None',
	argNames = ('modeRGB', 'modeAlpha',),
)


def glInitBlendEquationSeparateEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
