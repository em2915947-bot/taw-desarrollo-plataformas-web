from datetime import date
from sqlalchemy import and_

from configuracion import Session
from crear_base_entidades import HistoriaClinica

session = Session()

# Historias de octubre de 2026 Y de la mascota "Toby"
historias = session.query(HistoriaClinica).filter(
    and_(
        HistoriaClinica.fecha_atencion >= date(2026, 10, 1),
        HistoriaClinica.fecha_atencion <= date(2026, 10, 31),
        HistoriaClinica.nombre_mascota == "Toby",
    )
).all()

for h in historias:
    print(f"{h.fecha_atencion} | {h.nombre_mascota} | {h.diagnostico}")

session.close()
