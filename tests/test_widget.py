from tw2.core.testbase import WidgetTest
from tw2.util import *

class TestUtil(WidgetTest):
    # place your widget at the TestWidget attribute
    widget = Util
    # Initilization args. go here 
    attrs = {'id':'util-test'}
    params = {}
    expected = """<div id="util-test"></div>"""
