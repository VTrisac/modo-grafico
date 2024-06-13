from PyQt5.QtWidgets import *

def areatriangulo():
    base = float(CuadroBaseRadio.text())
    altura = float(CuadroAltura.text())
    area = (base * altura) / 2
    mensaje = "Resultado: %4.3f" % area
    resul.setText(mensaje)


def arearectangulo():
    base = float(CuadroBaseRadio.text())
    altura = float(CuadroAltura.text())
    area = base * altura
    mensaje = "Resultado: %4.3f" % area
    resul.setText(mensaje)


def areacilindro():
    PI = 3.141516
    radio = float(CuadroBaseRadio.text())
    altura = float(CuadroAltura.text())
    area = 2 * PI * radio * altura
    mensaje = "Resultado: %4.3f" % area
    resul.setText(mensaje)


app = QApplication([])
w = QWidget()
w.setWindowTitle("Cálculo de áreas")
w.resize(280, 100)

etiq1 = QLabel("Base / Radio:")
etiq2 = QLabel("Altura")
resul = QLabel("Resultado:")

CuadroBaseRadio = QLineEdit()
CuadroAltura = QLineEdit()


bTriangulo = QPushButton("Triángulo")
bRectangulo = QPushButton("Rectángulo")
bCilindro = QPushButton("Cilindro")
bTriangulo.clicked.connect(areatriangulo)
bRectangulo.clicked.connect(arearectangulo)
bCilindro.clicked.connect(areacilindro)

grid = QGridLayout()
grid.setSpacing(10)

grid.addWidget(etiq1, 1, 0)
grid.addWidget(CuadroBaseRadio, 1, 1)

grid.addWidget(etiq2, 2, 0)
grid.addWidget(CuadroAltura, 2, 1)

grid.addWidget(bTriangulo, 3, 0)
grid.addWidget(bRectangulo, 4, 0)
grid.addWidget(bCilindro, 5, 0)
grid.addWidget(resul, 4, 1)

w.setLayout(grid)
w.show()
app.exec_()


"""
from gi.repository import Gtk


def areatriangulo(boton):
    base = float(conector.get_object("base_radio").get_text())
    altura = float(conector.get_object("altura").get_text())
    area = (base * altura) / 2
    area = round(area, 3)
    etiqueta = conector.get_object("resultado")
    etiqueta.set_text(str(area))


def arearectangulo(boton):
    base = float(conector.get_object("base_radio").get_text())
    altura = float(conector.get_object("altura").get_text())
    area = base * altura
    area = round(area, 3)
    etiqueta = conector.get_object("resultado")
    etiqueta.set_text(str(area))


def areacilindro(boton):
    PI = 3.141516
    radio = float(conector.get_object("base_radio").get_text())
    altura = float(conector.get_object("altura").get_text())
    area = 2 * PI * radio * altura
    area = round(area, 3)
    etiqueta = conector.get_object("resultado")
    etiqueta.set_text(str(area))

conector = Gtk.Builder()
conector.add_from_file("areas.glade")

miboton1 = conector.get_object("triangulo")
miboton1.connect("clicked", areatriangulo)

miboton1 = conector.get_object("rectangulo")
miboton1.connect("clicked", arearectangulo)

miboton1 = conector.get_object("cilindro")
miboton1.connect("clicked", areacilindro)

ventana = conector.get_object("window1")
ventana.connect("delete-event", Gtk.main_quit)
ventana.show_all()
Gtk.main()
"""