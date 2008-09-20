'''OpenGL extension DFX.texture_compression_FXT1

Overview (from the spec)
	
	    This extension additional texture compression functionality 's FXT1
	    format, specific to 3dfxsubject to all the requirements and
	    limitations described by the extension GL_ARB_texture_compression.
	    The FXT1 texture format supports only 2D and 3D images without
	    borders.
	
	    Because 3dfx expects to make continual improvement to its FXT1
	    compressor implementation, 3dfx recommends that to achieve best
	    visual quality applications adopt the following procedure with
	    respect to reuse of textures compressed by the GL:
	
		1) Save the RENDERER and VERSION strings along with images
		   compressed by the GL;
		2) Before reuse of the textures, compare the stored strings with
		   strings newly returned from the current GL;
		3) If out-of-date, repeat the compression and storage steps.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/DFX/texture_compression_FXT1.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_DFX_texture_compression_FXT1'
GL_COMPRESSED_RGB_FXT1_3DFX = constant.Constant( 'GL_COMPRESSED_RGB_FXT1_3DFX', 0x86B0 )
GL_COMPRESSED_RGBA_FXT1_3DFX = constant.Constant( 'GL_COMPRESSED_RGBA_FXT1_3DFX', 0x86B1 )


def glInitTextureCompressionFxt1DFX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
