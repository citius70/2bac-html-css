
import zipfile
from datetime import datetime

# Crear el archivo ZIP en memoria
zip_filename = 'curso-html-css-mkdocs.zip'

# Leer los archivos que ya creé anteriormente (están como code_file en la conversación)
# Voy a recrear el contenido completo aquí

# Debido a la limitación de caracteres, voy a crear los archivos principales
# y generar el ZIP

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    
    # Archivo 1: README.md
    readme_content = '''# Curso HTML y CSS - Material para MkDocs

Este repositorio contiene todo el material didáctico del curso de HTML y CSS para 2º de Bachillerato.

## 🚀 Instalación

1. Instalar MkDocs y Material theme:
```bash
pip install -r requirements.txt
```

2. Ejecutar servidor local:
```bash
mkdocs serve
```

3. Abrir navegador en: http://127.0.0.1:8000/

## 📁 Estructura

```
curso-html-css/
├── docs/
│   ├── index.md
│   ├── apuntes/
│   │   ├── 01-introduccion.md
│   │   └── 02-html-basico.md
│   ├── ejercicios/
│   │   └── html-basico.md
│   ├── proyecto/
│   │   └── descripcion.md
│   └── recursos/
│       ├── html-cheatsheet.md
│       └── css-cheatsheet.md
├── mkdocs.yml
├── README.md
└── requirements.txt
```

## 📚 Contenido incluido

✅ **Apuntes teóricos**
- Módulo 1: Introducción al desarrollo web
- Módulo 2: HTML básico completo

✅ **Ejercicios prácticos**
- 13 ejercicios de HTML (básico, intermedio, avanzado)

✅ **Proyecto web progresivo**
- Descripción completa del proyecto
- 4 fases para 20 sesiones

✅ **Recursos de referencia**
- Cheatsheet HTML completo
- Cheatsheet CSS completo

## 📝 Despliegue

Para generar el sitio estático:
```bash
mkdocs build
```

Para desplegar en GitHub Pages:
```bash
mkdocs gh-deploy
```

## 👨‍🏫 Uso educativo

Material diseñado para:
- **Nivel**: 2º Bachillerato (estudiantes con nivel básico 2/10)
- **Duración**: 4-5 semanas (20 sesiones)
- **Formato**: Clases teóricas + práctica + proyecto

---

Creado con ❤️ para la enseñanza de HTML y CSS
'''
    zipf.writestr('README.md', readme_content)
    
    # Archivo 2: requirements.txt
    requirements = '''mkdocs>=1.5.0
mkdocs-material>=9.5.0
pymdown-extensions>=10.7
'''
    zipf.writestr('requirements.txt', requirements)
    
    # Archivo 3: mkdocs.yml
    mkdocs_config = '''site_name: Curso HTML y CSS - 2º Bachillerato
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
    - content.code.annotate

plugins:
  - search:
      lang: es

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - attr_list
  - md_in_html
  - tables
  - footnotes

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

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com
    - icon: fontawesome/solid/envelope
      link: mailto:profesor@ejemplo.com

copyright: Copyright &copy; 2025 - Curso HTML y CSS 2º Bachillerato
'''
    zipf.writestr('mkdocs.yml', mkdocs_config)
    
print(f"✅ ZIP creado: {zip_filename}")
print(f"📦 Tamaño: {os.path.getsize(zip_filename) / 1024:.2f} KB")
print("\n📝 Archivos base incluidos:")
print("   - README.md")
print("   - requirements.txt") 
print("   - mkdocs.yml")
print("\n⚠️  Nota: El ZIP está listo, pero necesito añadir el resto del contenido...")
print("   Los archivos de docs/ se añadirán en el siguiente paso.")
