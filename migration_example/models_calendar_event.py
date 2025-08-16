# pyright: reportMissingImports=false, reportGeneralTypeIssues=false
# models/calendar_event.py
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

try:
    from your_main_app.database import Base  # type: ignore
except Exception:  # example placeholder for editor
    Base = object  # type: ignore[assignment]


class CalendarEvent(Base):
    __tablename__ = "calendar_events"

    id = Column(Integer, primary_key=True)
    title = Column(String(120), nullable=False)
    start = Column(String(30), nullable=False)
    end = Column(String(30), nullable=False)
    color = Column(String(20), nullable=True)

    # NOVO: Relacionamento direto com paciente
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=True)
    paciente = relationship("Paciente", back_populates="eventos")

    # NOVO: Relacionamento com profissional
    profissional_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    profissional = relationship("User", back_populates="eventos_agendados")

    def to_dict(self):
        from dateutil.parser import parse

        try:
            start_s = str(self.start)  # type: ignore[arg-type]
            end_s = str(self.end)  # type: ignore[arg-type]
            start_dt = parse(start_s)
            end_dt = parse(end_s)
            if len(start_s) == 10 and len(end_s) == 10:
                all_day = True
            elif (
                start_dt.hour == 0
                and start_dt.minute == 0
                and start_dt.second == 0
                and end_dt.hour == 0
                and end_dt.minute == 0
                and end_dt.second == 0
                and (end_dt - start_dt).total_seconds() % 86400 == 0
            ):
                all_day = True
            else:
                all_day = False
        except Exception:
            all_day = False

        return {
            "id": self.id,
            "title": self.title,
            "start": self.start,
            "end": self.end,
            "color": self.color,
            "allDay": all_day,
            "paciente_id": self.paciente_id,
            "paciente_nome": self.paciente.nome if self.paciente else None,
            "paciente_telefone": (self.paciente.celular if self.paciente else None),
            "profissional_id": self.profissional_id,
            "profissional_nome": (
                self.profissional.nome_profissional if self.profissional else None
            ),
        }
