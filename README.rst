Color Thief
===========

A Python module for grabbing the color palette from an image.

Installation
------------

::

    $ pip install colorthief

Usage
-----

.. code:: python

    from colorthief import ColorThief

    color_thief = ColorThief('/path/to/imagefile')
    # get the dominant color
    dominant_color = color_thief.get_color(quality=1)
    # build a color palette
    palette = color_thief.get_palette(color_count=6)

API
---

.. code:: python

    class ColorThief(object):
        def __init__(self, file):
            """Create one color thief for one image.

            :param file: A filename (string) or a file object. The file object
                         must implement `read()`, `seek()`, and `tell()` methods,
                         and be opened in binary mode.
            :param is_obj: A boolean. If True, the object will be passed along. Useful
                        for passing PIL objects to ColorThief.
            """
            pass

        def get_color(self, quality=10):
            """Get the dominant color.

            :param quality: quality settings, 1 is the highest quality, the bigger
                            the number, the faster a color will be returned but
                            the greater the likelihood that it will not be the
                            visually most dominant color
            :return tuple: (r, g, b)
            """
            pass

        def get_palette(self, color_count=10, quality=10):
            """Build a color palette.  We are using the median cut algorithm to
            cluster similar colors.

            :param color_count: the size of the palette, max number of colors
            :param quality: quality settings, 1 is the highest quality, the bigger
                            the number, the faster the palette generation, but the
                            greater the likelihood that colors will be missed.
            :return list: a list of tuple in the form (r, g, b)
            """
            pass

Thanks
------

Thanks to Lokesh Dhakar for his `original work
<https://github.com/lokesh/color-thief/>`_.

Better
------

If you feel anything wrong, feedbacks or pull requests are welcome.
