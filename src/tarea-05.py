import socket
import time
import threading

pages = ["scanme.nmap.org", "testphp.vulnweb.com","example.com","google.com"]
#AF_INET significa IPv4 
#SOCK_STREAM significa TCP conexion orientada a flujo no a datagramas
def nmap(page:str) -> None:
    ports = []
    for port in range(1000):  
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((page, port)) == 0:
                    ports.append(port)
                    print(f"puerto abierto encontrado: {port} en {page}")

    print(f"puerto abierto: {ports} en {page}")

if __name__ == "__main__":
    start = time.time()
    threads = []
    for page in pages:
         threads.append(
              threading.Thread(target=nmap,args=(page,))
         )   

    for thread in threads:
         thread.start()

    for thread in threads:
         thread.join()
    
    end = time.time()

    print(f"Tiempo total {end-start}")