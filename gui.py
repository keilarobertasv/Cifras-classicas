import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QTextEdit, QLineEdit,
    QMessageBox, QTabWidget, QFormLayout, QSplitter
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from cifras.cesar import cifrar as cifrar_cesar, decifrar as decifrar_cesar
from cifras.monoalfabetica import cifrar as cifrar_mono, decifrar as decifrar_mono
from cifras.playfair import cifrar as cifrar_playfair, decifrar as decifrar_playfair
from cifras.hill import cifrar as cifrar_hill, decifrar as decifrar_hill
from cifras.vigenere import cifrar as cifrar_vigenere, decifrar as decifrar_vigenere
from cifras.vernam import cifrar as cifrar_vernam, decifrar as decifrar_vernam
from cifras.otp import cifrar as cifrar_otp, decifrar as decifrar_otp
from cifras.railfence import cifrar as cifrar_railfence, decifrar as decifrar_railfence
from cifras.transcolunas import cifrar as cifrar_colunar, decifrar as decifrar_colunar
from cifras.doubletrans import cifrar as cifrar_doubletrans, decifrar as decifrar_doubletrans
from cifras.keycipher import cifrar as cifrar_keycipher, decifrar as decifrar_keycipher

from criptoanalise.criptoanalise import calcular_frequencia
from criptoanalise.analise_grafico import GraficoFrequencia

class CriptoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cifras Clássicas')
        self.setWindowIcon(QIcon('icon.png')) 
        self.resize(700, 700)
        self.initUI()

    def initUI(self):
        layout_principal = QVBoxLayout()
        
        self.main_tabs = QTabWidget()
        
        tab_cifragem = self.criar_aba_cifragem()
        tab_analise = self.criar_aba_criptoanalise()
        
        self.main_tabs.addTab(tab_cifragem, "Cifras")
        self.main_tabs.addTab(tab_analise, "Criptoanálise")
        
        layout_principal.addWidget(self.main_tabs)
        self.setLayout(layout_principal)
        
    def criar_aba_cifragem(self):
        widget_aba = QWidget()
        layout_aba = QVBoxLayout(widget_aba)
        
        self.cipher_tabs = QTabWidget()
        
        tab_cesar = self.criar_tab_cesar()
        tab_mono = self.criar_tab_monoalfabetica()
        tab_playfair = self.criar_tab_playfair()
        tab_hill = self.criar_tab_hill()
        tab_vigenere = self.criar_tab_vigenere()
        tab_vernam = self.criar_tab_vernam()
        tab_otp = self.criar_tab_otp()
        tab_railfence = self.criar_tab_railfence()
        tab_colunar = self.criar_tab_colunar()
        tab_doubletrans = self.criar_tab_doubletrans()
        tab_keycipher = self.criar_tab_keycipher()
        
        self.cipher_tabs.addTab(tab_cesar, "Cifra de César")
        self.cipher_tabs.addTab(tab_mono, "Cifra Monoalfabética")
        self.cipher_tabs.addTab(tab_playfair, "Cifra de Playfair")
        self.cipher_tabs.addTab(tab_hill, "Cifra de Hill")
        self.cipher_tabs.addTab(tab_vigenere, "Cifra de Vigenère")
        self.cipher_tabs.addTab(tab_vernam, "Cifra de Vernam")
        self.cipher_tabs.addTab(tab_otp, "One-Time Pad")
        self.cipher_tabs.addTab(tab_railfence, "Rail Fence")
        self.cipher_tabs.addTab(tab_colunar, "Transposição Colunar")
        self.cipher_tabs.addTab(tab_doubletrans, "Dupla Transposição")
        self.cipher_tabs.addTab(tab_keycipher, "KeyCipher")
        
        layout_aba.addWidget(self.cipher_tabs)
        return widget_aba

    def criar_aba_criptoanalise(self):
        widget_aba = QWidget()
        layout_aba = QVBoxLayout(widget_aba)

        layout_textos = QHBoxLayout()
        
        layout_texto1 = QVBoxLayout()
        self.texto_analise_1 = QTextEdit()
        self.texto_analise_1.setPlaceholderText("Cole o Texto Original aqui...")
        layout_texto1.addWidget(QLabel("Texto 1 (Original):"))
        layout_texto1.addWidget(self.texto_analise_1)
        
        layout_texto2 = QVBoxLayout()
        self.texto_analise_2 = QTextEdit()
        self.texto_analise_2.setPlaceholderText("Cole o Texto Cifrado aqui...")
        layout_texto2.addWidget(QLabel("Texto 2 (Cifrado):"))
        layout_texto2.addWidget(self.texto_analise_2)
        
        layout_textos.addLayout(layout_texto1)
        layout_textos.addLayout(layout_texto2)
        
        layout_aba.addLayout(layout_textos)

        layout_graficos = QHBoxLayout()
        self.grafico_1 = GraficoFrequencia()
        self.grafico_2 = GraficoFrequencia()
        layout_graficos.addWidget(self.grafico_1)
        layout_graficos.addWidget(self.grafico_2)
        
        layout_aba.addLayout(layout_graficos)

        self.analisar_btn = QPushButton("Analisar Frequência")
        self.analisar_btn.clicked.connect(self.on_analisar_frequencia)
        layout_aba.addWidget(self.analisar_btn)
        
        return widget_aba
        
    def on_analisar_frequencia(self):
        texto1 = self.texto_analise_1.toPlainText()
        texto2 = self.texto_analise_2.toPlainText()
        
        if not texto1 and not texto2:
            self.mostrar_erro("Preencha pelo menos um dos campos de texto.")
            return

        frequencia1, total1 = calcular_frequencia(texto1)
        frequencia2, total2 = calcular_frequencia(texto2)
        
        self.grafico_1.atualizar_grafico(frequencia1, "Frequência do Texto 1", total1)
        self.grafico_2.atualizar_grafico(frequencia2, "Frequência do Texto 2", total2)

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
        self.chave_mono_input.setPlaceholderText("Alfabeto de 26 letras únicas")
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
        self.chave_hill_input.setPlaceholderText("Números separados por espaço")
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

    def criar_tab_vernam(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_vernam_input = QLineEdit()
        self.chave_vernam_input.setPlaceholderText("Digite a chave")
        layout_chave.addRow(QLabel("Chave:"), self.chave_vernam_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_vernam = QTextEdit()
        self.texto_input_vernam.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_vernam)

        self.texto_output_vernam = QTextEdit()
        self.texto_output_vernam.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_vernam.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_vernam)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_vernam)
        decifrar_btn.clicked.connect(self.on_decifrar_vernam)
        
        return widget_tab

    def on_cifrar_vernam(self):
        try:
            texto = self.texto_input_vernam.toPlainText()
            chave = self.chave_vernam_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_vernam(texto, chave)
            self.texto_output_vernam.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_vernam(self):
        try:
            texto = self.texto_input_vernam.toPlainText()
            chave = self.chave_vernam_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_vernam(texto, chave)
            self.texto_output_vernam.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_otp(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_otp_input = QLineEdit()
        self.chave_otp_input.setPlaceholderText("Digite a chave (tão longa quanto o texto)")
        layout_chave.addRow(QLabel("Chave:"), self.chave_otp_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_otp = QTextEdit()
        self.texto_input_otp.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_otp)

        self.texto_output_otp = QTextEdit()
        self.texto_output_otp.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_otp.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_otp)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_otp)
        decifrar_btn.clicked.connect(self.on_decifrar_otp)
        
        return widget_tab

    def on_cifrar_otp(self):
        try:
            texto = self.texto_input_otp.toPlainText()
            chave = self.chave_otp_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_otp(texto, chave)
            self.texto_output_otp.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_otp(self):
        try:
            texto = self.texto_input_otp.toPlainText()
            chave = self.chave_otp_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_otp(texto, chave)
            self.texto_output_otp.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_railfence(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_railfence_input = QLineEdit()
        self.chave_railfence_input.setPlaceholderText("Digite o número de trilhos")
        layout_chave.addRow(QLabel("Chave (Trilhos):"), self.chave_railfence_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_railfence = QTextEdit()
        self.texto_input_railfence.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_railfence)

        self.texto_output_railfence = QTextEdit()
        self.texto_output_railfence.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_railfence.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_railfence)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_railfence)
        decifrar_btn.clicked.connect(self.on_decifrar_railfence)
        
        return widget_tab

    def on_cifrar_railfence(self):
        try:
            texto = self.texto_input_railfence.toPlainText()
            chave = self.chave_railfence_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_railfence(texto, chave)
            self.texto_output_railfence.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_railfence(self):
        try:
            texto = self.texto_input_railfence.toPlainText()
            chave = self.chave_railfence_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_railfence(texto, chave)
            self.texto_output_railfence.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_colunar(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_colunar_input = QLineEdit()
        self.chave_colunar_input.setPlaceholderText("Palavra-chave (letras únicas)")
        layout_chave.addRow(QLabel("Chave:"), self.chave_colunar_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_colunar = QTextEdit()
        self.texto_input_colunar.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_colunar)

        self.texto_output_colunar = QTextEdit()
        self.texto_output_colunar.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_colunar.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_colunar)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_colunar)
        decifrar_btn.clicked.connect(self.on_decifrar_colunar)
        
        return widget_tab

    def on_cifrar_colunar(self):
        try:
            texto = self.texto_input_colunar.toPlainText()
            chave = self.chave_colunar_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_colunar(texto, chave)
            self.texto_output_colunar.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_colunar(self):
        try:
            texto = self.texto_input_colunar.toPlainText()
            chave = self.chave_colunar_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_colunar(texto, chave)
            self.texto_output_colunar.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro na chave: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_doubletrans(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_doubletrans_1_input = QLineEdit()
        self.chave_doubletrans_1_input.setPlaceholderText("Chave 1 (letras únicas)")
        layout_chave.addRow(QLabel("Chave 1:"), self.chave_doubletrans_1_input)
        
        self.chave_doubletrans_2_input = QLineEdit()
        self.chave_doubletrans_2_input.setPlaceholderText("Chave 2 (letras únicas)")
        layout_chave.addRow(QLabel("Chave 2:"), self.chave_doubletrans_2_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_doubletrans = QTextEdit()
        self.texto_input_doubletrans.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_doubletrans)

        self.texto_output_doubletrans = QTextEdit()
        self.texto_output_doubletrans.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_doubletrans.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_doubletrans)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_doubletrans)
        decifrar_btn.clicked.connect(self.on_decifrar_doubletrans)
        
        return widget_tab

    def on_cifrar_doubletrans(self):
        try:
            texto = self.texto_input_doubletrans.toPlainText()
            chave1 = self.chave_doubletrans_1_input.text()
            chave2 = self.chave_doubletrans_2_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_doubletrans(texto, chave1, chave2)
            self.texto_output_doubletrans.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro nas chaves: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_doubletrans(self):
        try:
            texto = self.texto_input_doubletrans.toPlainText()
            chave1 = self.chave_doubletrans_1_input.text()
            chave2 = self.chave_doubletrans_2_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_doubletrans(texto, chave1, chave2)
            self.texto_output_doubletrans.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro nas chaves: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def criar_tab_keycipher(self):
        widget_tab = QWidget()
        layout_tab = QVBoxLayout(widget_tab)
        
        layout_chave = QFormLayout()
        self.chave_keycipher_1_input = QLineEdit()
        self.chave_keycipher_1_input.setPlaceholderText("Chave de Vigenère")
        layout_chave.addRow(QLabel("Chave 1 (Vigenère):"), self.chave_keycipher_1_input)
        
        self.chave_keycipher_2_input = QLineEdit()
        self.chave_keycipher_2_input.setPlaceholderText("Chave Colunar (letras únicas)")
        layout_chave.addRow(QLabel("Chave 2 (Colunar):"), self.chave_keycipher_2_input)
        
        layout_tab.addLayout(layout_chave)

        self.texto_input_keycipher = QTextEdit()
        self.texto_input_keycipher.setPlaceholderText("Digite o texto aqui...")
        layout_tab.addWidget(QLabel("Texto:"))
        layout_tab.addWidget(self.texto_input_keycipher)

        self.texto_output_keycipher = QTextEdit()
        self.texto_output_keycipher.setPlaceholderText("O resultado aparecerá aqui...")
        self.texto_output_keycipher.setReadOnly(True)
        layout_tab.addWidget(QLabel("Texto Cifrado / Decifrado:"))
        layout_tab.addWidget(self.texto_output_keycipher)

        botoes_layout = QHBoxLayout()
        cifrar_btn = QPushButton("Cifrar")
        decifrar_btn = QPushButton("Decifrar")
        
        botoes_layout.addWidget(cifrar_btn)
        botoes_layout.addWidget(decifrar_btn)
        layout_tab.addLayout(botoes_layout)

        cifrar_btn.clicked.connect(self.on_cifrar_keycipher)
        decifrar_btn.clicked.connect(self.on_decifrar_keycipher)
        
        return widget_tab

    def on_cifrar_keycipher(self):
        try:
            texto = self.texto_input_keycipher.toPlainText()
            chave1 = self.chave_keycipher_1_input.text()
            chave2 = self.chave_keycipher_2_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio.")
                return
                
            texto_cifrado = cifrar_keycipher(texto, chave1, chave2)
            self.texto_output_keycipher.setText(texto_cifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro nas chaves: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def on_decifrar_keycipher(self):
        try:
            texto = self.texto_input_keycipher.toPlainText()
            chave1 = self.chave_keycipher_1_input.text()
            chave2 = self.chave_keycipher_2_input.text()
            
            if not texto:
                self.mostrar_erro("O campo 'Texto' não pode estar vazio para decifrar.")
                return

            texto_decifrado = decifrar_keycipher(texto, chave1, chave2)
            self.texto_output_keycipher.setText(texto_decifrado)
        except ValueError as ve:
            self.mostrar_erro(f"Erro nas chaves: {ve}")
        except Exception as e:
            self.mostrar_erro(f"Erro inesperado: {e}")

    def mostrar_erro(self, mensagem):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setText(mensagem)
        msg_box.setWindowTitle("Erro de Validação")
        msg_box.exec()