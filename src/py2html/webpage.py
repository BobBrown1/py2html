import re

class Py2HTML:
  def __init__(self, htmlstring = None):
   htmlstring = ""
   self.htmlstring = htmlstring

  def create_page(self, title):
    self.htmlstring += f"<!DOCTYPE html>\n<html>\n<head>\n<title>{title}</title>\n</head>\n<body>"
    return self.htmlstring

  def add_header(self, headertype, text, style=None):
    headerlist = ["h1", "h2", "h3", "h4", "h5", "h6"]
    if headertype in headerlist:
      pass
    else:
      raise ValueError("Invalid header type.")
      return
    if style != None:
      self.htmlstring += f"\n<{headertype} style=\"{style}\">{text}</{headertype}>"
    else:
      self.htmlstring += f"\n<{headertype}>{text}</{headertype}>"
    return self.htmlstring

  def add_text(self, text, style=None):
    if style != None:
      self.htmlstring += f"\n<p style=\"{style}\">{text}</p>"
    else:
      self.htmlstring += f"\n<p>{text}</p>"
    return self.htmlstring

  def set_background_color(self, colorhex):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', colorhex)
    if match:                      
      self.htmlstring = self.htmlstring.replace("<body>", f"<body style=\"background-color: {colorhex}\">")
      return self.htmlstring
    else:
      raise ValueError("Invalid hex code.")
      return

  def add_link(self, text, link, style=None):
    if style != None:
      self.htmlstring += f"\n<a href=\"{link}\" style=\"{style}\">{text}</a>"
    else:
      self.htmlstring += f"\n<a href=\"{link}\">{text}</a>"
    return self.htmlstring

  def add_break(self):
    self.htmlstring += "<br>\n"
    return self.htmlstring

  def clear(self):
    self.htmlstring = ""
    return self.htmlstring

  def add_image(self, src, alt=None, style=None):
    if alt == None:
      alt = "An Image"
    if style != None:
      self.htmlstring += f"\n<img src=\"{src}\" alt=\"{alt}\" style=\"{style}\">"
    else:
      self.htmlstring += f"\n<img src=\"{src}\" alt=\"{alt}\">"
    return self.htmlstring

  def add_video(self, src):
    oggfile = src.replace(".mp4", ".ogg")
    self.htmlstring += f"\n<video controls>\n<source src=\"{src}\" type=\"video/mp4\">\n<source src=\"{oggfile}\" type=\"video/ogg\"\nVideo Not Supported\n</video>"
    return self.htmlstring
 
  def save(self, pagename):
    self.htmlstring += "\n</body>\n</html>"
    file = open(f"{pagename}","w")
    file.write(self.htmlstring)
    file.close()