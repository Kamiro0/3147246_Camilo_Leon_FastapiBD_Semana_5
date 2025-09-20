3147246-Leon-Camilo-Fastapi-Semana-5
📌 Resumen Técnico – Semana 5

En esta semana avancé bastante en el manejo de conceptos de seguridad en APIs, específicamente en lo relacionado con login, autenticación y autorización usando FastAPI junto con JWT. El proyecto pasó de ser una API básica a convertirse en un sistema con gestión de usuarios y validaciones de acceso más confiables. Esto me permitió tener una visión más cercana a cómo funcionan las aplicaciones reales.

⚙️ Configuración del Entorno Local

Para evitar conflictos con el sistema y poder trabajar de manera ordenada, configuré el proyecto con:

📂 Entorno virtual propio: venv/ creado exclusivamente para este proyecto.

🔑 Git ajustado al repositorio: los cambios de usuario y correo solo aplican a este proyecto, no afectan la configuración global.

📦 Dependencias controladas: las librerías están aisladas y no interfieren con otros proyectos.

🚀 Pasos de Ejecución

Activar el entorno virtual:

source venv/Scripts/activate


Instalar dependencias necesarias:

pip install -r requirements.txt


Iniciar el servidor de desarrollo:

uvicorn main:app --reload

🛠️ Apuntes Técnicos Personales

📌 Git configurado únicamente para este repositorio.

📧 Se usó correo privado en GitHub para mayor seguridad.

🧪 Librerías aisladas dentro del entorno virtual.

🌐 El servidor corre en el puerto 8000, pero puede cambiarse si ya está en uso.

❗ Problemas Comunes y Soluciones
Problema	Posible Solución
El entorno virtual no activa	Eliminar y recrear con python -m venv venv
Puerto 8000 ocupado	Cambiar el puerto con --port en el comando uvicorn
Configuración de Git incorrecta	Revisar git config user.name y git config user.email
Cambiar correo en GitHub	Ajustar correo privado desde las opciones de GitHub
💭 Reflexión Personal – Semana 5

Lo más importante que aprendí fue a diferenciar bien autenticación de autorización: la primera se centra en confirmar quién es el usuario, mientras que la segunda establece qué permisos tiene dentro del sistema.

La implementación de JWT y el uso de hash en contraseñas me hizo ver la importancia de resguardar la información sensible, no solo para el login, sino pensando en posibles ataques o fugas de datos.

Finalmente, trabajar con roles de usuario me permitió imaginar cómo se aplicaría en un sistema real (administradores, usuarios normales, etc.), lo que le dio al proyecto una estructura más cercana a un entorno de producción.
