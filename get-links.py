import sys
from bs4 import BeautifulSoup

def extract_links(html_file):
    with open(html_file, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        links = [f'"https:{link}"' for link in links if link.startswith("//")]
        links = list(set(links))
    return ' '.join(links)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        html_file = sys.argv[1]
        code_snippet = extract_links(html_file)
        print(code_snippet)
    else:
        print("Please provide an HTML file as a command line argument.")
