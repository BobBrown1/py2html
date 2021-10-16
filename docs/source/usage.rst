Usage
=======

Here you will learn how to best use PyWig and take full advantage of 
the features it has to offer. The following table contains a list of attributes and their parameters.
Click on the attributes to learn more about them or read through the entire page.

+----------------------+---------------------------+
| Attributes           | Parameters                |
+======================+===========================+
| create_page          | title                     |
+----------------------+---------------------------+
| add_header           | header_type, text, style* |
+----------------------+---------------------------+
| add_text             | text, style*              |
+----------------------+---------------------------+
| add_link             | text, link, style*        |
+----------------------+---------------------------+
| add_list             | list_type, items, style*  |
+----------------------+---------------------------+
| add_image            | src, alt*, style*         |
+----------------------+---------------------------+
| add_video            | src                       |
+----------------------+---------------------------+
| set_background_color | color                     |
+----------------------+---------------------------+
| add_template        | template, items           |
+----------------------+---------------------------+
| auto_create          | cooldown, max, filename   |
+----------------------+---------------------------+
| save                 | filename                  |
+----------------------+---------------------------+

Adding Elements
----------------
  
.. function:: add_header(header_type, text, style*)

.. function:: add_text(text, style*)

.. function:: add_link(text, link, style*)

.. function:: add_link(list_type, items, style*)
