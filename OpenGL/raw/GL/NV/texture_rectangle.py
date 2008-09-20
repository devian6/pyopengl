'''OpenGL extension NV.texture_rectangle

Overview (from the spec)
	
	OpenGL texturing is limited to images with power-of-two dimensions
	and an optional 1-texel border.  NV_texture_rectangle extension
	adds a new texture target that supports 2D textures without requiring
	power-of-two dimensions.
	
	Non-power-of-two dimensioned textures are useful for storing
	video images that do not have power-of-two dimensions.  Re-sampling
	artifacts are avoided and less texture memory may be required by using
	non-power-of-two dimensioned textures.  Non-power-of-two dimensioned
	textures are also useful for shadow maps and window-space texturing.
	
	However, non-power-of-two dimensioned (NPOTD) textures have
	limitations that do not apply to power-of-two dimensioned (POT)
	textures.  NPOTD textures may not use mipmap filtering; POTD
	textures support both mipmapped and non-mipmapped filtering.
	NPOTD textures support only the GL_CLAMP, GL_CLAMP_TO_EDGE,
	and GL_CLAMP_TO_BORDER_ARB wrap modes; POTD textures support
	GL_CLAMP_TO_EDGE, GL_REPEAT, GL_CLAMP, GL_MIRRORED_REPEAT_IBM,
	and GL_CLAMP_TO_BORDER.  NPOTD textures do not support an optional
	1-texel border; POTD textures do support an optional 1-texel border.
	
	NPOTD textures are accessed by non-normalized texture coordinates.
	So instead of thinking of the texture image lying in a [0..1]x[0..1]
	range, the NPOTD texture image lies in a [0..w]x[0..h] range.
	
	This extension adds a new texture target and related state (proxy,
	binding, max texture size).

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/texture_rectangle.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_texture_rectangle'
GL_TEXTURE_RECTANGLE_NV = constant.Constant( 'GL_TEXTURE_RECTANGLE_NV', 0x84F5 )
glget.addGLGetConstant( GL_TEXTURE_RECTANGLE_NV, (1,) )
GL_TEXTURE_BINDING_RECTANGLE_NV = constant.Constant( 'GL_TEXTURE_BINDING_RECTANGLE_NV', 0x84F6 )
glget.addGLGetConstant( GL_TEXTURE_BINDING_RECTANGLE_NV, (1,) )
GL_PROXY_TEXTURE_RECTANGLE_NV = constant.Constant( 'GL_PROXY_TEXTURE_RECTANGLE_NV', 0x84F7 )
GL_MAX_RECTANGLE_TEXTURE_SIZE_NV = constant.Constant( 'GL_MAX_RECTANGLE_TEXTURE_SIZE_NV', 0x84F8 )
glget.addGLGetConstant( GL_MAX_RECTANGLE_TEXTURE_SIZE_NV, (1,) )


def glInitTextureRectangleNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
