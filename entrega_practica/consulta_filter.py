from configuracion import Session
from crear_base_entidades import Consultorio

session = Session()

# Consultorios de la especialidad "Medicina general"
consultorios = session.query(Consultorio).filter(
    Consultorio.especialidad == "Medicina general"
).all()

for c in consultorios:
    print(f"{c.nombre} - {c.especialidad} - Clínica: {c.clinica.nombre_comercial}")

session.close()
