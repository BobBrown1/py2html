# py2html

Welcome to py2html, a python library that helps you build html webpages seemlessly. This package allows you to set headers, text, links, divs, and more. Learn more about py2html and how you can use it in our documentation.

## Install The Package

`pip install py2html`

## Examples

**Import Py2HTML:**

`from py2html import webpage`

**Define your Builder:**

`builder = Py2HTML()`

**Create Your Page:**

`builder.create(title="Your webpage title")`

**Add A Header:**

`builder.add_header(headertype="h1", text="My Header Text Here")`

**Add Text:**

`builder.add_text(text="Your text here")`

**Set Webpage Background Color:**

`builder.set_background_color(color="Hex Code Here [e.g. #FFFFFF]")`

**Saving The File:**

`builder.save("sample.html")`