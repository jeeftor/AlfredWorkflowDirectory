from workflow import Workflow3
import os, sys
import plistlib

def main(wf):

	from os.path import expanduser
	home = expanduser("~")
	
	cwd = os.getcwd()

	base_dir = os.path.abspath('..')
	#home + '/Library/Application Support/Alfred 3/Alfred.alfredpreferences/workflows'
	
	wf_directories = os.listdir(base_dir)

	for wfd in wf_directories:
		try:
			wf_base_dir = base_dir + '/' + wfd + '/'
			plist_file = wf_base_dir + 'info.plist'
			pl = plistlib.readPlist(plist_file)

			# print pl.get('name')
			# print 'Version: ' + pl.get('version','0')
			icon_file = wf_base_dir + '/icon.png'

			wf.add_item(pl.get('name'), 'Version: ' + pl.get('version','0'), arg=wf_base_dir, type=u'file', icon=icon_file, valid=True)
		except:
			pass
	wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow3(libraries=['./lib'])
    log = wf.logger
    sys.exit(wf.run(main))

