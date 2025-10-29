#!/usr/bin/env python3
"""
Script para generar la estructura completa del curso HTML y CSS para MkDocs
Ejecutar: python genera_estructura.py
"""

import os

# Crear estructura de carpetas
folders = [
    'docs',
    'docs/apuntes',
    'docs/ejercicios',
    'docs/proyecto',
    'docs/recursos',
    'docs/evaluacion'
]

print("Creando estructura de carpetas...")
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"  ✓ {folder}")

print("\n✅ Estructura de carpetas creada correctamente!")
print("\n📝 Ahora copia el contenido de cada archivo:")
print("   1. index.md → docs/index.md")
print("   2. 01-introduccion.md → docs/apuntes/01-introduccion.md")
print("   3. 02-html-basico.md → docs/apuntes/02-html-basico.md")
print("   4. html-basico.md → docs/ejercicios/html-basico.md")
print("   5. descripcion.md → docs/proyecto/descripcion.md")
print("   6. html-cheatsheet.md → docs/recursos/html-cheatsheet.md")
print("   7. css-cheatsheet.md → docs/recursos/css-cheatsheet.md")
print("\n💡 Los archivos de contenido están en mensajes anteriores de esta conversación")
