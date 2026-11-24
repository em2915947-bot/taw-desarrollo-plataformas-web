from configuracion import Session
from crear_base_entidades import HistoriaClinica

session = Session()

# Historias clínicas ordenadas por fecha, de la más reciente a la más antigua
historias = session.query(HistoriaClinica).order_by(
    HistoriaClinica.fecha_atencion.desc()
).all()

for h in historias:
    print(f"{h.fecha_atencion} | {h.nombre_mascota} | {h.diagnostico}")

session.close()
