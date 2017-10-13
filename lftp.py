import sublime
import sublime_plugin
import os
import json
from shutil import copyfile

def findConfig(configPath):
	while not os.path.isfile(configPath) and not configPath == "/lftp-config.json":
		print (configPath)
		configPath = configPath.rsplit('/',2)[0] + "/lftp-config.json"
	if os.path.isfile(configPath):
		configObj = json.loads(open(configPath).read())
		return (configObj)
	else:
		print ("No config file found! (lftp-config.json)")
		return None

def syncFile(windowObj):
	thisFileName = windowObj.view.file_name().rsplit('/',1)[1]
	thisDir = windowObj.view.file_name().rsplit('/',1)[0]
	thisFile = windowObj.view.file_name()
	configFile = thisDir + "/lftp-config.json"
	configObj = findConfig(configFile)
	if configObj != None:
		mappedPath = configObj["mappedPath"]
		copyPath = thisFile.replace(configFile.rsplit('/',1)[0],mappedPath,1)
		copyfile(thisFile, copyPath)
		print("File copied from",thisFile,"to",copyPath)

class LocalsyncCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		syncFile(self)

class EventListeners(sublime_plugin.EventListener):
	def on_post_save(self, view): # event triggered after a file has been saved
		configObj = findConfig(view.file_name().rsplit('/',1)[0] + "/lftp-config.json")
		if configObj != None and configObj["syncOnSave"] == "true":
			self.view = view
			syncFile(self)