'''OpenGL extension VERSION.GL_1_5

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_5 to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_1_5 import *
### END AUTOGENERATED SECTION

glDeleteBuffers = arrays.setInputArraySizeType(
	glDeleteBuffers,
	None,
	arrays.GLuintArray,
	'buffers',
)

glGenBuffers = wrapper.wrapper( glGenBuffers ).setOutput(
	'buffers', lambda n: (n,), 'n',
)

def _sizeOfArrayInput( pyArgs, index, wrapper ):
	return (
		arrays.ArrayDatatype.arrayByteCount( pyArgs[index] )
	)

glBufferData = wrapper.wrapper( glBufferData ).setPyConverter(
	'data', arrays.asVoidArray(),
).setPyConverter( 'size' ).setCResolver( 
	'data', arrays.ArrayDatatype.voidDataPointer ,
).setCConverter(
	'size', _sizeOfArrayInput,
).setReturnValues( 
	wrapper.returnPyArgument( 'data' ) 
)

glBufferSubData = wrapper.wrapper( glBufferSubData ).setPyConverter(
	'data', arrays.asVoidArray(),
).setPyConverter( 'size' ).setCResolver( 
	'data', arrays.ArrayDatatype.voidDataPointer ,
).setCConverter(
	'size', _sizeOfArrayInput,
).setReturnValues( 
	wrapper.returnPyArgument( 'data' ) 
)
