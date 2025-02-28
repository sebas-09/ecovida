# 🌟 ECOVIDA - Aplicación Web de Comercio Electrónico 🌟

## 📌 1. Introducción

ECOVIDA es una aplicación web de comercio electrónico desarrollada con una arquitectura de microservicios, diseñada para ofrecer una plataforma escalable, segura y eficiente para la compra y venta de productos de salud y bienestar.

El sistema cuenta con una separación clara entre servicios, lo que permite una mejor gestión del backend y una optimización del rendimiento en la comunicación entre microservicios. Además, la interfaz de administración permite a los usuarios con rol de administrador gestionar productos, categorías y órdenes de manera intuitiva.

---

## 🎯 2. Objetivos

- Desarrollar una aplicación de comercio electrónico basada en microservicios para mejorar la escalabilidad y modularidad del sistema.
- Implementar autenticación y autorización seguras mediante JWT y OAuth 2.0.
- Permitir la gestión eficiente de productos, categorías y pedidos mediante un panel de administración intuitivo.
- Asegurar la calidad del código en el backend utilizando **SonarQube**.
- Implementar pruebas automatizadas en el frontend con **Selenium** para validar la experiencia del usuario.
- Desplegar el sistema en un hosting gratuito asegurando su correcto funcionamiento.

---

## 🔍 3. Metodología

El desarrollo de PURELY se basa en una arquitectura de **microservicios**, asegurando modularidad y escalabilidad. La aplicación se compone de múltiples servicios independientes que se comunican mediante REST APIs y Eureka Service Registry.

### 📌 3.1. Diagrama de Arquitectura

![purely_archi](https://github.com/user-attachments/assets/eb0466cf-b6a0-464b-89e6-f44ac481f536)

### 📌 3.2. Endpoints

#### 📍 Servicio de Autenticación

El servicio de autenticación es responsable de verificar de forma segura las identidades de los usuarios y facilitar la autenticación basada en token

| HTTP Method                                                                                | Route Path            | Parameters | Description                                  |
| ------------------------------------------------------------------------------------------ | --------------------- | ---------- | -------------------------------------------- |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/auth/signin`        | -          | User login                                   |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/auth/signup`        | -          | User registration                            |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/auth/signup/verify` | code       | Validate registration one time password code |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/auth/isValidToken`  | token      | Validate json web token                      |

#### 📍 Servicio de Categorías

El servicio de categorías proporciona gestión de datos y operaciones centralizadas para categorías de productos.

| HTTP Method                                                                                | Route Path               | Parameters | Description              | Authentication | Role                |
| ------------------------------------------------------------------------------------------ | ------------------------ | ---------- | ------------------------ | -------------- | ------------------- |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/admin/category/create` | -          | Create new category      | Yes            | Admin               |
| <img alt="Static Badge" src="https://img.shields.io/badge/put-yellow?style=for-the-badge"> | `/admin/category/edit`   | categoryId | Edit existing category   | Yes            | Admin               |
| <img alt="Static Badge" src="https://img.shields.io/badge/delete-red?style=for-the-badge"> | `/admin/category/delete` | categoryId | Delete existing category | Yes            | Admin               |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/category/get/all`      | -          | Get all categories       | No             | Admin/User/Non user |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/category/get/byId`     | categoryId | Get category by id       | No             | Admin/User/Non user |

#### 📍 Servicio de Productos

El servicio de productos proporciona gestión centralizada de datos y operaciones para los productos disponibles.

| HTTP Method                                                                                | Route Path                | Parameters | Description             | Authentication | Role (Admin/User)   |
| ------------------------------------------------------------------------------------------ | ------------------------- | ---------- | ----------------------- | -------------- | ------------------- |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/admin/product/add`      | -          | Create new product      | Yes            | Admin               |
| <img alt="Static Badge" src="https://img.shields.io/badge/put-yellow?style=for-the-badge"> | `/admin/product/edit`     | productId  | Edit existing product   | Yes            | Admin               |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/product/get/all`        | -          | Get all products        | No             | Admin/User/Non user |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/product/get/byId`       | productId  | Get product by id       | No             | Admin/User/Non user |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/product/get/byCategory` | categoryId | Get product by category | No             | Admin/User/Non user |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/product/search`         | searchKey  | Search products by key  | No             | Admin/User/Non user |

#### 📍 Servicio de Carrito

El servicio de carrito proporciona gestión centralizada de datos y operaciones para los carritos de los usuarios.

| HTTP Method                                                                                | Route Path         | Parameter | Description                        | Authentication | Role (Admin/User) |
| ------------------------------------------------------------------------------------------ | ------------------ | --------- | ---------------------------------- | -------------- | ----------------- |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/cart/add`        | -         | Add item to cart, update quantity  | Yes            | User              |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/cart/get/byUser` | -         | Get cart details by user           | Yes            | User              |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/cart/get/byId`   | cartId    | Get cart details by cart id        | Yes            | User              |
| <img alt="Static Badge" src="https://img.shields.io/badge/delete-red?style=for-the-badge"> | `/cart/remove`     | productId | Remove an item from the cart       | Yes            | User              |
| <img alt="Static Badge" src="https://img.shields.io/badge/delete-red?style=for-the-badge"> | `/cart/clear/byId` | cartId    | Remove all the items from the cart | Yes            | User              |

#### 📍 Servicio de Ordenes

El Servicio de Pedidos proporciona gestión centralizada de datos y operaciones para pedidos.

| HTTP Method                                                                                | Route Path          | Parameter | Description        | Authentication | Role (Admin/User) |
| ------------------------------------------------------------------------------------------ | ------------------- | --------- | ------------------ | -------------- | ----------------- |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/order/create`     | -         | Place an order     | Yes            | User              |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/order/get/byUser` | -         | Get orders by user | Yes            | User              |
| <img alt="Static Badge" src="https://img.shields.io/badge/get-blue?style=for-the-badge">   | `/order/get/all`    | -         | Get all orders     | Yes            | Admin             |
| <img alt="Static Badge" src="https://img.shields.io/badge/delete-red?style=for-the-badge"> | `/order/cancel`     | orderId   | Cancel the order   | Yes            | User              |

#### 📍 Servicio de Notificación

El Servicio de Notificación proporciona operaciones centralizadas para enviar correos electrónicos a los usuarios.

| HTTP Method                                                                                | Route Path           | Description |
| ------------------------------------------------------------------------------------------ | -------------------- | ----------- |
| <img alt="Static Badge" src="https://img.shields.io/badge/post-green?style=for-the-badge"> | `/notification/send` | Send email  |

### 📌 3.3. Comunicación entre Microservicios

Se utiliza **Eureka Service Registry** para el descubrimiento de servicios y **Feign Client** para la comunicación entre microservicios.

### 📌 3.4. Cómo Ejecutar el Proyecto

#### 📍 Paso 1: Clonar el repositorio

```sh
git clone https://github.com/<tu-usuario>/Fullstack-E-commerce-web-application
```

#### 📍 Paso 2: Configurar las bases de datos en MongoDB

Crear las siguientes bases de datos:

- `purely_auth_service`
- `purely_category_service`
- `purely_product_service`
- `purely_cart_service`
- `purely_order_service`

#### 📍 Paso 3: Configurar el servicio de notificaciones

En el archivo `notification-service/src/main/resources/application.properties`:

```properties
spring.mail.username=TU_USUARIO
spring.mail.password=TU_CONTRASEÑA
```

#### 📍 Paso 4: Ejecutar los microservicios

1. Iniciar **Service Registry** (`http://localhost:8761`).
2. Iniciar los demás servicios asegurando su registro en Eureka.

#### 📍 Paso 5: Ejecutar el frontend

```sh
cd ./frontend
npm install
npm run dev
```

Acceder a [`http://localhost:5173/`](http://localhost:5173/).

### 📌 3.5. Capturas de Pantalla

![Screenshot 2024-05-07 194247](https://github.com/user-attachments/assets/6f0ea4eb-6757-4955-b64f-18fcca1cee96)
![Screenshot 2024-05-07 194417](https://github.com/user-attachments/assets/92dbbf00-5606-4530-982a-6cbd1748ee40)
![Screenshot 2024-05-07 195308](https://github.com/user-attachments/assets/affced2c-3ee5-46d6-96f2-399591b37995)

---

## 📊 4. Resultados y Pruebas de Calidad

### 📍 4.1. Pruebas con SonarQube en Backend

Se utilizó **SonarQube** para analizar la calidad del código de cada microservicio. Se evaluaron métricas clave como:

- **Duplicación de código**
- **Complejidad ciclomática**
- **Vulnerabilidades de seguridad**
- **Bugs y code smells**

Estas pruebas permitieron mejorar la mantenibilidad del código, reducir errores y optimizar el rendimiento del backend.

---

### 📍 4.2. Pruebas con Selenium en Frontend

Para garantizar el correcto funcionamiento del flujo administrativo, se automatizaron pruebas con **Selenium**, verificando:

1. **Inicio de sesión del administrador.**
2. **Creación de una nueva categoría.**
3. **Creación de un nuevo producto dentro de una categoría.**
4. **Visualización de órdenes en el panel de administración.**

Estas pruebas aseguran que la interfaz de administración sea funcional, intuitiva y libre de errores.

---

Este documento proporciona una visión detallada del desarrollo de PURELY, resaltando su arquitectura, metodologías y estrategias de prueba para garantizar un sistema eficiente y seguro.
