'''Package TOX for Release Class
Authors | matthew ragan
matthewragan.com
'''

import webbrowser

class PackageTOX:
	'''
	This class is designed to operate as a general helper extension. 
	
	When sharing a TOX it's often difficult to ensure that it's correctly 
	packaged in a uniform and consistent manner that will ensure it's immediately usable by a third party. This TOX 
	aims to simplify some of that process by automating the prep and packaging of a TOX in a consitent and
	reliable manner.

	---------------
	
	'''

	def __init__( self ):
		''' This is the init method for the Soptosvg process
		'''
		self.Polylinesop 			= parent.svg.par.Polylinesop
		self.Polygonsop				= parent.svg.par.Polygonsop
		self.Svgtype 				= parent.svg.par.Svgtype
		self.Filepath 				= "{dir}/{file}.svg"
		self.UseCamera 				= parent.svg.par.Usecamera
		self.Camera 				= parent.svg.par.Camera
		self.Aspect 				= (parent.svg.par.Aspect1, parent.svg.par.Aspect2)



		self.Axidocumentation 		= "http://wiki.evilmadscientist.com/AxiDraw"
		self.Axipdf 				= "http://cdn.evilmadscientist.com/wiki/axidraw/software/AxiDraw_V33.pdf"
		self.Svgwritedocumentation 	= "http://svgwrite.readthedocs.io/en/latest/svgwrite.html"

		print( "Sop to SVG Initialized" )
		return