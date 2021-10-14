# py2html

Welcome to py2html, a Python library that helps you build HTML webpages saemlessly. This package allows you to set headers, text, links, lists, and more. Learn more about py2html and how you can use it in our [documentation](https://py2html.readthedocs.io).

## Install The Package

`pip install py2html`

## Examples

**Import Py2HTML:**

`from py2html import webpage`

**Define your Builder:**

`builder = Py2HTML()`

**Create Your Page:**

`builder.create(title="Your webpage title")`

After following these three steps, you are free to do anything you want with your webpage! Remember to save your file when you are done:

`builder.save(filename="sample.html")`