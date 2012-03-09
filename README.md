# HTML5 Shim for ToscaWidgets2

## About

Allows HTML5-Shim to be added as a widget-specific or global resource for
compatability with Internet Explorer.

## Using tw2.util.html5shim

### Turbogears 2

If you need HTML5-Shim to be injected globally, add the following to 
`projectname/base/lib.py`

Top of file:

    from tw2.util.html5shim import html5shim_js

Above the `return` statement in `BaseController.__call__`:

    html5shim_js.inject()
