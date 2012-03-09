# HTML5 Shim for ToscaWidgets2

## About

Allows HTML5-Shim to be added as a widget-specific or global resource for
compatability with Internet Explorer versions lower than 9.0.

## Using tw2.util.html5shim

### Inside ToscaWidget2 Widgets

In the `widgets.py` file (or a resource declaration file if you use one)
add following:

Top of file:

    from tw2.util.html5shim import html5shim_js

In the widget declaration add `html5shim_js` to the resources attribute 
like so:

    class YourWidget(tw2.core.Widget):
        resources = [html5shim_js, other_res, another_res]


### Turbogears 2

If you need HTML5-Shim to be injected globally, add the following to 
`projectname/base/lib.py`

Top of file:

    from tw2.util.html5shim import html5shim_js

Above the `return` statement in `BaseController.__call__`:

    html5shim_js.inject()
