from bs4 import BeautifulSoup


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    pre_str = [i.text.replace("\n", "") for i in soup.find_all({"div": {"class": "texts"}})]

    while "" in pre_str:
        pre_str.remove("")

    return '\n'.join(pre_str)
