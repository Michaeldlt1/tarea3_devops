# Flask Ejercicio 3 - CI/CD con GitHub Actions y GHCR

Este repositorio contiene una aplicación web construida con **Flask (Python 3.12)**. Incluye un flujo de trabajo automatizado de Integración y Despliegue Continuo (CI/CD) mediante **GitHub Actions** para empaquetar y publicar la aplicación en **GitHub Container Registry (GHCR)**.

## 🚀 Flujo de Trabajo (CI/CD)

Cada vez que realizas un `push` a la rama `main`, el flujo de trabajo ejecuta los siguientes pasos de forma automática:

1. **Clonado de Código:** Descarga el repositorio en el entorno virtual (`ubuntu-latest`).
2. **Entorno Python:** Configura Python 3.12 e instala las dependencias de `requirements.txt`.
3. **Construcción Docker:** Compila la imagen local del proyecto usando el `Dockerfile`.
4. **Autenticación en GHCR:** Inicia sesión de forma segura en el registro de contenedores de GitHub.
5. **Publicación:** Sube (pushea) la imagen etiquetada como `3.0.0` a GitHub Packages.

---

## ⚙️ Configuración del Secreto en GitHub

Para que el proceso de inicio de sesión de Docker funcione correctamente, debes registrar tu token de acceso en GitHub:

1. Genera un **Personal Access Token (classic)** desde tu cuenta de GitHub con los permisos `write:packages` y `read:packages`.
2. En este repositorio, ve a la pestaña **Settings** -> **Secrets and variables** -> **Actions**.
3. Haz clic en **New repository secret**.
4. Configura los siguientes campos:
   * **Name:** `TOKEN_WR`
   * **Secret:** *(Pega el token que generaste)*

---

## 🛠️ Archivo de Configuración (`.github/workflows/flask-ejercicio3.yml`)

El flujo utiliza la acción oficial de Docker para autenticarse, evitando errores de terminal interactiva (`non TTY device`):

```yaml
name: Flask ejercicio3

on:
  push:
    branches: [ "main" ]

permissions:
  contents: read
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python 3.12
      uses: actions/setup-python@v3
      with:
        python-version: "3.12"

    - name: Install dependencies
      run: |
         pip install -r requirements.txt

    - name: construir la imagen de Docker
      run: |
        docker build -t ghcr.io/michaeldlt1/ejercicio:3.0.0 .

    - name: login hacia github container registry
      uses: docker/login-action@v3
      with:
        registry: ghcr.io
        username: \${{ github.actor }}
        password: \${{ secrets.TOKEN_WR }}
      
    - name: publicar la imagen de Docker
      run: |
        docker push ghcr.io/michaeldlt1/ejercicio:3.0.0
```

---

## 📦 Descarga y Ejecución Local

Una vez completado el flujo de GitHub Actions, puedes descargar y correr el contenedor en cualquier máquina con Docker:

```bash
# 1. Iniciar sesión en el registro
echo "TU_PERSONAL_ACCESS_TOKEN" | docker login ghcr.io -u Michaeldlt1 --password-stdin

# 2. Descargar la imagen
docker pull ghcr.io/michaeldlt1/ejercicio:3.0.0

# 3. Ejecutar el contenedor
docker run -d -p 5000:5000 ghcr.io/michaeldlt1/ejercicio:3.0.0
```
