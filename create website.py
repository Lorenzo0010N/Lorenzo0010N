from googlesearch import search
from bs4 import BeautifulSoup
import requests
import re

def google_search(query):
    results = search(query, num=5, stop=5, pause=2)
    result_snippets = []
    for url in results:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.get_text()
        text = re.sub(r'\s+', ' ', text)
        result_snippets.append(text[:200])  # Abbrevia il testo a 200 caratteri
    return result_snippets

def generate_html(results):
    html = "<html><head><title>Risultati della ricerca</title></head><body>"
    for i, snippet in enumerate(results):
        html += f"<p><b>Risultato {i+1}:</b> {snippet}</p>"
    html += "</body></html>"
    return html

def save_html(html, filename):
    with open(filename, 'w') as file:
        file.write(html)

def start_server(filename, port=8000):
    import http.server
    import socketserver
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Server avviato su http://localhost:{port}")
        httpd.serve_forever()

def main():
    num_words = int(input("Inserisci il numero di parole da cercare: "))
    words = [input(f"Inserisci la parola {i+1}: ") for i in range(num_words)]
    max_results = int(input("Inserisci il numero massimo di righe per risultato: "))

    results = []
    for word in words:
        print(f"Effettuando la ricerca per '{word}'...")
        snippets = google_search(word)
        results.append(snippets[:max_results])

    html = generate_html(results)
    filename = "search_results.html"
    save_html(html, filename)
    print(f"Pagina web generata: {filename}")

    start_server(filename)

if __name__ == "__main__":
    main()
