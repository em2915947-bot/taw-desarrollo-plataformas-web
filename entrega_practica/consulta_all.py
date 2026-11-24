from configuracion import Session
from crear_base_entidades import Clinica

session = Session()

clinicas = session.query(Clinica).all()

print("CLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS")
print("-" * 60)
for clinica in clinicas:
    total = sum(
        len(vet.historias_clinicas)
        for consultorio in clinica.consultorios
        for vet in consultorio.veterinarios
    )
    print(f"{clinica.nombre_comercial} ({clinica.direccion}) -> {total} historias clínicas")

session.close()
