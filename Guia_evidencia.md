# ContaPYME Módulo web de usuarios

Laura Vanessa Herrera Cortes · Ficha 3336221 · GA7-220501096-AA2-EV02

La rúbrica presentada evalúa formularios procesados por vistas Django, GET y POST, plantillas DTL y versionamiento con Git. Este proyecto aplica ese enfoque al módulo de Usuarios del prototipo ContaPYME. Conserva la relación de usuario con empresa y rol del esquema existente.

## Ejecutar en Windows

1. Verifica que en MySQL existan las tablas `usuario`, `empresa` y `rol` de `software_contable_pymes`. Si usas la base ya creada, no vuelvas a importar el SQL. Si es una base nueva, ejecuta una vez el script de la carpeta base_datos. Para registrar desde el formulario, debe existir al menos una empresa y un rol.
2. Abre la carpeta del proyecto en VS Code. En PowerShell ejecuta:

   ```powershell
   python -m pip install -r requirements.txt
   $env:MYSQL_PASSWORD = Read-Host "Contraseña de MySQL" -MaskInput
   python manage.py check
   python manage.py runserver
   ```

   Si tu PowerShell es antiguo y no admite `-MaskInput`, abre PowerShell 7 o usa el prompt siguiente:

   ```powershell
   $clave = Read-Host "Contraseña de MySQL" -AsSecureString
   $env:MYSQL_PASSWORD = [System.Net.NetworkCredential]::new("", $clave).Password
   ```

   Se usan por defecto el puerto 3307 y el usuario root. Si configuraste otros, define `MYSQL_PORT` y `MYSQL_USER` en la misma terminal. Abre http://127.0.0.1:8000/ en el navegador. Django utiliza las tablas existentes con modelos no administrados.

## Demostración para la rúbrica

- Edición y eliminación. Abre Editar o Eliminar desde el listado. GET muestra el formulario o la confirmación. POST aplica los cambios. Prueba con un usuario de demostración creado para esta evidencia.
- La publicación del repositorio queda para la Entrega 3 según el instrumento de evaluación.

- POST. Completa el formulario con nombre, correo de prueba, empresa, rol, contraseña de al menos ocho caracteres y estado. El servidor valida los campos, protege la contraseña con un hash, guarda el registro y redirige al listado.
- GET. Busca el nombre o correo y selecciona el estado. La URL conserva los parámetros de búsqueda.
- DTL. En el HTML se muestran el ciclo `for`, las condiciones `if`, el token CSRF y el renderizado de los formularios.
- Git. Publica el proyecto desde su carpeta en un repositorio vacío nuevo, por ejemplo `ContaPYME-Web-AA2-EV02`. Usa el usuario que corresponda.

  ```powershell
  git init -b main
  git add .
  git commit -m "Codificar módulo web de usuarios de ContaPYME"
  git remote add origin https://github.com/TU_USUARIO/ContaPYME-Web-AA2-EV02.git
  git push -u origin main
  ```

  Si ya tienes Git inicializado, revisa primero `git status` y `git remote -v`. Después de publicar, coloca la URL real en `ENLACE_REPOSITORIO.txt`, guarda y vuelve a comprimir los archivos con el nombre `LAURAHERRERA_AA2_EV02.zip`.
