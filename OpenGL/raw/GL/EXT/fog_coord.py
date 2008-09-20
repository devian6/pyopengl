'''OpenGL extension EXT.fog_coord

Overview (from the spec)
	
	This extension allows specifying an explicit per-vertex fog
	coordinate to be used in fog computations, rather than using a
	fragment depth-based fog equation.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/fog_coord.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_fog_coord'
GL_FOG_COORDINATE_SOURCE_EXT = constant.Constant( 'GL_FOG_COORDINATE_SOURCE_EXT', 0x8450 )
GL_FOG_COORDINATE_EXT = constant.Constant( 'GL_FOG_COORDINATE_EXT', 0x8451 )
GL_FRAGMENT_DEPTH_EXT = constant.Constant( 'GL_FRAGMENT_DEPTH_EXT', 0x8452 )
GL_CURRENT_FOG_COORDINATE_EXT = constant.Constant( 'GL_CURRENT_FOG_COORDINATE_EXT', 0x8453 )
glget.addGLGetConstant( GL_CURRENT_FOG_COORDINATE_EXT, (1,) )
GL_FOG_COORDINATE_ARRAY_TYPE_EXT = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_TYPE_EXT', 0x8454 )
glget.addGLGetConstant( GL_FOG_COORDINATE_ARRAY_TYPE_EXT, (1,) )
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_STRIDE_EXT', 0x8455 )
glget.addGLGetConstant( GL_FOG_COORDINATE_ARRAY_STRIDE_EXT, (1,) )
GL_FOG_COORDINATE_ARRAY_POINTER_EXT = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_POINTER_EXT', 0x8456 )
GL_FOG_COORDINATE_ARRAY_EXT = constant.Constant( 'GL_FOG_COORDINATE_ARRAY_EXT', 0x8457 )
glFogCoordfEXT = platform.createExtensionFunction( 
	'glFogCoordfEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLfloat,),
	doc = 'glFogCoordfEXT( GLfloat(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoordfvEXT = platform.createExtensionFunction( 
	'glFogCoordfvEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLfloatArray,),
	doc = 'glFogCoordfvEXT( GLfloatArray(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoorddEXT = platform.createExtensionFunction( 
	'glFogCoorddEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLdouble,),
	doc = 'glFogCoorddEXT( GLdouble(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoorddvEXT = platform.createExtensionFunction( 
	'glFogCoorddvEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(arrays.GLdoubleArray,),
	doc = 'glFogCoorddvEXT( GLdoubleArray(coord) ) -> None',
	argNames = ('coord',),
)

glFogCoordPointerEXT = platform.createExtensionFunction( 
	'glFogCoordPointerEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLsizei, ctypes.c_void_p,),
	doc = 'glFogCoordPointerEXT( GLenum(type), GLsizei(stride), c_void_p(pointer) ) -> None',
	argNames = ('type', 'stride', 'pointer',),
)


def glInitFogCoordEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
