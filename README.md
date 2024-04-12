# Albercan Backend

Este proyecto está construido con **Django 5.0** y **Python 3.10**.

## Estructura del proyecto

El proyecto consta de los siguientes directorios y archivos principales:

- `.github`: Contiene los archivos de configuración de GitHub.
- `albercan_backend`: Contiene el código fuente del backend.
- `envs`: Contiene los archivos de entorno.
- `people`, `pet`, `structure`, `utils`: Contienen el código fuente de las diferentes partes del proyecto.

## Instalación y ejecución con Docker

Para instalar y ejecutar el proyecto con Docker, sigue estos pasos:

1. Construye la imagen de Docker:

```bash
docker build -t albercan_backend .
```

Para ejecutar el proyecto con Docker Compose:
```bash
docker-compose up
```

# Instalación y ejecución con Poetry
Para instalar y ejecutar el proyecto con Poetry, sigue estos pasos:

1. Instala las dependencias del proyecto:
```bash
poetry install
```

2. Ejecuta el servidor de desarrollo de Django:
```bash
poetry run python manage.py runserver
```