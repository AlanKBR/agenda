# config/agenda_config.py
class AgendaConfig:
    """Configuração para integração da agenda"""

    # Database settings
    DATABASE_URI = "postgresql://user:pass@localhost/clinica_db"

    # Table mappings - adapte para suas tabelas existentes
    TABLES = {
        "pacientes": "pacientes",
        "usuarios": "users",
        "eventos": "calendar_events",
    }

    # Field mappings - adapte para seus campos
    FIELDS = {
        "paciente": {
            "id": "id",
            "nome": "nome",
            "telefone": "celular",
            "email": "email",
        },
        "usuario": {"id": "id", "nome": "nome_profissional", "tipo": "cargo"},
        "evento": {
            "id": "id",
            "titulo": "title",
            "inicio": "start",
            "fim": "end",
            "cor": "color",
        },
    }

    # Authentication settings
    AUTH_REQUIRED = True
    AUTH_DECORATOR = "@login_required"

    # UI Settings
    DEFAULT_VIEW = "timeGridWeek"
    BUSINESS_HOURS = {
        "start": "08:00",
        "end": "18:00",
        "days": [1, 2, 3, 4, 5],  # Segunda a sexta
    }

    # Integration settings
    URL_PREFIX = "/agenda"
    TEMPLATE_FOLDER = "agenda/templates"
    STATIC_FOLDER = "agenda/static"
