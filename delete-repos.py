import requests

# Inserisci il tuo nome utente e token personale GitHub
username = 'CampanelliEmanuele'
token = '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'

# Prefisso delle repository da eliminare
prefixs = ['html-', 'css-',  'htmlcss-', 'bootstrap-',  'js-',  'java-',  'db-',  'spring-', 'Spring-', 'hello-']
reposToDelete = ['drink-project', 'best-of-the-year', 'human-code']

def get_repositories():
    url = f'https://api.github.com/users/{username}/repos'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Errore durante il recupero delle repository:", response.status_code)
        return None

def delete_repository(repo_name):
    url = f'https://api.github.com/repos/{username}/{repo_name}'
    headers = {'Authorization': f'token {token}'}
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' eliminata con successo.")
    else:
        print(f"Errore durante l'eliminazione della repository '{repo_name}':", response.status_code)

def filter_and_delete_repositories(repositories, filter_func):
    for repo in filter(filter_func, repositories):
        delete_repository(repo['name'])

def main():
    repositories = get_repositories()
    if repositories:
        # eliminazione delle repo aventi un certo suffisso
        for prefix in prefixs:
            filter_and_delete_repositories(repositories, lambda r: r['name'].startswith(prefix))
                    
        # eliminazione di repository specifiche
        for repoToDelete in reposToDelete:
            filter_and_delete_repositories(repositories, lambda r: r['name'] == repoToDelete)

if __name__ == "__main__":
    main()
