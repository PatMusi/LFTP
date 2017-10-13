Copy this folder into your sublime plugins directory

MacOS: /Users/<user>/Library/Application Support/Sublime Text 3/Packages

Use

In any folder, create a file called "lftp-config.json" and give it one property called "mappedPath" with the absolute path to the other local folder you want to map to.

After the lftp-config.json file is in place and configured, right click on any open file tab in sublime and click on "Sync to Local Folder"

To enable sync on file save, add a parameter to the JSON file, "syncOnSave": "true"