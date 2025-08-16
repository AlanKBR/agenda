# pyright: basic
# agenda_blueprint.py
from flask import Blueprint, jsonify, render_template, request

try:
    from your_main_app.models import CalendarEvent, Paciente  # type: ignore
except Exception:  # example code; stubs to silence editor warnings

    class _QueryStub:
        def filter(self, *args, **kwargs):  # type: ignore[no-untyped-def]
            return self

        def limit(self, *args, **kwargs):  # type: ignore[no-untyped-def]
            return self

        def all(self):  # type: ignore[no-untyped-def]
            return []

        def first(self):  # type: ignore[no-untyped-def]
            return None

    class _Field:
        def ilike(self, *args, **kwargs):  # type: ignore[no-untyped-def]
            return object()

    class _Stub:
        query = _QueryStub()
        nome = _Field()  # for ilike access
        celular = ""

    CalendarEvent = _Stub  # type: ignore[assignment]
    Paciente = _Stub  # type: ignore[assignment]

agenda_bp = Blueprint(
    "agenda",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/agenda",
)


@agenda_bp.route("/")
def index():
    return render_template("agenda/calendar.html")


@agenda_bp.route("/events")
def get_events():
    events = CalendarEvent.query.all()
    return jsonify([event.to_dict() for event in events])


@agenda_bp.route("/buscar_nomes")
def buscar_nomes():
    query = request.args.get("q", "").strip()
    nomes = []

    if query and len(query) >= 2:
        # Usar models do sistema principal
        pacientes = (
            Paciente.query.filter(Paciente.nome.ilike(f"%{query}%")).limit(10).all()
        )

        for paciente in pacientes:
            nomes.append(paciente.nome)

    return jsonify(nomes[:15])


@agenda_bp.route("/buscar_telefone")
def buscar_telefone():
    nome = request.args.get("nome", "").strip()

    if not nome:
        return jsonify({"telefone": None})

    # Usar ORM do sistema principal
    paciente = Paciente.query.filter(Paciente.nome.ilike(f"%{nome}%")).first()

    if paciente and paciente.celular:
        return jsonify({"telefone": paciente.celular})

    return jsonify({"telefone": None})


# ... outros endpoints adaptados
