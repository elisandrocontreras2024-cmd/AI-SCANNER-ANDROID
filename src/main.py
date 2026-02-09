from core.engine import AIScannerCore
print("--- AI-SCANNER-ANDROID v1.0 ---")
scanner = AIScannerCore("127.0.0.1")
found, alerts = scanner.launch(20, 1024)
print(f"\n[+] Puertos: {found}\n[!] Alertas: {alerts}")
