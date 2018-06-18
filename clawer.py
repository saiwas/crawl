
import file
import html_helper
import sys

def main():
  url = sys.argv[1]
  next_page = crawl_article(url)
  while next_page['slug'] != '/36/36613/':
    next_page = crawl_article(next_page['url'])

def crawl_article(url):
  domain = html_helper.url_parse(url)
  html = html_helper.get_html_content(url)
  content = html_helper.extra_content(html)
  file.create_file(content['title'], content['content'])
  return {
      "slug": content['next_link'],
      "url": domain + content['next_link']
  }

if __name__ == '__main__' :
  main()
