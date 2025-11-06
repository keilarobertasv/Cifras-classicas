from PyQt6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import string

ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class GraficoFrequencia(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.figure = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.figure)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        
        self.ax = self.figure.add_subplot(111)
        self.limpar_grafico()

    def limpar_grafico(self):
        self.ax.clear()
        
        self.ax.set_title("Gráfico de Frequência", color='#00FF00')
        self.ax.set_ylabel('Frequência (%)', color='#00FF00')
        self.ax.set_ylim(0, 30)

        self.figure.patch.set_facecolor('#0D0D0D')
        self.ax.set_facecolor('#1C1C1C')
        self.ax.spines['top'].set_color('#00FF00')
        self.ax.spines['bottom'].set_color('#00FF00')
        self.ax.spines['left'].set_color('#00FF00')
        self.ax.spines['right'].set_color('#00FF00')
        self.ax.xaxis.label.set_color('#00FF00')
        self.ax.yaxis.label.set_color('#00FF00')
        self.ax.tick_params(axis='x', colors='#00FF00', labelsize='small')
        self.ax.tick_params(axis='y', colors='#00FF00')
        
        self.ax.set_xticks(range(len(ALFABETO)))
        self.ax.set_xticklabels(ALFABETO, fontsize='small')

        self.figure.tight_layout()
        self.canvas.draw()

    def atualizar_grafico(self, frequencias_pct, titulo, total_letras):
        self.ax.clear()
        
        letras = list(frequencias_pct.keys())
        valores = list(frequencias_pct.values())
        
        titulo_completo = f"{titulo} (Total de Letras: {total_letras})"
        
        self.ax.bar(letras, valores, color='#00FF00')
        
        self.ax.set_title(titulo_completo, color='#00FF00')
        self.ax.set_ylabel('Frequência (%)', color='#00FF00')
        self.ax.set_ylim(bottom=0)

        self.figure.patch.set_facecolor('#0D0D0D')
        self.ax.set_facecolor('#1C1C1C')
        self.ax.spines['top'].set_color('#00FF00')
        self.ax.spines['bottom'].set_color('#00FF00')
        self.ax.spines['left'].set_color('#00FF00')
        self.ax.spines['right'].set_color('#00FF00')
        self.ax.xaxis.label.set_color('#00FF00')
        self.ax.yaxis.label.set_color('#00FF00')
        self.ax.tick_params(axis='x', colors='#00FF00', labelsize='small')
        self.ax.tick_params(axis='y', colors='#00FF00')

        self.figure.tight_layout()
        self.canvas.draw()