"""
Color Thief
-----------

A module for grabbing the color palette from an image.

Links
`````

* `github <https://github.com/fengsp/color-thief-py>`_
* `development version
  <http://github.com/fengsp/color-thief-py/zipball/master#egg=color-thief-py-dev>`_

"""
from setuptools import setup


setup(
    name='colorthief',
    version='0.1',
    url='https://github.com/fengsp/color-thief-py',
    license='BSD',
    author='Shipeng Feng',
    author_email='fsp261@gmail.com',
    description='A module for grabbing the color palette from an image.',
    long_description=__doc__,
    py_modules=['colorthief'],
    install_requires=[
        'Pillow'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
