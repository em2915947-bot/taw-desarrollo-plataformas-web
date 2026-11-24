from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from configuracion import engine

Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_comercial = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    veterinario_responsable = Column(String(100), nullable=False)

    consultorios = relationship(
        "Consultorio", back_populates="clinica", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Clinica(id={self.id}, nombre='{self.nombre_comercial}')>"


class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)  # nombre o número
    especialidad = Column(String(100), nullable=False)
    clinica_id = Column(Integer, ForeignKey("clinicas.id"), nullable=False)

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship(
        "Veterinario", back_populates="consultorio", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Consultorio(id={self.id}, nombre='{self.nombre}', especialidad='{self.especialidad}')>"


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False, unique=True)
    licencia_profesional = Column(String(50), nullable=False, unique=True)
    consultorio_id = Column(Integer, ForeignKey("consultorios.id"), nullable=False)

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias_clinicas = relationship(
        "HistoriaClinica", back_populates="veterinario", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Veterinario(id={self.id}, {self.nombres} {self.apellidos})>"


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_atencion = Column(Date, nullable=False)
    diagnostico = Column(String(200), nullable=False)
    tratamiento = Column(String(300), nullable=False)
    nombre_mascota = Column(String(100), nullable=False)
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"), nullable=False)

    veterinario = relationship("Veterinario", back_populates="historias_clinicas")

    def __repr__(self):
        return f"<HistoriaClinica(id={self.id}, mascota='{self.nombre_mascota}', fecha={self.fecha_atencion})>"


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("Base de datos y tablas creadas correctamente.")
