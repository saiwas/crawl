
import file
import html_helper

def main():
  url = ''
  html = html_helper.get_html_content(url)
  content = html_helper.extra_content(html)
  file.create_file(content[0], content[1])


if __name__ == '__main__' :
  main()
