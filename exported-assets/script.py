
import zipfile
import os
from io import BytesIO

# Crear el contenido de cada archivo
files_content = {
    'README.md': '''# Curso HTML y CSS - Material para MkDocs

## 📚 Descripción

Este repositorio contiene todo el material didáctico del curso de HTML y CSS para 2º de Bachillerato de Tecnología de la Información y Comunicación.

El contenido está estructurado en formato Markdown para ser usado con **MkDocs** y el tema **Material for MkDocs**.

## 🚀 Instalación rápida

1. Instalar MkDocs:
```bash
pip install mkdocs mkdocs-material
```

2. Ejecutar el servidor:
```bash
cd curso-html-css
mkdocs serve
```

3. Abrir en navegador: http://127.0.0.1:8000/

## 📁 Estructura

- `docs/` - Contiene todo el contenido en Markdown
- `mkdocs.yml` - Configuración de MkDocs
- `requirements.txt` - Dependencias Python

## 📚 Material incluido

✅ Módulo 1: Introducción al desarrollo web
✅ Módulo 2: HTML básico completo
✅ 13 ejercicios de HTML clasificados por nivel
✅ Descripción del proyecto web progresivo
✅ Cheatsheets de HTML y CSS

## 📝 Para continuar

Este es el material base. Faltan por desarrollar:
- Módulos 3-6 (HTML avanzado y CSS)
- Más ejercicios
- Fases detalladas del proyecto
- Tests de evaluación
''',
    
    'requirements.txt': '''mkdocs>=1.5.0
mkdocs-material>=9.5.0
pymdown-extensions>=10.7
''',
    
    'mkdocs.yml': '''site_name: Curso HTML y CSS - 2º Bachillerato
site_description: Material didáctico completo para aprender HTML y CSS desde cero
site_author: Profesor TIC 2º Bachillerato

theme:
  name: material
  language: es
  palette:
    - scheme: default
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-7
        name: Cambiar a modo oscuro
    - scheme: slate
      primary: indigo
      accent: blue
      toggle:
        icon: material/brightness-4
        name: Cambiar a modo claro
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - navigation.footer
    - search.suggest
    - search.highlight
    - content.code.copy

plugins:
  - search:
      lang: es

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - attr_list
  - tables

nav:
  - Inicio: index.md
  - Apuntes:
    - 01. Introducción: apuntes/01-introduccion.md
    - 02. HTML Básico: apuntes/02-html-basico.md
  - Ejercicios:
    - HTML Básico: ejercicios/html-basico.md
  - Proyecto Web:
    - Descripción General: proyecto/descripcion.md
  - Recursos:
    - Cheatsheet HTML: recursos/html-cheatsheet.md
    - Cheatsheet CSS: recursos/css-cheatsheet.md
'''
}

print("✅ Archivos de configuración creados")
print(f"   - README.md")
print(f"   - requirements.txt")
print(f"   - mkdocs.yml")
print("\n⏳ Los demás archivos de contenido se añadirán al ZIP...")
