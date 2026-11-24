from sqlalchemy import or_

from configuracion import Session
from crear_base_entidades import Consultorio

session = Session()

# Consultorios de Cirugía O Dermatología
consultorios = session.query(Consultorio).filter(
    or_(
        Consultorio.especialidad == "Cirugía",
        Consultorio.especialidad == "Dermatología",
    )
).all()

for c in consultorios:
    print(f"{c.nombre} - {c.especialidad}")

session.close()
