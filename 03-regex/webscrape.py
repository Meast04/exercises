import requests
import re

def extract_urls(url):
    response = requests.get(url)
    html_content = response.text

    url_pattern = r"https?://[^\s]+?\.(?:jpg|jpeg|png|svg|gif)"

    urls = re.findall(url_pattern, html_content)

    return urls

def main():
    url = "https://www.bol.com"
    urls = extract_urls(url)
    print("Extracted urls:")
    for url in urls:
        print(url)

main()