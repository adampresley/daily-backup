#! /usr/bin/python

#
# dailyBackup.py
# Creates a twice daily backup of documents and such on my local machine
# and puts them into my network personal folder for company backup.
#
# The variable backupSrc below controls what folders get archived.
#
# Author: Adam Prelsey
# Version: 1.0
#

import os, zipfile
import datetime
import shutil


def performArchive(zipFile, backupLocations):
	#
	# Walk the tree yo.
	#
	print "Zipping files in"

	with zipfile.ZipFile(zipFile, "w") as z:
		for srcDir in backupLocations:
			print "... %s" % (srcDir)
			filenames = os.listdir(srcDir)

			#
			# Loop over all the files in this directory, and if they are not
			# temp files, or a directory, add them to the ZIP archive.
			#
			for filename in filenames:
				fullFilename = os.path.join(srcDir, filename)
				if filename[0] != "~" and not os.path.isdir(fullFilename):
					z.write(fullFilename)



#
# Change me or add to me to determine WHAT get's backed up.
#
backupLocations = [
	"C:\\Users\\adampresley\\Documents"
]

#
# Change me to determine where ZIP files are temporarily saved.
# Change tmpFilename to alter how ZIP files are named.
#
zipLocation = "C:\\backup"
zipFilename = ("backup-%s.zip" % (datetime.datetime.now().isoformat())).replace(":", "-")
zipFullPath = "%s\\%s" % (zipLocation, zipFilename)

if not os.path.exists(zipFullPath):
	f = open(zipFullPath, "w")
	f.write(" ")
	f.close()


#
# Do the deed.
#
performArchive(zipFullPath, backupLocations)


#
# Copy to another location
#
shutil.copyfile(zipFullPath, "\\\\server\\somewhere\\else\\%s" % (zipFilename))
