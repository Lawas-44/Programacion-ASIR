# Programación ASIR

Ejercicios de Python del módulo de Programación (1.º ASIR), siguiendo los [apuntes del módulo](https://joapuiib.github.io/asix-ip/apunts/).

## Estructura

- `ud1/` — Introducción: tipos de datos `int`, `float`, `bool` y ejercicios combinados.
- `ud2/` — Programación estructurada:
  - `seleccióon/` — Estructuras de selección (`if`, `match`).
  - `repetición/` — Estructuras de repetición (bucles).
  - `p1/` — Práctica 1.
- `ud3/` — Estructuras de datos:
  - `list/` — Listas, cadenas y matrices. `list_utils.py` es un módulo con funciones que reutilizan los demás ejercicios.
  - `dict/` — Diccionarios.
- `estructuras_datos/` — Práctica 2 (`text_analyzer.py`, `parse_groups.py`). Entregada con la etiqueta `P2`.

## Uso

Ejecuta cada ejercicio desde su propia carpeta, para que encuentre los módulos que importa (por ejemplo, `list_utils.py`):

```bash
cd ud3/list
python3 sort_list.py
```

Los ejercicios que leen ficheros del sistema reciben los datos por entrada estándar:

```bash
python3 ud3/list/parse_users.py < /etc/passwd
```

```bash
python3 estructuras_datos/parse_groups.py < /etc/group
```
