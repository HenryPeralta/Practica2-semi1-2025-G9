# Manual Técnico

## Integrantes
|             Nombre             |   Carnet  |
| :----------------------------  | :------   |
| Henry Gabriel Peralta Martinez | 201712289 |
| Brando Iván Muñoz Debroy       | 201700890 |
| Diego Abraham Robles Meza      | 201901429 |
| Oscar David Padilla Vásquez    | 202103250 |
| Pablo Jose Oliva Bonilla       | 201700898 |

---

## Arquitectura

La aplicación TaskFlow + CloudDrive se desplegó utilizando servicios equivalentes de **AWS** y **Azure**. Ambas implementaciones siguen la misma arquitectura de dos capas: una web estática consumiendo servicios desde backend con balanceo de carga.

### AWS
- IAM: Creación de roles y políticas específicas por servicio.
- EC2: Dos instancias para backend en NodeJS y Python.
- ELB: Balanceo de carga entre las instancias EC2.
- S3: Almacenamiento de archivos estáticos y archivos de usuario.
- RDS: Base de datos para gestión de usuarios y tareas.
- Lambda: Funciones serverless para cargar archivos.
- API Gateway: Exposición de funciones serverless vía HTTP.

### Azure
- Azure VM: Dos instancias para backend en NodeJS y Python.
- Azure Load Balancer: Distribución de carga entre VMs.
- Azure Blob: Almacenamiento web y de archivos de usuario.
- Azure Functions: Funciones serverless para manejo de archivos.
- Azure API Management: Gestión de rutas API hacia Azure Functions.

---

## Usuarios IAM (AWS)

A continuación, se describen los usuarios IAM creados, sus roles y políticas asignadas:

### Usuario: `taskflow-uploader`
- **Políticas:**
  - `AmazonS3FullAccess`
  - `LambdaInvokeFunction`
  - `APIGatewayInvokeFullAccess`

### Usuario: `taskflow-ec2-backend`
- **Políticas:**
  - `AmazonEC2FullAccess`
  - `AmazonRDSFullAccess`

---

## Capturas de Pantalla

### AWS

#### Buckets de Amazon S3
![S3 Bucket](/IMG)

#### Instancias de EC2
![EC2 Instances](/IMG)

#### Balanceador de Carga (ELB)
![Load Balancer](/IMG)

#### Base de Datos (RDS)
![RDS](/IMG)

#### Funciones Lambda
![Lambda](/IMG)

#### API Gateway
![API Gateway](/IMG)

### Azure

#### Blob Containers
![Azure Blob](/IMG)

#### Instancias VM
![Azure VMs](/IMG)

#### Balanceador de carga
![Azure Load Balancer](/IMG)

#### Azure Functions
![Azure Functions](/IMG)

#### API Management
![API Management](/IMG)

---

## Conclusiones

Durante la implementación se observaron las siguientes diferencias entre AWS y Azure:

- **Facilidad de uso:** Azure tiene una interfaz más amigable para nuevos usuarios, pero AWS ofrece mayor granularidad de control.
- **Integración de servicios:** AWS permite una integración más directa entre Lambda y API Gateway, mientras que en Azure, la integración con Functions y API Management puede requerir más pasos.
- **Documentación:** AWS posee más documentación y casos de uso, mientras que Azure ofrece plantillas útiles y automatizaciones.

Ambas plataformas permiten lograr la misma solución, pero cada una presenta ventajas según la experiencia del equipo y los requisitos del proyecto.


# Manual de Usuario

