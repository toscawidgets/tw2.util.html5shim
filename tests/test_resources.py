import tw2.core as twc
from nose.tools import eq_

from tw2.util.html5shim import html5shim_js
try:
    from tw2.util.html5shim import version
    _ver_num_ = version._version_num_
except ImportError:
    _ver_num_ = 'pre3.5'

def request_local_tst():
    global _request_local, _request_id
# if _request_id is None:
# raise KeyError('must be in a request')
    if _request_local == None:
        _request_local = {}
    try:
        return _request_local[_request_id]
    except KeyError:
        rl_data = {}
        _request_local[_request_id] = rl_data
        return rl_data

twc.core.request_local = request_local_tst
_request_local = {}
_request_id = 'whatever'

def setup():
    twc.core.request_local = request_local_tst
    twc.core.request_local()['middleware'] = twc.make_middleware()

def test_html5shim_js():
    shim = html5shim_js.req()
    eq_(shim.link, '/resources/tw2.util.html5shim/static/html5shim/%s/html5shim.min.js'% _ver_num_)
