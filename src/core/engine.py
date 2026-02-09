import socket
import threading
from datetime import datetime

class AIScannerCore:
    def __init__(self, target, threads=20):
        self.target = target
        self.threads = threads
        self.results = []
        self.vulns = []

    def audit_port(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            if s.connect_ex((self.target, port)) == 0:
                self.results.append(port)
                if port == 21: self.vulns.append("CRITICAL: FTP Detected")
                if port == 22: self.vulns.append("INFO: SSH Active")
                if port == 80: self.vulns.append("WARNING: HTTP Exposed")
            s.close()
        except: pass

    def launch(self, start, end):
        print(f"[*] Escaneando: {self.target}")
        pool = []
        for port in range(start, end + 1):
            t = threading.Thread(target=self.audit_port, args=(port,))
            pool.append(t)
            t.start()
            if len(pool) >= self.threads:
                for t in pool: t.join()
                pool = []
        for t in pool: t.join()
        return self.results, self.vulns
