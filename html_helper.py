import urllib.request
import urllib.parse
import re


def get_html_content(url):
    print(url)
    f = urllib.request.urlopen(url)
    return f.read().decode('gb2312', errors='ignore')


def extra_content(html):
    title = re.search(
        r'<div class="nr_title" id="nr_title">(.*?)</div>', html, re.S)
    content = re.search(r'<div id="nr1">(.*?)</div>', html, re.S)
    next_page = re.search(
        r'<a id="pt_next" href="(.*?)">(.*?)</a>', html, re.S)
    result = {
        'title' : title.group(1).strip(),
        'content': clean_up_tags(content.group(1).strip()),
        'next_page': next_page.group(2),
        'next_link': next_page.group(1)
    }
    return result

def url_parse(url):
    url_info = urllib.parse.urlparse(url)
    return url_info.scheme + '://' + url_info.netloc

def clean_up_tags(html_content):
    result = html_content.replace('<br />', '').replace('&nbsp;', '')

    a_tags = re.search(r'<a (.*?)>(.*)</a>', html_content, re.S)
    if not a_tags is None:
        result = result.replace(a_tags.group(), '')
    return result
