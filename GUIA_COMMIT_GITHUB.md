# Guia para guardar cambios y subirlos a GitHub

## 1. Revisar los cambios

Guarda tus archivos en VS Code y abre la terminal integrada en la carpeta del proyecto. Comprueba en que rama estas y que archivos cambiaron:

```powershell
git branch --show-current
git status
```

En este proyecto, normalmente debes trabajar en la rama `main`.

## 2. Preparar los cambios

Para incluir todos los archivos modificados y nuevos, ejecuta:

```powershell
git add .
```

Si solo quieres incluir un archivo, reemplaza la ruta por la del archivo:

```powershell
git add nombre-del-archivo.py
```

Antes de continuar, revisa que solo hayas agregado los archivos que quieres publicar:

```powershell
git status
```

## 3. Crear un commit

Un commit guarda una version de los cambios en el historial del proyecto. Escribe un mensaje corto que describa lo que hiciste:

```powershell
git commit -m "Describe brevemente los cambios"
```

Por ejemplo:

```powershell
git commit -m "Actualiza clases de animales"
```

## 4. Subir el commit a GitHub

Sube los cambios de la rama `main` al repositorio remoto:

```powershell
git push origin main
```

## 5. Confirmar que se subieron

Abre el repositorio en GitHub, selecciona la rama `main` y comprueba que aparecen tus archivos y el nuevo commit.

## Si Git dice que no hay cambios

Comprueba que guardaste los archivos y vuelve a ejecutar `git status`. Si no hay cambios nuevos, no hace falta crear otro commit.

## Si GitHub solicita iniciar sesion

Inicia sesion en GitHub desde VS Code y vuelve a ejecutar `git push origin main`. No escribas contrasenas ni tokens dentro de los comandos de Git.