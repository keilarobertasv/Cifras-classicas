import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QLineEdit,
    QMessageBox, QTabWidget, QFormLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from cifras.cesar import cifrar as cifrar_cesar, decifrar as decifrar_cesar

class CriptoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cifras Clássicas')
        self.setWindowIcon(QIcon('icon.png')) 
        self.resize(600, 500)
        self.initUI()

    def initUI(self):
        layout_principal = QVBoxLayout()
        
        self.tabs = QTabWidget()
        
        tab_cesar = self.criar_tab_cesar()
        
        self.tabs.addTab(tab_cesar, "Cifra de César")
        
        layout_principal.addWidget(self.tabs)
        self.setLayout(layout_principal)

    def criar_tab_cesar(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_cesar_input = QLineEdit()
        self.chave_cesar_input.setPlaceholderText("Digite a chave (ex: 3)")
        layout_chave.addRow(QLabel("Chave (1-25):"), self.chave_cesar_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input = QTextEdit()
        self.texto_input.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input)

        self.texto_processado_output = QTextEdit()
        self.texto_processado_output.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_processado_output.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_processado_output)

        botoes_layout = QHBoxLayout()
        self.cifrar_btn = QPushButton("Cifrar")
        self.decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(self.cifrar_btn)
        botoes_layout.addWidget(self.decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        self.cifrar_btn.clicked.connect(self.on_cifrar_cesar)
        self.decifrar_btn.clicked.connect(self.on_decifrar_cesar)
        
        return widget_tab

    def on_cifrar_cesar(self):
        try:
            texto = self.texto_input.toPlainText()
            chave = self.chave_cesar_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_cesar(texto, chave)
            self.texto_processado_output.setText(texto_cifrado)
            
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_cesar(self):
        try:
            texto = self.texto_input.toPlainText()
            chave = self.chave_cesar_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_cesar(texto, chave)
            self.texto_processado_output.setText(texto_decifrado)

        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")
            
    def mostrar_erro(self, mensagem):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle("Erro de Validação")
        msg_box.exec()