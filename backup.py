
# Took reference from Byte of Python

import os
import time

sourcePath = input('Enter source path to backup :')
backupPath = input('Folder path to store backup file :')

backupFolderPath = backupPath + os.sep + time.strftime('%d_%m_%Y')

if not os.path.exists(backupFolderPath) :
	os.mkdir(backupFolderPath)

now = time.strftime('%H%M%S')

fileNameWithPath = backupFolderPath + os.sep + now + '.zip'

zipCommand = 'zip -r {0} {1}'.format(fileNameWithPath, sourcePath)

if os.system(zipCommand) :
	print('Back up failed')
else :
	print('Back up complete')