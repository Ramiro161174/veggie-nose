#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servidor local para el dashboard Veggie-Nose.
Sirve esta carpeta en http://localhost:PORT y abre el navegador.
Todo ocurre en el propio ordenador: no sale nada a internet.
Web Serial funciona porque localhost es un contexto seguro.
"""
import http.server, socketserver, webbrowser, os, sys

PORT = 8765
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass  # sin ruido en consola

def main():
    try:
        httpd = socketserver.TCPServer(("127.0.0.1", PORT), Handler)
    except OSError:
        # puerto ocupado: abre el navegador igualmente, ya habra un servidor
        webbrowser.open(f"http://localhost:{PORT}")
        print(f"Ya habia un servidor en el puerto {PORT}. Abriendo el navegador...")
        input("Pulsa Enter para cerrar esta ventana.")
        return
    url = f"http://localhost:{PORT}"
    print("=" * 50)
    print("  Veggie-Nose Dashboard en marcha")
    print("  " + url)
    print("  Deja esta ventana abierta mientras lo usas.")
    print("  Para cerrar: cierra esta ventana.")
    print("=" * 50)
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
