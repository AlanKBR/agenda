"""
Script simples para iniciar o app Flask.

Uso:
  - Via terminal:  A:/programa/agenda/venv/Scripts/python.exe iniciar.py
  - Ou com Python do sistema: python iniciar.py
"""

from agenda import create_app


def main() -> None:
    app = create_app()
    # Mantém o mesmo comportamento do __main__.py
    app.run(debug=True)


if __name__ == "__main__":
    main()
