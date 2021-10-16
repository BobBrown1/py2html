Frequently Asked Questions
===========================

Here are some frequently asked questions that we think will help you on your PyWig journey:

.. contents:: Table of FAQ Contents:
  
  :local:
  
General Questions
------------------

How do I install the package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install the package using the following code:

.. code-block:: console

  pip install pywig
  
Learn more in :doc:`installation`.

How do I mass create HTML files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

  A reasonable cooldown time is highly recommended for this function.
  
Use the following code to automatically create as many files as you would like:

.. code-block:: python

  builder.auto_create(cooldown=20, max=5, filename="sample.html")
  
**Things to keep in mind:**
* Cooldown time is in seconds
* A number will be added to your file name after the first is made (e.g. file two will be named "sample-1.html", file five will be named "sample-6", etc.)
* Using your own while loop rather than this function is highly discouraged

Why is my code not returning anything?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure you have used the start and end functions that are required in PyWig. 
For example:

.. code-block:: python

  builder.create_page("Page Title")
  # my pywig code here
  builder.save("sample.html")
  
If you would not like to save the code in a file and rather have it be outputted in your console, define the last line of your build and print it.
For example:

.. code-block:: python

  builder.create_page("Page Title")
  builder.add_header("h1", "Header Text")
  x = builder.add_text("This is how you output HTML")
  print(x)

  
