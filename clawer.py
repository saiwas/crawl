
import file
import html_helper
import sys
import time

def main():
  url = sys.argv[1]
  end_url = "https://transcoder.baiducontent.com/tc?srd=1&dict=32&h5ad=1&bdenc=1&lid=7640207153210287896&title=%E9%80%8F%E8%A7%86%E5%8C%BB%E5%9C%A3%E6%9C%80%E6%96%B0%E7%AB%A0%E8%8A%82%28%E5%A4%A7%E5%B0%8F%E5%86%99%29%2C%E9%80%8F%E8%A7%86%E5%8C%BB%E5%9C%A3%E5%85%A8%E6%96%87%E9%98%85%E8%AF%BB%2C%E9%80%8F%E8%A7%86%E5%8C%BB%E5%9C%A3...&nsrc=IlPT2AEptyoA_yixCFOxXnANedT62v3IGti2RncK1TWz7JuVb4HvIddpWXKhVivJU-_cemaKf1C"
  next_page = crawl_article(url)
  while next_page['slug'] != end_url:
    next_page = crawl_article(next_page['slug'])

def crawl_article(url):
  domain = html_helper.url_parse(url)
  html = html_helper.get_html_content(url)
  content = html_helper.extra_content(html)
  file.create_file(content['title'], content['content'])
  time.sleep(1)
  return {
      "slug": content['next_link'],
      "url": domain + content['next_link']
  }

if __name__ == '__main__' :
  main()
