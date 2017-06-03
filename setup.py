from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize

import numpy
import pyarrow
setup(name='arrow_cython',
      version='0.0.1',
      ext_modules=cythonize([
        Extension('cy',
              sources=['cy.pyx'],
              extra_compile_args=["-std=c++11", '-stdlib=libc++',
                "-I" + pyarrow.__path__[0] + '/include',
                "-I" + numpy.get_include()],

              extra_link_args=["-std=c++11", '-stdlib=libc++'],
              language='c++')
        ]),
    install_requires=['pyarrow', 'numpy'])

