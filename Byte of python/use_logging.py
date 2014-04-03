import os, platform, logging

if platform.platform().startswith('Windows'):
	logFile = os.path.join(os.getenv('HOMEDRIVE'), OS.getenv('HOMEPATH'), 'test.log')
else :
	logFile = os.path.join(os.getenv('HOME'), 'test.log')

print('logging to file :', logFile)

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s : %(levelname)s : %(message)s',
	filename = logFile,
	filemode = 'w',
	)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')