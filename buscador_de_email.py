import requests
import re

def extract_emails(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

    # Usamos uma expressão regular para encontrar endereços de e-mail
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', response.text)
    return emails

def save_emails_to_file(emails, site_nome):
    nome_arquivo = f"{site_nome}_emails.txt"
    with open(nome_arquivo, 'w') as file:
        for email in emails:
            file.write(email + '\n')

def main():
    url = input("Digite o site para buscar e-mails: ")

    # Adiciona 'https://' se não estiver presente na URL
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    print(f"Buscando e-mails em {url}")

    emails = extract_emails(url)

    if not emails:
        print("Nenhum e-mail encontrado.")
        return

    print(f"\nE-mails encontrados ({len(emails)} no total):")
    for email in emails:
        print(email)

    # Usa o nome do site (sem "https://") para criar o nome do arquivo
    site_nome = re.sub(r'https?://(www\.)?', '', url)
    site_nome = site_nome.replace('.', '_')

    salvar_arquivo = input("\nDeseja salvar os e-mails em um arquivo? (s/n): ").lower()

    if salvar_arquivo == 's':
        # Salva os e-mails no arquivo
        save_emails_to_file(emails, site_nome)
        print(f"E-mails salvos em {site_nome}_emails.txt")

if __name__ == "__main__":
    main()
