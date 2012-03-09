from setuptools import setup, find_packages

from setup_ext import UpdateHTML5ShivCommand

import multiprocessing
import logging

setup(
    name='tw2.util.html5shim',
    version='2.0.0a',
    description='HTML5 Shim resource for TW2',
    author='Greg Jurman',
    author_email='gdj2214@rit.edu',
    url='https://github.com/toscawidgets/tw2.util.html5shim',
    install_requires=[
        "tw2.core",
        'mako',
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2', 'tw2.util'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.util.html5shim
    """,
    keywords = [
        'toscawidgets.widgets',
        'html5-shim'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    cmdclass = {'updatehtml5shim' : UpdateHTML5ShivCommand}
)
