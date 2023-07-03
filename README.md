# ODS4 Backend
## Solución
Esta RestAPI es solo una parte de la solución que tiene como objetivo promover el desarrollo sostenible de la educación de calidad.

La herramienta en general, contando con la RestAPI y la web, va dirigida a profesores que quieran enseñar a sus alumnos sobre desarrollo sostenible, cuando probablemente no tengan tiempo para preparar la clase. La aplicación web va a generar clases teóricas y preguntas sobre la ODS que el profesor haya elegido previamente, todo esto usando inteligencia artificial.

## Como he aplicado lo aprendido en el curso
1. He usado diccionarios que se vio en el microcurso de **Python Data Structures** para almacenar información básica sobre las ODS.
2. Ya habia usado BeautifulSoup para hacer web scraping antes, asi que probe con otra libreria para aplicar esta tecnica y automatizar tareas y esta es **Selenium**
3. Aplique conceptos de REST en este proyecto asi como manejo de JSON para la respuesta. Todo esto se vio en el microcurso **Using Python to Access Web Data**

## Requisitos
- **TENER PYTHON INSTALADO**

## Instalación
- Clonar el proyecto
- Dentro del proyecto clonado abrir una terminal:

    1.  Instalar y cargar el entorno virtual para usar Python y otras dependencias (tarda un poco).
        ```bash:
        pip install virtualenv
        python -m venv venv
        ```
    2. Iniciar el entorno virtual, en mi caso uso *.ps1* porque utilizo Windows.
        ```bash:
        & ./venv/Scripts/Activate.ps1
        ```
    3. Instalar las dependencias o librerias.
        ```bash:
        pip install -r ./requirements.txt
        ```
    4. Iniciar el servidor.
        ```bash:
        uvicorn main:app --reload
        ```
        Normalmente se inicia en el puerto 8000, asi que vas a tu navegador y en la barra de direcciones debes colocar: **localhost:8000**
- Listo ya tienes la API corriendo de manera local.
