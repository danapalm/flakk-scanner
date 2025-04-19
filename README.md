# 🕷️ FLAKK - Custom Web Scanner v0.3.1

**FLAKK** es un escáner de subdominios simple, personalizable e interactivo, diseñado para ayudarte a encontrar subdominios activos en un dominio objetivo.  
Incluye una interfaz de consola amigable con navegación por teclado (flechas) gracias a `InquirerPy` y colores con `colorama` para resaltar resultados importantes.

---

## 📦 Características

- Escaneo multihilo de subdominios comunes
- Menú interactivo con flechas (`InquirerPy`)
- Soporte de colores para mejorar la lectura (`colorama`)
- Visuales en consola con arte ASCII (`pyfiglet`)
- Limpieza automática de la terminal
- Opción de repetir escaneos o salir fácilmente

---

## 📁 Estructura del Proyecto

```bash
FLAKK/
├── scripts/
│   └── simple_domains.py        # Módulo que contiene el escáner de subdominios
│
├── flakk.py                     # Archivo principal que ejecuta el menú interactivo
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Dependencias necesarias
└── __init__.py                  # (opcional, para tratar como paquete)
```
