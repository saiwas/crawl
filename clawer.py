
import file
import html_helper
import sys


def main():
  url = sys.argv[1]
  html = html_helper.get_html_content(url)
  content = html_helper.extra_content(html)
  file.create_file(content['title'], content['content'])


if __name__ == '__main__' :
  main()
