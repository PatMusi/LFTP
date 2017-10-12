import sublime
import sublime_plugin
import os
import json
from shutil import copyfile

class LocalsyncCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		thisFileName = self.view.file_name().rsplit('/',1)[1]
		thisDir = self.view.file_name().rsplit('/',1)[0]
		thisFile = self.view.file_name()
		configFile = thisDir + "/lftp-config.json"
		while not os.path.isfile(configFile) and not configFile == "/lftp-config.json":
			print (configFile)
			configFile = configFile.rsplit('/',2)[0] + "/lftp-config.json"
		if os.path.isfile(configFile):
			configObj = json.loads(open(configFile).read())
			mappedPath = configObj["mappedPath"]
			copyPath = thisFile.replace(configFile.rsplit('/',1)[0],mappedPath,1)
			copyfile(thisFile, copyPath)
			print("File copied from",thisFile,"to",copyPath)
		else:
			print ("No config file!")
