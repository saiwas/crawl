import urllib.request
import urllib.parse
import re


def get_html_content(url):
    f = urllib.request.urlopen(url)
    return f.read().decode('gb2312', errors='ignore')


def extra_content(html):
    title = re.search(
        r'<title>(.*?)</title>', html, re.S)
    content = re.search(
        r'<div id="nr1">(.*?)<div class="nr_page">', html, re.S)
    next_page = re.search(
        r'<td class="next"><a href="(.*?)" h5_ads_link="1" id="pt_next">', html, re.S)
    result = {
        'title' : title.group(1).strip(),
        'content': clean_up_tags(content.group(1).strip()),
        'next_link': next_page.group(1).replace('amp;', '')
    }
    return result

def url_parse(url):
    url_info = urllib.parse.urlparse(url)
    return url_info.scheme + '://' + url_info.netloc

def clean_up_tags(html_content):
    result = html_content.replace(
        '<div style="margin:10px 0 5px 0"></div>', '').replace('</div>', '').replace(
        '<br/>', '\n').replace('\u3000', '').replace('”', '').replace('“', '')

    a_tags = re.search(r'<a (.*?)>(.*)</a>', html_content, re.S)
    if not a_tags is None:
        result = result.replace(a_tags.group(), '')
    return result
