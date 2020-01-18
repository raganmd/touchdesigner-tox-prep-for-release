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
	aims to simplify some of that process by automating the prep and packaging of a TOX in a consistent and
	reliable manner.

	---------------
	
	'''

	def __init__( self ):
		''' This is the init method for the Soptosvg process
		'''
		self.Release_target_op		= parent().par.Targetoperator
		self.Release_version 		= parent().par.Releaseversion
		self.Reset_color			= (0.545, 0.545, 0.545)
		self.Format_ready_save_loc	= '{loc}/{name}.tox'
		self.Save_dir				= parent().par.Savelocation
		self.Tox_Name				= parent().par.Toxname
		self.Destory_tags			= parent().par.Destroytags
		self.Ext_file_tags 			= parent().par.Externalfiletags 

		self.GithubLink 			= "https://github.com/raganmd/touchdesigner-tox-prep-for-release"
		print( "PackagTOX Initialized" )
		return

	def Save_tox(self):
		# format the save location for the tox
		save_loc 					= self.Format_ready_save_loc.format(loc=self.Save_dir, name=self.Tox_Name)
		
		target_op 					= self.Release_target_op.eval()

		# set version
		target_op.par.Version  		= self.Release_version
		target_op.par.Version.readOnly = True

		# clean-up external files - disable loading, remove paths
		ext_file_tags 				= self.Ext_file_tags.val.split(',')
		ops_to_prep 				= target_op.findChildren(tags=ext_file_tags)
		self.Disable_external_file(ops_to_prep)

		# ensure target tox doesn't have a file path
		target_op.par.externaltox = ''
		
		# reset target tox color to be default
		target_op.color = self.Reset_color

		# lock the tox icon 
		target_op.op('null_icon').lock = True

		# destory ops used for Dev
		destory_tags 				= self.Destory_tags.val.split(',')
		ops_to_destory 				= target_op.findChildren(tags=destory_tags)
		self.Destory_ops(ops_to_destory)

		# save TOX in target location
		target_op.save(save_loc)
		
		return save_loc
	
	def Destory_ops(self, ops_to_destory):
		
		for each in ops_to_destory:
			each.destroy()

		return ops_to_destory

	def Disable_external_file(self, ops_to_prep):
	
		for each in ops_to_prep:
			# remove path par for ext
			each.par.file 			= ''
			# turn off loading on start
			each.par.loadonstart 	= False
			each.par.syncfile 		= False 
	
		return ops_to_prep
	
	def Open_github_link(self):

		webbrowser.open_new_tab(self.GithubLink)
	
		return self.GithubLink
	