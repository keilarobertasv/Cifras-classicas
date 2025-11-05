import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QLineEdit,
    QMessageBox, QTabWidget, QFormLayout
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from cifras.cesar import cifrar as cifrar_cesar, decifrar as decifrar_cesar
from cifras.monoalfabetica import cifrar as cifrar_mono, decifrar as decifrar_mono
from cifras.playfair import cifrar as cifrar_playfair, decifrar as decifrar_playfair
from cifras.hill import cifrar as cifrar_hill, decifrar as decifrar_hill
from cifras.vigenere import cifrar as cifrar_vigenere, decifrar as decifrar_vigenere

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
        tab_mono = self.criar_tab_monoalfabetica()
        tab_playfair = self.criar_tab_playfair()
        tab_hill = self.criar_tab_hill()
        tab_vigenere = self.criar_tab_vigenere()
        
        self.tabs.addTab(tab_cesar, "Cifra de César")
        self.tabs.addTab(tab_mono, "Cifra Monoalfabética")
        self.tabs.addTab(tab_playfair, "Cifra de Playfair")
        self.tabs.addTab(tab_hill, "Cifra de Hill")
        self.tabs.addTab(tab_vigenere, "Cifra de Vigenère")
        
        layout_principal.addWidget(self.tabs)
        self.setLayout(layout_principal)

    def criar_tab_cesar(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_cesar_input = QLineEdit()
        self.chave_cesar_input.setPlaceholderText("Digite a chave")
        layout_chave.addRow(QLabel("Chave (1-25):"), self.chave_cesar_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_cesar = QTextEdit()
        self.texto_input_cesar.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_cesar)

        self.texto_output_cesar = QTextEdit()
        self.texto_output_cesar.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_cesar.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_cesar)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_cesar)
        decifrar_btn.clicked.connect(self.on_decifrar_cesar)
        
        return widget_tab

    def on_cifrar_cesar(self):
        try:
            texto = self.texto_input_cesar.toPlainText()
            chave = self.chave_cesar_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_cesar(texto, chave)
            self.texto_output_cesar.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_cesar(self):
        try:
            texto = self.texto_input_cesar.toPlainText()
            chave = self.chave_cesar_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_cesar(texto, chave)
            self.texto_output_cesar.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_monoalfabetica(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_mono_input = QLineEdit()
        self.chave_mono_input.setPlaceholderText("Digite o alfabeto embaralhado (26 letras únicas)")
        layout_chave.addRow(QLabel("Chave (A-Z):"), self.chave_mono_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_mono = QTextEdit()
        self.texto_input_mono.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_mono)

        self.texto_output_mono = QTextEdit()
        self.texto_output_mono.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_mono.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_mono)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_mono)
        decifrar_btn.clicked.connect(self.on_decifrar_mono)
        
        return widget_tab

    def on_cifrar_mono(self):
        try:
            texto = self.texto_input_mono.toPlainText()
            chave = self.chave_mono_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_mono(texto, chave)
            self.texto_output_mono.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_mono(self):
        try:
            texto = self.texto_input_mono.toPlainText()
            chave = self.chave_mono_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_mono(texto, chave)
            self.texto_output_mono.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_playfair(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_playfair_input = QLineEdit()
        self.chave_playfair_input.setPlaceholderText("Digite a palavra-chave")
        layout_chave.addRow(QLabel("Chave:"), self.chave_playfair_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_playfair = QTextEdit()
        self.texto_input_playfair.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_playfair)

        self.texto_output_playfair = QTextEdit()
        self.texto_output_playfair.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_playfair.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_playfair)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_playfair)
        decifrar_btn.clicked.connect(self.on_decifrar_playfair)
        
        return widget_tab

    def on_cifrar_playfair(self):
        try:
            texto = self.texto_input_playfair.toPlainText()
            chave = self.chave_playfair_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_playfair(texto, chave)
            self.texto_output_playfair.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_playfair(self):
        try:
            texto = self.texto_input_playfair.toPlainText()
            chave = self.chave_playfair_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_playfair(texto, chave)
            self.texto_output_playfair.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_hill(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_form = QFormLayout()
        
        self.m_hill_input = QLineEdit()
        self.m_hill_input.setPlaceholderText("Tamanho do bloco")
        layout_form.addRow(QLabel("Bloco (m):"), self.m_hill_input)
        
        self.chave_hill_input = QLineEdit()
        layout_form.addRow(QLabel("Chave (números):"), self.chave_hill_input)
        
        layout_tab.addLayout(layout_form)

        self.texto_input_hill = QTextEdit()
        self.texto_input_hill.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_hill)

        self.texto_output_hill = QTextEdit()
        self.texto_output_hill.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_hill.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_hill)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_hill)
        decifrar_btn.clicked.connect(self.on_decifrar_hill)
        
        return widget_tab

    def on_cifrar_hill(self):
        try:
            texto = self.texto_input_hill.toPlainText()
            chave = self.chave_hill_input.text()
            m = self.m_hill_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_hill(texto, chave, m)
            self.texto_output_hill.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave ou 'm': {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_hill(self):
        try:
            texto = self.texto_input_hill.toPlainText()
            chave = self.chave_hill_input.text()
            m = self.m_hill_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_hill(texto, chave, m)
            self.texto_output_hill.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave ou 'm': {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_vigenere(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_vigenere_input = QLineEdit()
        self.chave_vigenere_input.setPlaceholderText("Digite a palavra-chave")
        layout_chave.addRow(QLabel("Chave:"), self.chave_vigenere_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_vigenere = QTextEdit()
        self.texto_input_vigenere.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_vigenere)

        self.texto_output_vigenere = QTextEdit()
        self.texto_output_vigenere.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_vigenere.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_vigenere)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_vigenere)
        decifrar_btn.clicked.connect(self.on_decifrar_vigenere)
        
        return widget_tab

    def on_cifrar_vigenere(self):
        try:
            texto = self.texto_input_vigenere.toPlainText()
            chave = self.chave_vigenere_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_vigenere(texto, chave)
            self.texto_output_vigenere.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_vigenere(self):
        try:
            texto = self.texto_input_vigenere.toPlainText()
            chave = self.chave_vigenere_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_vigenere(texto, chave)
            self.texto_output_vigenere.setText(texto_decifrado)
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