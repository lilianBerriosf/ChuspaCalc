Dentro del __init__, después de crear la lista de historial:

python
# Botón para comparar
self.btn_comparar = QPushButton("Comparar")
self.btn_comparar.clicked.connect(self._comparar_seleccion)
self.btn_comparar.setEnabled(False)
layout.addWidget(self.btn_comparar)
Conectar la selección:

python
self.lista_historial.itemSelectionChanged.connect(self._on_seleccion_cambiada)
Agregar estos métodos al final de la clase:

python
def _on_seleccion_cambiada(self):
    seleccionados = self.lista_historial.selectedItems()
    self.btn_comparar.setEnabled(len(seleccionados) == 2)

def _comparar_seleccion(self):
    from src.chuspacalc.ui.dialogo_comparar_historial import DialogoCompararHistorial
    seleccionados = self.lista_historial.selectedItems()
    if len(seleccionados) == 2:
        entrada1 = self._obtener_datos(seleccionados[0])
        entrada2 = self._obtener_datos(seleccionados[1])
        dialogo = DialogoCompararHistorial(entrada1, entrada2, self)
        dialogo.exec()

def _obtener_datos(self, item):
    return {"texto": item.text()}  # ajusta según tu estructura



"""
Diálogo para comparar dos entradas del historial lado a lado.
"""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QWidget, QScrollArea
)
from PySide6.QtCore import Qt


class DialogoCompararHistorial(QDialog):
    """Diálogo que muestra dos entradas del historial lado a lado."""

    def __init__(self, entrada1, entrada2, parent=None):
        super().__init__(parent)

        self.entrada1 = entrada1
        self.entrada2 = entrada2

        self.setWindowTitle("Comparación de Historial")
        self.setMinimumSize(800, 400)

        self._setup_ui()

    def _setup_ui(self):
        """Configura la interfaz del diálogo."""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Título
        titulo = QLabel("📊 Comparación de Entradas del Historial")
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo)

        # Contenedor de comparación
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QHBoxLayout()
        scroll_widget.setLayout(scroll_layout)

        # Entrada 1
        panel1 = self._crear_panel(self.entrada1, "Entrada 1")
        scroll_layout.addWidget(panel1)

        # Entrada 2
        panel2 = self._crear_panel(self.entrada2, "Entrada 2")
        scroll_layout.addWidget(panel2)

        scroll.setWidget(scroll_widget)
        layout.addWidget(scroll)

        # Botón cerrar
        btn_cerrar = QPushButton("Cerrar")
        btn_cerrar.clicked.connect(self.accept)
        layout.addWidget(btn_cerrar)

    def _crear_panel(self, entrada, titulo):
        """Crea un panel para una entrada del historial."""
        panel = QWidget()
        panel.setStyleSheet("""
            QWidget {
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 10px;
                margin: 5px;
            }
        """)
        panel_layout = QVBoxLayout()
        panel.setLayout(panel_layout)

        # Título del panel
        label_titulo = QLabel(f"📌 {titulo}")
        label_titulo.setStyleSheet("font-size: 14px; font-weight: bold;")
        panel_layout.addWidget(label_titulo)

        # Mostrar información de la entrada
        texto = self._formatear_entrada(entrada)
        label_info = QLabel(texto)
        label_info.setWordWrap(True)
        label_info.setStyleSheet("font-size: 12px;")
        panel_layout.addWidget(label_info)

        return panel

    def _formatear_entrada(self, entrada):
        """Formatea una entrada del historial para mostrarla."""
        if not entrada:
            return "No hay datos disponibles."

        lineas = []
        for clave, valor in entrada.items():
            if clave == "id":

        return "<br>".join(lineas)

