# mex30-sdk

## Install AWS CLI
```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip
sudo ./aws/install
```

## Create Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate
```

## Problems

1. Automatizador de subida de archivos a Amazon S3
Objetivo
Crear un script en Python que suba automáticamente archivos locales a un bucket.
Servicios involucrados
Amazon S3
boto3
Funcionalidad del proyecto
El script debe:
Subir un archivo
Listar archivos en el bucket
Descargar un archivo

2. Sistema automático de backups a S3
Objetivo
Crear un script que haga backup automático de una carpeta local hacia S3.
Servicios involucrados
Amazon S3
Funcionalidad
El programa debe:
Escanear una carpeta
Subir todos los archivos
Crear una carpeta con fecha
Ejemplo de estructura en S3:


3. Monitor de instancias EC2
Objetivo
Crear un script que liste y monitoree instancias EC2.
Servicios involucrados
Amazon EC2
Funcionalidad
El script debe mostrar:
Instance ID
Estado
Tipo de instancia
IP pública


4. Script para limpiar buckets S3 automáticamente
Objetivo
Crear un programa que detecte y elimine archivos antiguos.
Servicios
Amazon S3
Funcionalidad
El script debe:
listar objetos
detectar archivos > 30 días
eliminarlos

5. Sistema simple de alertas con CloudWatch
Objetivo
Crear métricas personalizadas desde Python.
Servicios
Amazon CloudWatch

6. Generador automático de usuarios IAM
Objetivo
Crear un script que cree usuarios IAM automáticamente.
Servicios
AWS Identity and Access Management
Funcionalidad
El script debe:
crear usuarios
asignar políticas
generar access keys

7. Inventario de recursos AWS
Objetivo
Crear un script que escanee tu cuenta AWS y genere un inventario.
Servicios
Amazon EC2
Amazon S3
AWS Lambda
Salida del programa
El script genera un archivo:
aws_inventory.json


