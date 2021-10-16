Quickstart
===========

Looking to learn PyWig as quickly as possible and get your web page generator up and running? You've come to the right page!

.. note::
  This tutorial assumes you have already installed and imported the PyWig package. 
  If you haven't done so, please read the :doc:`installation` segment.

Coding a Basic Web Page Generator
-----------------------------------

Let's make a simple web page generator with just a few lines of code. This will show you the basics of PyWig.

Copy and paste this code into your Python file, then we'll go over what it means and does:

.. code-block:: python

  builder = webpage.PyWig()
  
  builder.create_page("My PyWig Webpage")
  builder.add_header("h1", text="Welcome to my web page")
  builder.add_text(text="This is my simple web page made with PyWig! Learn more in our documentation and on our github page.")
  
  builder.save("sample.html")
  
Now let's learn about what is happening in this code block. 

1. **Defining the builder**:
  * Your web page builder is your key to creating webpages. With it, you can create headers, text, links, lists and more.
2. **Creating a page**: 
  * Creating your page creates the string that will contain all of your web page elements. This is a required step that must be taken before creating your web page. The title of your webpage is the only parameter. This is the title that will appear in your list of tabs on a browser.
3. **Adding a Header**:
  * This is the first element we add to our webpage. The header_type is set as `h1` so that the text will be large. Your header can be any type, `h1` - `h6`. The text is what your header will contain.
4. **Adding Text**:
  * This is the text that will be displayed under your header as a paragraph. The text is what is displayed in your paragraph, it can be however long orshort you want.
5. **Saving your Web Page**:
  * This is the final line of your web page as it will save your web page as a `.html` or `.txt` file, depending on the file extension you pick. For this tutorial, we are saving the file as an HTML document named `sample.html`.
  
Now you must run your Python file. If you are using an online IDE, you can run your file there. Otherwise, enter the following code in your terminal:

For Linux or MacOS:

.. code-block:: console

  python3 your_file_name.py
  
For Windows:

.. code-block:: console

  py -3 your_file_name.py

Congrats! You have now created a basic web page builder with PyWig!

Want to learn more?
---------------------

There is so much more you can do with PyWig. If you want to add more elements and customize your web pages, try exploring the :doc:`usage` segment to learn more!