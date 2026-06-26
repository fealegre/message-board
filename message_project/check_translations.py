import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'message_project.settings'
import django
django.setup()
from django.template.loader import render_to_string

html = render_to_string('base.html', {})
print('lang=es:', 'lang="es"' in html)
print('Blog Django title:', '<title>Blog Django</title>' in html)
print('Blog Django brand:', 'Blog Django</a>' in html)
print('Iniciar sesion:', 'Iniciar sesi\u00f3n' in html)
print('Registrarse:', 'Registrarse' in html)
print('Hola:', 'Hola' in html)
print('Nuevo Post:', 'Nuevo Post' in html)
print('Cerrar sesion:', 'Cerrar sesi\u00f3n' in html)

html2 = render_to_string('home.html', {'post_list': []})
print('Todos los posts:', 'Todos los posts' in html2)
print('Leer mas:', 'Leer m\u00e1s' in html2)
print('No hay posts:', 'No hay posts' in html2)
