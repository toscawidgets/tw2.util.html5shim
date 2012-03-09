import tw2.core as twc
import pkg_resources
import os

try:
    import version as ver
    ver_num = ver._version_num_
    _variant_ = 'min' # Always min
except ImportError:
    # Version information not found, 
    # `python setup.py updatelesscss` wasn't run prior to install
    # use defaults
    ver_num = 'pre3.5'
    _variant_ = 'min'


class JSLinkError(Exception): pass

# The adapter

class JSLinkMixin(twc.Link):
    name = twc.Param('(string) The name of the library to link to')
    dirname = twc.Param('(string) Specify the directory path for the given file, relative to the "static" folder. Some substitutions are allowed (name and version).')
    basename = twc.Param('(string) Specify the basename for the given file.')
    version = twc.Param('(string) Specify the version of the javascript library to use.')
    external = twc.Param('(boolean) True if you would like to grab the file from a CDN instead of locally. Default: False', default=False)
    url_base = twc.Param('(string) The base url for fetching the javascript library externally')
    extension = twc.Param('(string) File extension', default = 'js')
    additional_files = twc.Param('(list(string)) An optional list of files that should be registered with the static resource handler. Default: []', default=[])

    variant = twc.Param('File variant, e.g., (min for minified), default is %s' % _variant_, default=_variant_)

    def __init__(self, *args, **kw):
        self._link = None
        super(twc.Link, self).__init__(*args, **kw)

    def prepare(self):
        if not self.is_external:
            modname = self.modname or self.__module__
            rl = twc.core.request_local()
            resources = rl['middleware'].resources
            resources.register(self.modname, os.path.dirname(self.filename), whole_dir=True)
        super(JSLinkMixin, self).prepare()

    @property
    def core_filename(self):
        ret = self.basename
        if self.variant:
            ret = '.'.join((ret, self.variant))
        ret += '.' + self.extension
        return ret

    @property
    def external_link(self):
        link = self.url_base
        return link

    def _get_link(self):
        rl = twc.core.request_local()
        mw = rl['middleware']

        if not self._link:
            if self.external:
                link = self.external_link
            else:
                link = ('/'+'/'.join((mw.config.res_prefix.strip('/'), self.modname, 'static', self.dirname, self.core_filename)) )
            self._link = link
        return self._link % self.substitutions

    def _set_link(self, link):
        self._link = link

    #Variable('Direct web link to file. If this is not specified, it is\
    #   automatically generated, based on :attr:`modname` and \
    #:attr:`filename`.', default=property(_get_link, _set_link))
    link = property(_get_link, _set_link)

    def abspath(self, filename):
        return os.sep.join((pkg_resources.resource_filename(self.modname, ''), filename))

    def try_filename(self, filename):
        abspath = self.abspath(filename)
        if os.path.exists(abspath):
            return filename
        raise JSLinkError('File does not exist: %s'%abspath)

    @property
    def substitutions(self):
        return dict(name=self.name, version=self.version)

    @property
    def filename(self):
        #make basename windows/qnix compat
        basename = self.core_filename
        basename = basename.replace('/', os.sep)
        basename = basename.replace('\\', os.sep)

        filename = os.sep.join(('static', self.dirname, basename)) % self.substitutions
        #try the default
        return self.try_filename(filename)

    @property
    def is_external(self):
        return self.external

class HTML5ShimMixin(JSLinkMixin):
    name = 'lesscss'
    modname = 'tw2.util.html5shim'
    dirname = 'html5shim/%(version)s'
    basename = 'html5shim'
    version = ver_num
    url_base = '//html5shiv.googlecode.com/svn/trunk/html5.js'

class HTML5ShimJSLink(twc.JSLink, HTML5ShimMixin):
    template = "tw2.util.html5shim.templates.shim"
    location = 'head' # Needs to be loaded in head first
    pass

html5shim_js = HTML5ShimJSLink()
