Usage
=======

Here you will learn how to best use PyWig and take full advantage of 
the features it has to offer. The table below contains a list of attributes and their parameters.
Browse through the table of contents below to search for a specific attribute.

.. contents::
  :local:
  :depth: 3

+-----------------------+---------------------------+
| Attributes            | Parameters                |
+=======================+===========================+
| create_page           | title                     |
+-----------------------+---------------------------+
| add_header_           | header_type, text, style* |
+-----------------------+---------------------------+
| add_text_             | text, style*              |
+-----------------------+---------------------------+
| add_link_             | text, link, style*        |
+-----------------------+---------------------------+
| add_list_             | list_type, items, style*  |
+-----------------------+---------------------------+
| add_image_            | src, alt*, style*         |
+-----------------------+---------------------------+
| add_video_            | src                       |
+-----------------------+---------------------------+
| set_background_color_ | color                     |
+-----------------------+---------------------------+
| add_template          | template, items           |
+-----------------------+---------------------------+
| auto_create           | cooldown, max, filename   |
+-----------------------+---------------------------+
| save                  | filename                  |
+-----------------------+---------------------------+

.. _add_header: https://pywig.readthedocs.io/en/latest/usage.html#add_header
.. _add_text: https://pywig.readthedocs.io/en/latest/usage.html#add_text
.. _add_link: https://pywig.readthedocs.io/en/latest/usage.html#add_link
.. _add_list: https://pywig.readthedocs.io/en/latest/usage.html#add_list
.. _add_image: https://pywig.readthedocs.io/en/latest/usage.html#add_image
.. _add_video: https://pywig.readthedocs.io/en/latest/usage.html#add_video


Adding Elements
----------------
  
Basic Elements
~~~~~~~~~~~~~~~
  
.. function:: add_header(header_type, text, style=None)

.. function:: add_text(text, style=None)

.. function:: add_link(text, link, style=None)

.. function:: add_link(list_type, items, style=None)

Images and Videos
~~~~~~~~~~~~~~~~~~

.. function:: add_image(src, alt=None, style=None)

.. function:: add_video(src)
