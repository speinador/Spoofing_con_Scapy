# 🕵️‍♂️ Spoofing de IP con Scapy
Este repositorio contiene un script de Python ( ```ip_spoof.py``` ) que demuestra cómo realizar un spoofing básico de direcciones IP utilizando la librería ```scapy```. El script permite especificar la IP de origen, la IP de destino y un mensaje personalizado, ofreciendo una visión práctica de esta técnica de red.

---

## 🎭 ¿Qué es el Spoofing de IP?
El **spoofing de IP** es una técnica en ciberseguridad donde un atacante falsifica la dirección IP de origen en los paquetes de red. Esto se hace para que la comunicación parezca provenir de una fuente diferente a la real. ¿El objetivo? Variado: desde ocultar la identidad del atacante hasta engañar a los sistemas para que acepten paquetes de una fuente que no es de confianza.

---

## 🚀 ¿Para Qué se Usa Este Código?
Este script está diseñado con fines puramente educativos y de demostración. Su propósito es ayudarte a:

- Comprender la construcción de paquetes: Observa cómo se ensamblan los paquetes IP e ICMP utilizando scapy.
- Experimentar con IPs de origen falsificadas: Envía un paquete con una IP de origen que no es la tuya.
- Visualizar el impacto: Entiende cómo un sistema receptor podría interpretar un paquete proveniente de una IP "falsa".

---

## 🚨 Implicaciones en Ciberseguridad
El spoofing de IP es una técnica fundamental que se encuentra en la base de varios tipos de ataques cibernéticos:

- **Ataques de Denegación de Servicio (DoS/DDoS):** Los atacantes pueden usar IPs falsificadas para ocultar su identidad mientras inundan un objetivo con tráfico, dificultando el rastreo y la mitigación.
- **Bypass de Firewalls/Filtros:** Si un firewall está configurado para permitir tráfico solo de ciertas IPs confiables, un atacante podría falsificar una de esas IPs para eludir las restricciones de seguridad.
- **Secuestro de Sesiones:** Aunque es una técnica más compleja, el spoofing de IP puede ser un componente clave en ataques para tomar el control de una sesión de comunicación ya establecida.
- **Engaño y Phishing:** En algunos contextos, el spoofing podría ser parte de un esquema más grande para engañar a usuarios o sistemas, haciéndoles creer que un mensaje proviene de una fuente legítima.

---

## 💻 Uso del Script
**Requisitos**
Asegúrate de tener ```scapy``` instalado, si usas Kali Linux deberia venir instalado por defecto. Si no lo tienes, puedes instalarlo fácilmente:

```
sudo apt update
sudo apt install python3-scapy
```
**Ejecución**
1. **Guarda el script:** Guarda el código proporcionado como ip_spoof.py.
```
https://github.com/speinador/Spoofing_con_Scapy/blob/main/ip_spoof.py
```

2. **Ejecútalo desde tu terminal:**

```
python ip_spoof.py
```

3. **Introduce los datos:** El script te guiará pidiéndote que ingreses:

- La **IP del router** (será la IP de origen falsificada).
- La **IP de la víctima** (el destino del paquete).
- El **mensaje** que quieres incluir en el paquete ICMP.

**Ejemplo de Interacción**
```
Ingresa la IP del router (ej. 192.168.0.1): 192.168.0.1
Ingresa la IP de la víctima (ej. 192.168.0.101): 192.168.0.101
Ingresa el mensaje que quieres enviar: ¡Soy tu router!

Paquete enviado desde 192.168.0.1 a 192.168.0.101 con el mensaje: '¡Soy tu router!'
```

---

⚠️ **Advertencia:** Este script es solo para **fines educativos y de aprendizaje**. El uso de técnicas de spoofing de IP en redes ajenas sin el permiso explícito del propietario es **ilegal y poco ético**. ¡Por favor, utiliza esta herramienta de manera responsable y ética!

---

## 🧑‍🏫 Autor

Explicación elaborada por [Sebastian Peinador](https://www.linkedin.com/in/sebastian-j-peinador/) para propósitos didácticos y de investigación en ciberseguridad ofensiva.

---

## 📄 Licencia

Este material se distribuye bajo la licencia [MIT](LICENSE).

---

> Si te resulta útil, ¡no olvides darle ⭐ al repo o compartirlo!
