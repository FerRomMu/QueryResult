# ChromaDB Query Result Handler

## Descripción

El módulo **ChromaDB Query Result Handler** (aka queryresults) es una biblioteca ligera y agnóstica diseñada para facilitar el manejo de resultados de consultas a la base de datos ChromaDB. Permite acceder a resultados de embeddings de manera intuitiva, evitando la complejidad de manejar múltiples sublistas y diccionarios.

## Características

- **Acceso Simplificado**: Proporciona una interfaz simple para acceder a los resultados de la consulta mediante índices y claves.
- **Manejo de Errores**: Se encarga de posibles valores `None` en la metadata u otros campos y permite calcular el tamaño de la colección de manera confiable.
- **Estructura Flexible**: Adaptable a cualquier tipo de embedding y metadata, ideal para proyectos que requieren un manejo dinámico de datos.

## Instalación

Puedes instalar el módulo utilizando `pip`. Ejecuta el siguiente comando:

```bash
pip install git+https://github.com/FerRomMu/QueryResult.git
```

## Uso

Puedes ver un ejemplo de uso en este [nb](example/getting_started.ipynb).

## Contribución
Cree este modulo por necesidad. Comprendo que puede no estar optimizado porque fue creado con el objetivo de mejorar mi flujo de trabajo personal. De todos modos, si tienes alguna sugerencia puedes armar un PR. En mi tiempo libre estaré encantado de revisarlo.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
Si tienes preguntas o comentarios, no dudes en ponerte en contacto:

- Autor: Romero Muñoz Fernando Mario.
- Email: fer.rom.mu.dev@gmail.com

