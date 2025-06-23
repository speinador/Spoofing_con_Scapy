from scapy.all import *

# Solicitar al usuario la IP del router
router_ip = input("Ingresa la IP del router (ej. 192.168.0.1): ")

# Solicitar al usuario la IP de la víctima
victim_ip = input("Ingresa la IP de la víctima (ej. 192.168.0.101): ")

# Solicitar al usuario el mensaje
message = input("Ingresa el mensaje que quieres enviar: ")

# Construir el paquete con la información ingresada por el usuario
paquete = IP(src=router_ip, dst=victim_ip) / ICMP() / message

# Enviar el paquete
send(paquete, count=1)

print(f"\nPaquete enviado desde {router_ip} a {victim_ip} con el mensaje: '{message}'")