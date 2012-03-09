import os

from distutils.core import setup, Command
import urllib2

from posixpath import basename
import re

class SetupBuildCommand(Command):
    """
    Master setup build command to subclass from.
    """

    user_options = []

    def initialize_options(self):
        """
        Setup the current dir.
        """
        self._dir = os.getcwd()

    def finalize_options(self):
        """
        Set final values for all the options that this command supports.
        """
        pass

class UpdateHTML5ShivCommand(SetupBuildCommand):
    '''
    Updates the HTML5-Shiv Runtime library
    '''
    
    description = "updates HTML5shiv with latest version"
    dl_link = 'http://html5shim.googlecode.com/svn/trunk/html5.js'

    def run(self):
        ver_regex = re.compile(r'^/\*! HTML5 Shiv ([\dpre.]+)')

        # Download H5-shiv
        shiv_js = urllib2.urlopen(self.dl_link)

        data = shiv_js.read()

        ver_num = ver_regex.match(data.splitlines()[0]).groups()[0]

        # Check to see if the directory already exists, if not make it
        if not os.path.exists('tw2/util/html5shim/static/html5shim/%s' % ver_num):
            os.mkdir('tw2/util/html5shim/static/html5shim/%s' % ver_num)

        # Write out the shim
        with open('tw2/util/html5shim/static/html5shim/%s/html5shim.min.js'%ver_num, 'w') as js:
            js.write(data)

        # Update version.py
        vs_file = "_version_num_ = '{ver_num}'".format(ver_num=ver_num)

        with open('tw2/util/html5shim/version.py', 'w') as vs_py:
            print "Writing new version.py"
            vs_py.write(vs_file)

        # Done!
        print 'Updated HTML5Shim to %s...' % ver_num
