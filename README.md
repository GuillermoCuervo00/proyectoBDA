# Proyecto RAG - Sistema de Recuperación de Información

Este proyecto permite generar, consultar y visualizar información mediante archivos de texto y PDF utilizando bases de datos locales. La funcionalidad incluye tanto ejecución por consola como una interfaz web simple.
Requisitos

    Python (versión 3.8 o superior).
    Conda (para la gestión de entornos virtuales).

## Instalación y configuración
### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

git clone https://github.com/tu_usuario/proyectoRAG.git
cd proyectoRAG

### 2. Importar el entorno Conda

A partir del archivo environment.yml, crea e importa el entorno con el siguiente comando:

conda env create -f environment.yml
conda activate proyectoRAG

### Generación y consulta de la base de datos
1. Generar la base de datos de texto

Para crear la base de datos con información de texto, ejecuta:

python rag_createdb.py

2. Consultar la base de datos de texto

Una vez generada la base de datos, puedes realizar consultas ejecutando:

python rag_readdb.py

Visualización mediante interfaz web

Puedes visualizar y consultar la base de datos a través de una interfaz web local. Ejecuta:

python rag_gui.py

### La interfaz estará disponible en tu IP local en la siguiente dirección:

http://127.0.0.1:8000

### Trabajo con PDFs
1. Generar la base de datos con PDFs

Para añadir información desde archivos PDF a la base de datos, ejecuta:

python rag_pdf_createdb.py

2. Consultar la base de datos con PDFs

Una vez añadidos los datos, realiza consultas ejecutando:

python rag_pdf_reader.py

## Estructura del proyecto

    rag_createdb.py: Genera la base de datos de texto.
    rag_readdb.py: Permite realizar preguntas sobre la base de datos de texto.
    rag_gui.py: Visualiza y consulta la base de datos mediante una interfaz web en 127.0.0.1.
    rag_pdf_createdb.py: Genera la base de datos a partir de PDFs.
    rag_pdf_reader.py: Permite realizar preguntas sobre la base de datos creada a partir de PDFs.
    environment.yml: Configuración del entorno Conda.

## Ejecución rápida

    Generar base de datos de texto:

python rag_createdb.py

Consultar base de datos de texto:

python rag_readdb.py

Visualización web:

python rag_gui.py

Generar base de datos de PDFs:

python rag_pdf_createdb.py

Consultar base de datos de PDFs:

    python rag_pdf_reader.py

Notas adicionales

    Asegúrate de que todas las dependencias están correctamente instaladas utilizando el archivo environment.yml.
    La interfaz web solo funciona localmente en 127.0.0.1 por defecto.
    La base de datos debe generarse antes de ejecutar las consultas.
