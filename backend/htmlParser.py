from bs4 import BeautifulSoup


def html_parser(html):
    soup = BeautifulSoup(html, 'html.parser')

    x = [i.text.replace("\n", "") for i in soup.find_all({"div": {"class": "texts"}})]

    while "" in x:
        x.remove("")

    return '\n'.join(x)
