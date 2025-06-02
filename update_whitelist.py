
import requests

GITHUB_RAW_URL = "https://raw.githubusercontent.com/votre-utilisateur/votre-repo/main/cheat_signatures/file_whitelist.txt"

def update_whitelist():
    try:
        response = requests.get(GITHUB_RAW_URL)
        if response.status_code == 200:
            with open("cheat_signatures/file_whitelist.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("[✓] Whitelist mise à jour depuis GitHub.")
        else:
            print(f"[ERREUR] Échec de la mise à jour : {response.status_code}")
    except Exception as e:
        print(f"[ERREUR] Exception lors de la mise à jour de la whitelist : {e}")
