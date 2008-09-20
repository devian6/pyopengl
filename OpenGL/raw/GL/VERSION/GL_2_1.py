'''OpenGL extension VERSION.GL_2_1

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/VERSION/GL_2_1.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_VERSION_GL_2_1'
GL_CURRENT_RASTER_SECONDARY_COLOR = constant.Constant( 'GL_CURRENT_RASTER_SECONDARY_COLOR', 0x845F )
GL_PIXEL_PACK_BUFFER = constant.Constant( 'GL_PIXEL_PACK_BUFFER', 0x88EB )
GL_PIXEL_UNPACK_BUFFER = constant.Constant( 'GL_PIXEL_UNPACK_BUFFER', 0x88EC )
GL_PIXEL_PACK_BUFFER_BINDING = constant.Constant( 'GL_PIXEL_PACK_BUFFER_BINDING', 0x88ED )
GL_PIXEL_UNPACK_BUFFER_BINDING = constant.Constant( 'GL_PIXEL_UNPACK_BUFFER_BINDING', 0x88EF )
GL_FLOAT_MAT2x3 = constant.Constant( 'GL_FLOAT_MAT2x3', 0x8B65 )
GL_FLOAT_MAT2x4 = constant.Constant( 'GL_FLOAT_MAT2x4', 0x8B66 )
GL_FLOAT_MAT3x2 = constant.Constant( 'GL_FLOAT_MAT3x2', 0x8B67 )
GL_FLOAT_MAT3x4 = constant.Constant( 'GL_FLOAT_MAT3x4', 0x8B68 )
GL_FLOAT_MAT4x2 = constant.Constant( 'GL_FLOAT_MAT4x2', 0x8B69 )
GL_FLOAT_MAT4x3 = constant.Constant( 'GL_FLOAT_MAT4x3', 0x8B6A )
GL_SRGB = constant.Constant( 'GL_SRGB', 0x8C40 )
GL_SRGB8 = constant.Constant( 'GL_SRGB8', 0x8C41 )
GL_SRGB_ALPHA = constant.Constant( 'GL_SRGB_ALPHA', 0x8C42 )
GL_SRGB8_ALPHA8 = constant.Constant( 'GL_SRGB8_ALPHA8', 0x8C43 )
GL_SLUMINANCE_ALPHA = constant.Constant( 'GL_SLUMINANCE_ALPHA', 0x8C44 )
GL_SLUMINANCE8_ALPHA8 = constant.Constant( 'GL_SLUMINANCE8_ALPHA8', 0x8C45 )
GL_SLUMINANCE = constant.Constant( 'GL_SLUMINANCE', 0x8C46 )
GL_SLUMINANCE8 = constant.Constant( 'GL_SLUMINANCE8', 0x8C47 )
GL_COMPRESSED_SRGB = constant.Constant( 'GL_COMPRESSED_SRGB', 0x8C48 )
GL_COMPRESSED_SRGB_ALPHA = constant.Constant( 'GL_COMPRESSED_SRGB_ALPHA', 0x8C49 )
GL_COMPRESSED_SLUMINANCE = constant.Constant( 'GL_COMPRESSED_SLUMINANCE', 0x8C4A )
GL_COMPRESSED_SLUMINANCE_ALPHA = constant.Constant( 'GL_COMPRESSED_SLUMINANCE_ALPHA', 0x8C4B )
glUniformMatrix2x3fv = platform.createExtensionFunction( 
	'glUniformMatrix2x3fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix2x3fv( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix3x2fv = platform.createExtensionFunction( 
	'glUniformMatrix3x2fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix3x2fv( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix2x4fv = platform.createExtensionFunction( 
	'glUniformMatrix2x4fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix2x4fv( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix4x2fv = platform.createExtensionFunction( 
	'glUniformMatrix4x2fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix4x2fv( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix3x4fv = platform.createExtensionFunction( 
	'glUniformMatrix3x4fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix3x4fv( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix4x3fv = platform.createExtensionFunction( 
	'glUniformMatrix4x3fv', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix4x3fv( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

