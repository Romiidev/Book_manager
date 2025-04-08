from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from flask_migrate import Migrate
from sqlalchemy import create_engine, Numeric, Boolean, CheckConstraint, String, Integer


app = Flask(__name__)

USER_DB = "postgres"
USER_PASSWORD = "55575664"
SERVER_BD = "localhost"
NAME_DB = "Libros_biblio"
FULL_URL_DB = f"postgresql://{USER_DB}:{USER_PASSWORD}@{SERVER_BD}/{NAME_DB}"

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB

db = SQLAlchemy(app) 
#Migracion de la tabla con un objeto migrate 

migrate = Migrate()
migrate.init_app(app, db)

#Modelo de la tabla

class Libreria(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(100), unique= False , nullable=False)
    editorial : Mapped[str] = mapped_column(String(100),unique =False)
    anio : Mapped[int] = mapped_column(nullable=False)
    genero : Mapped[str] = mapped_column(String(100), nullable=False)
    precio : Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    forma_digital : Mapped[bool] = mapped_column(Boolean, nullable= False)
    
    def __str__(self):
        return (
            f"id : {self.id},"
            f"nombre : {self.nombre},"
            f"editorial : {self.editorial},"
            f"anio : {self.anio},"
            f"genero : {self.genero},"
            f"precio : {self.precio},"
            f"forma_digital : {self.forma_digital},"

        )
