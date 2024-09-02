# Info de la materia: ST0263-242
## Estudiante(s): Juan Manuel Garzón Vargas, jmgarzonv@eafit.edu.co, Andrés Felipe Téllez Rodríguez, aftellezr@eafit.edu.co
## Profesor: EDWIN NELSON MONTOYA MUNERA, emontoya@eafit.edu.co
## Arquitectura P2P y Comunicación entre procesos mediante API REST, RPC y MO
## 1. Breve descripción de la actividad
La actividad consiste en diseñar e implementar un sistema P2P estructurado para la compartición de archivos. Cada nodo del sistema (peer) contiene microservicios que permiten la localización de recursos y la comunicación entre pares. El sistema utiliza gRPC para la comunicación de alto rendimiento, REST API para consultas de recursos, y RabbitMQ como middleware para la notificación de eventos.
### 1.1. Aspectos cumplidos o desarrollados de la actividad propuesta por el profesor
Requerimientos funcionales
Registro de pares: Implementación del método RegisterPeer que permite a los clientes registrarse en el sistema.
Consulta de recursos: Implementación de un microservicio que permite a los peers consultar el índice de archivos disponibles en otros nodos.
Interacción entre microservicios: Uso de gRPC y REST API para la comunicación entre microservicios, permitiendo la ejecución de operaciones de manera eficiente.
Requerimientos no funcionales
Manejo de concurrencia: Uso de un threading.Lock en los microservicios para asegurar el acceso seguro a los recursos compartidos.
Escalabilidad: La arquitectura permite la adición de nuevos peers sin afectar el rendimiento del sistema.
### 1.2. Aspectos NO cumplidos o desarrollados de la actividad propuesta por el profesor
Requerimientos funcionales
Transferencia de archivos: No se implementó la transferencia real de archivos, solo se proporciona un mecanismo de carga y descarga simulado (servicios ECO).
Autenticación de usuarios: No se implementó un sistema de autenticación para validar la identidad de los peers.
Requerimientos no funcionales
Documentación: La documentación del sistema es limitada y necesita ser ampliada para facilitar su comprensión y mantenimiento.
Pruebas automatizadas: No se implementaron pruebas automatizadas para validar el funcionamiento de los microservicios.
## 2. Información general de diseño de alto nivel
Arquitectura: El sistema sigue una arquitectura P2P estructurada basada en Chord, donde cada peer mantiene un índice de archivos y se comunica con otros peers para la localización de recursos.
Patrones utilizados: Se utilizó el patrón de diseño de "Productor-Consumidor" para la integración con RabbitMQ, y el patrón de "Microservicios" para la organización del código.
Mejores prácticas: Uso de gRPC para la comunicación eficiente entre microservicios y manejo de concurrencia para evitar condiciones de carrera.
## 3. Descripción del ambiente de desarrollo y técnico
Lenguaje de programación: Python 3.8
Librerías y paquetes:
grpcio (versión 1.42.0)
grpcio-tools (versión 1.42.0)
pika (versión 1.2.0)
flask (versión 2.0.1) para la API REST
Cómo se compila y ejecuta
Compilación del archivo .proto:

```
  bash
  python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. peer_service.proto
```

Ejecución del servidor (PServidor):

```
bash
python peer_server.py
```

Ejecución del cliente (PCliente):
```
bash
python peer_client.py
```
Ejecución del publicador:
```
bash
python publisher.py
```
Ejecución del consumidor:
```
bash
python consumer.py
```
Detalles del desarrollo
Parámetros del proyecto:
IP: 0.0.0.0 para aceptar conexiones externas
Puerto: 50051 para gRPC
Cola RabbitMQ: file_notifications
Directorio de archivos: Configurable a través del archivo de configuración.
Estructura de directorios y archivos importante del proyecto
```
text
project/
├── peer_client.py
├── peer_server.py
├── publisher.py
├── consumer.py
├── peer_service_pb2.py
├── peer_service_pb2_grpc.py
├── peer_service.proto
└── config.json
```

## 4. Descripción del ambiente de EJECUCIÓN (en producción)
Lenguaje de programación: Python 3.8
Librerías y paquetes:
```
grpcio (versión 1.42.0)
pika (versión 1.2.0)
flask (versión 2.0.1)
```
Configuración del entorno
IP o nombres de dominio: ec2-xx-xx-xx-xx.compute-1.amazonaws.com (ejemplo de instancia en AWS)
Parámetros de configuración:
IP: 0.0.0.0
Puerto: 50051
Cola RabbitMQ: file_notifications
Directorio de archivos: Configurable desde config.json.
Cómo se lanza el servidor
El servidor gRPC se lanza ejecutando el script peer_server.py, que inicia el servidor y espera conexiones de clientes.
Mini guía de uso para el usuario
Registrar un nuevo peer: Ejecutar peer_client.py para registrar un nuevo peer en la red.
Consultar recursos: Utilizar el cliente para consultar el índice de archivos disponibles en otros peers.
Cargar y descargar archivos: Simular la carga y descarga de archivos utilizando los servicios ECO implementados en los microservicios.

