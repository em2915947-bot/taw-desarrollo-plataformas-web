from datetime import date

from configuracion import Session
from crear_base_entidades import (
    Clinica, Consultorio, Veterinario, HistoriaClinica
)

session = Session()

# --- Clínicas ---
c1 = Clinica(nombre_comercial="VetCare Quito",
             direccion="Av. Amazonas N24-15, Quito",
             veterinario_responsable="Dr. Marcelo Andrade")
c2 = Clinica(nombre_comercial="PetSalud Guayaquil",
             direccion="Av. 9 de Octubre 1020, Guayaquil",
             veterinario_responsable="Dra. Lucía Paredes")
c3 = Clinica(nombre_comercial="Mascotas Felices Loja",
             direccion="Calle Bolívar 12-30, Loja",
             veterinario_responsable="Dr. Esteban Ríos")

# --- Consultorios ---
co1 = Consultorio(nombre="Consultorio 1", especialidad="Medicina general", clinica=c1)
co2 = Consultorio(nombre="Consultorio 2", especialidad="Cirugía", clinica=c1)
co3 = Consultorio(nombre="Consultorio A", especialidad="Dermatología", clinica=c2)
co4 = Consultorio(nombre="Consultorio B", especialidad="Medicina general", clinica=c2)
co5 = Consultorio(nombre="Consultorio 1", especialidad="Medicina general", clinica=c3)

# --- Veterinarios ---
v1 = Veterinario(nombres="Carlos", apellidos="Mena Torres",
                 correo="carlos.mena@vetcare.com",
                 licencia_profesional="LIC-0001", consultorio=co1)
v2 = Veterinario(nombres="Ana", apellidos="Salazar Vera",
                 correo="ana.salazar@vetcare.com",
                 licencia_profesional="LIC-0002", consultorio=co2)
v3 = Veterinario(nombres="Pedro", apellidos="Cedeño Loor",
                 correo="pedro.cedeno@petsalud.com",
                 licencia_profesional="LIC-0003", consultorio=co3)
v4 = Veterinario(nombres="María", apellidos="Bravo Intriago",
                 correo="maria.bravo@petsalud.com",
                 licencia_profesional="LIC-0004", consultorio=co4)
v5 = Veterinario(nombres="Jorge", apellidos="Armijos León",
                 correo="jorge.armijos@mascotasfelices.com",
                 licencia_profesional="LIC-0005", consultorio=co5)

# --- Historias clínicas ---
historias = [
    HistoriaClinica(fecha_atencion=date(2026, 9, 3), diagnostico="Otitis externa",
                    tratamiento="Gotas óticas por 10 días",
                    nombre_mascota="Max", veterinario=v1),
    HistoriaClinica(fecha_atencion=date(2026, 9, 10), diagnostico="Gastroenteritis",
                    tratamiento="Dieta blanda y probióticos",
                    nombre_mascota="Luna", veterinario=v1),
    HistoriaClinica(fecha_atencion=date(2026, 9, 15), diagnostico="Fractura de tibia",
                    tratamiento="Cirugía y reposo por 6 semanas",
                    nombre_mascota="Rocky", veterinario=v2),
    HistoriaClinica(fecha_atencion=date(2026, 10, 1), diagnostico="Dermatitis alérgica",
                    tratamiento="Antihistamínico y baño medicado",
                    nombre_mascota="Bella", veterinario=v3),
    HistoriaClinica(fecha_atencion=date(2026, 10, 5), diagnostico="Sarna",
                    tratamiento="Ivermectina según peso",
                    nombre_mascota="Toby", veterinario=v3),
    HistoriaClinica(fecha_atencion=date(2026, 10, 12), diagnostico="Control y vacunación",
                    tratamiento="Vacuna múltiple",
                    nombre_mascota="Nina", veterinario=v4),
    HistoriaClinica(fecha_atencion=date(2026, 11, 2), diagnostico="Parásitos intestinales",
                    tratamiento="Desparasitante oral",
                    nombre_mascota="Simba", veterinario=v5),
]

session.add_all([c1, c2, c3])
session.add_all(historias)
session.commit()
session.close()

print("Datos ingresados correctamente.")
