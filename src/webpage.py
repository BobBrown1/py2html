def create_page(title):
    htmlstring = ""
    htmlstring += f"<!DOCTYPE html>\n<html>\n<head>\n<title>{title}</title>\n</head>\n<body>\n"
    return htmlstring

def add_header(htmlstring, headertype, text):
  htmlstring += f"<{headertype}>{text}</{headertype}>"
  return htmlstring
  
def close_page(htmlstring, pagename):
  htmlstring += "\n</body>\n</html>"
  file = open(f"{pagename}.html","w")
  file.write(htmlstring)
  file.close()