# 📌 Proyecto Gestor de Usuarios (FastAPI + React Vite)

Este proyecto consiste en una **API de usuarios con FastAPI** y un **frontend en React Vite** que permite registrar, listar y eliminar usuarios, además de autenticarlos mediante login.

---

## ⚙️ Backend (FastAPI)

### 🚀 Instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/gestor-usuarios.git
   cd gestor-usuarios/backend

Crear entorno virtual:

python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

Instalar dependencias:

pip install -r requirements.txt

▶️ Ejecutar servidor
uvicorn main:app --reload


El backend estará disponible en:
👉 http://127.0.0.1:8000

📂 Estructura
backend/
│── main.py          # Punto de entrada FastAPI
│── database.py      # Conexión SQLite
│── models.py        # Modelos ORM
│── schemas.py       # Esquemas Pydantic
│── crud.py          # Funciones CRUD
│── routes.py        # Endpoints API
│── requirements.txt # Dependencias

🔑 Endpoints principales
Método	Endpoint	Descripción
GET	/usuarios	Listar usuarios
POST	/usuarios	Registrar un nuevo usuario
DELETE	/usuarios/{id}	Eliminar usuario por ID
POST	/login	Autenticar usuario (login)
🎨 Frontend (React + Vite + TypeScript)
🚀 Instalación

Ir a la carpeta del frontend:

cd ../frontend


Instalar dependencias:

npm install


Ejecutar en modo desarrollo:

npm run dev


El frontend estará disponible en:
👉 http://localhost:5173

📂 Estructura
frontend/
│── src/
│   ├── api.ts          # Conexión con el backend
│   ├── App.tsx         # Componente principal
│   ├── components/
│   │   ├── UsuarioList.tsx   # Lista de usuarios
│   │   ├── UsuarioForm.tsx   # Formulario registro
│   │   ├── LoginForm.tsx     # Formulario login
│── package.json
│── vite.config.ts

🔗 Conexión con API

En src/api.ts se definen las funciones:

export function getUsuarios(): Promise<any>;
export function addUsuario(usuario: any): Promise<any>;
export function deleteUsuario(id: number): Promise<any>;
export function registerUsuario(usuario: any): Promise<any>;
export function loginUsuario(credenciales: any): Promise<any>;

✅ Funcionalidades

Registro de usuarios 👤

Listado de usuarios 📋

Eliminación de usuarios ❌

Autenticación (Login) 🔑

📌 Requisitos

Python 3.10+

Node.js 18+

FastAPI

React + Vite

🧑‍💻 Autor

Desarrollado por Camilo Andrés León Roldán
📅 2025

💡 Reflexión

Este proyecto fue una oportunidad para integrar backend y frontend en un flujo real de desarrollo.
Con FastAPI se logró un backend rápido, seguro y modular; mientras que con React Vite se implementó una interfaz ligera y eficiente.

El mayor aprendizaje fue la importancia de la comunicación entre cliente y servidor, asegurando que ambos compartan un mismo lenguaje de datos (JSON) y gestionen correctamente los errores y validaciones.

Además, permitió aplicar buenas prácticas como:

Organización por capas (modelos, esquemas, rutas, CRUD).

Separación del frontend y backend para mayor escalabilidad.

Documentación clara de endpoints y funciones.
