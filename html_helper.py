import urllib.request
import urllib.parse
import re


def get_html_content(url):
  f = urllib.request.urlopen(url)
  return f.read().decode('gb2312', errors='ignore')


def extra_content(html):
  title = re.search(
      r'<div class="nr_title" id="nr_title">(.*?)</div>', html, re.S)
  content = re.search(r'<div id="nr1">(.*?)</div>', html, re.S)
  return title.group(1).strip(), clean_up_tags(content.group(1).strip())


def clean_up_tags(html_content):
  result = html_content.replace('<br />', '').replace('&nbsp;', '').replace(
      '<a href="http://www.paipaibook.com&lt;a" target="_blank">www.paipaibook.com&lt;a</a> href=&quot;//&quot; target=&quot;_blank&quot;&gt;--&lt;/a&gt;', '')
  return result
