from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import random
import time
import os

app = QtWidgets.QApplication([])

tela_home = uic.loadUi('janelas/tela_home.ui')
tela_forca = uic.loadUi('janelas/tela_forca.ui')
tela_velha = uic.loadUi('janelas/tela_velha.ui')
tela_jokenpo = uic.loadUi('janelas/tela_jokenpo.ui')
tela_dificuldade = uic.loadUi('janelas/tela_dificuldade.ui')
tela_perdeu_forca = uic.loadUi('janelas/tela_perdeu_forca.ui')
tela_ganhou_forca = uic.loadUi('janelas/tela_ganhou_forca.ui')
tela_memoria = uic.loadUi('janelas/tela_memoria.ui')
tela_click_jog = uic.loadUi('janelas/tela_click_jog.ui')

class Main:
    def exibicao_home():
        tela_click_jog.close()
        tela_home.show()

    def exibicao_velha():
        tela_velha.show()
    
    def exibicao_dificuldade():
        tela_dificuldade.show()

    def exibicao_jokenpo():
        tela_jokenpo.show()

    def chamada_memoria():
        jogo_memoria.reset()
        tela_memoria.show()
        jogo_memoria.sorteio_posicoes()

    def chamada_velha(btn):
        jogo_velha.jogada(btn)
        if jogo_velha.possib_vitoria() == True:
            jogo_velha.limpar()
            jogo_velha.pontos()
        else:
            jogo_velha.deu_velha()
    
    def resetar_velha():
        jogo_velha.resetar()

    def chamada_forca(dific):
        sorteio = random.randint(0, 9)
        tela_dificuldade.close()
        tela_forca.show()
        jogo_forca.definicao_dificuldade(dific)
        jogo_forca.import_palav()
        jogo_forca.dica_palavra(sorteio)
        jogo_forca.oculto()

    def enviar_forca():
        palpite = tela_forca.lineEdit_palpite.text()
        vr = jogo_forca.logica(palpite)

        if vr == True:
            tela_forca.close()
            tela_ganhou_forca.show()
        elif vr == False:
            tela_forca.close()
            tela_perdeu_forca.show()

        jogo_forca.chutes()
        jogo_forca.oculto()
        tela_forca.lineEdit_palpite.clear()

    def chamada_jokenpo(escolha):
        pc_sort = random.randint(0, 2)
        jogo_jokenpo.escolha_pc(pc_sort)
        jogo_jokenpo.disputa(escolha)

    def resetar_jokenpo():
        jogo_jokenpo.resetar()

    def memoria_btn_img(num, btn):
        jogo_memoria.mostrar_img(num, btn)
        jogo_memoria.verif_igualdade()
        jogo_memoria.tempo()

#//////////////////////////////////////////////////////////////////////

class Velha:
    def __init__(self):
        self.vez = 0
        self.pont_o = 0
        self.pont_x = 0
        self.vit_x = False
        self.vit_o = False

    def possib_vitoria(self):
        if tela_velha.cse.text() == 'X' and tela_velha.ms.text() == 'X' and tela_velha.csd.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.me.text() == 'X' and tela_velha.meio.text() == 'X' and tela_velha.md.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.cie.text() == 'X' and tela_velha.mi.text() == 'X' and tela_velha.cid.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.cse.text() == 'X' and tela_velha.me.text() == 'X' and tela_velha.cie.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.ms.text() == 'X' and tela_velha.meio.text() == 'X' and tela_velha.mi.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.csd.text() == 'X' and tela_velha.md.text() == 'X' and tela_velha.cid.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.cse.text() == 'X' and tela_velha.meio.text() == 'X' and tela_velha.cid.text() == 'X':
            self.vit_x = True
            return True
        elif tela_velha.csd.text() == 'X' and tela_velha.meio.text() == 'X' and tela_velha.cie.text() == 'X':
            self.vit_x = True
            return True

        if tela_velha.cse.text() == 'O' and tela_velha.ms.text() == 'O' and tela_velha.csd.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.me.text() == 'O' and tela_velha.meio.text() == 'O' and tela_velha.md.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.cie.text() == 'O' and tela_velha.mi.text() == 'O' and tela_velha.cid.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.cse.text() == 'O' and tela_velha.me.text() == 'O' and tela_velha.cie.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.ms.text() == 'O' and tela_velha.meio.text() == 'O' and tela_velha.mi.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.csd.text() == 'O' and tela_velha.md.text() == 'O' and tela_velha.cid.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.cse.text() == 'O' and tela_velha.meio.text() == 'O' and tela_velha.cid.text() == 'O':
            self.vit_o = True
            return True
        elif tela_velha.csd.text() == 'O' and tela_velha.meio.text() == 'O' and tela_velha.cie.text() == 'O':
            self.vit_o = True
            return True
    
    def jogada(self, btn):
        btn.setEnabled(False)
        self.vez = self.vez + 1
        if self.vez % 2 == 0:
            btn.setText('O')
        else:
            btn.setText('X')

    def limpar(self):
        tela_velha.cse.setEnabled(True)
        tela_velha.ms.setEnabled(True)
        tela_velha.csd.setEnabled(True)
        tela_velha.me.setEnabled(True)
        tela_velha.meio.setEnabled(True)
        tela_velha.md.setEnabled(True)
        tela_velha.cie.setEnabled(True)
        tela_velha.mi.setEnabled(True)
        tela_velha.cid.setEnabled(True)
        
        tela_velha.cse.setText('')
        tela_velha.ms.setText('')
        tela_velha.csd.setText('')
        tela_velha.me.setText('')
        tela_velha.meio.setText('')
        tela_velha.md.setText('')
        tela_velha.cie.setText('')
        tela_velha.mi.setText('')
        tela_velha.cid.setText('')
    
    def deu_velha(self):
        if tela_velha.cse.text() != '' and tela_velha.ms.text() != '' and tela_velha.csd.text() != '' and tela_velha.me.text() != '' and tela_velha.meio.text() != '' and tela_velha.md.text() != '' and tela_velha.cie.text() != '' and tela_velha.mi.text() != '' and tela_velha.cid.text() != '':
            tela_velha.cse.setEnabled(True)
            tela_velha.ms.setEnabled(True)
            tela_velha.csd.setEnabled(True)
            tela_velha.me.setEnabled(True)
            tela_velha.meio.setEnabled(True)
            tela_velha.md.setEnabled(True)
            tela_velha.cie.setEnabled(True)
            tela_velha.mi.setEnabled(True)
            tela_velha.cid.setEnabled(True)
            
            tela_velha.cse.setText('')
            tela_velha.ms.setText('')
            tela_velha.csd.setText('')
            tela_velha.me.setText('')
            tela_velha.meio.setText('')
            tela_velha.md.setText('')
            tela_velha.cie.setText('')
            tela_velha.mi.setText('')
            tela_velha.cid.setText('')
    
    def resetar(self):
        tela_velha.cse.setEnabled(True)
        tela_velha.ms.setEnabled(True)
        tela_velha.csd.setEnabled(True)
        tela_velha.me.setEnabled(True)
        tela_velha.meio.setEnabled(True)
        tela_velha.md.setEnabled(True)
        tela_velha.cie.setEnabled(True)
        tela_velha.mi.setEnabled(True)
        tela_velha.cid.setEnabled(True)
        
        tela_velha.cse.setText('')
        tela_velha.ms.setText('')
        tela_velha.csd.setText('')
        tela_velha.me.setText('')
        tela_velha.meio.setText('')
        tela_velha.md.setText('')
        tela_velha.cie.setText('')
        tela_velha.mi.setText('')
        tela_velha.cid.setText('')

        self.pont_x = 0
        tela_velha.Browser_X.setText(str(self.pont_x))

        self.pont_o = 0
        tela_velha.Browser_O.setText(str(self.pont_o))

    def pontos(self):
        if self.vit_x == True:
            self.pont_x = self.pont_x + 1
            tela_velha.Browser_X.setText(str(self.pont_x))
            self.vit_x = False
            print('X')

        if self.vit_o == True:
            self.pont_o = self.pont_o + 1
            tela_velha.Browser_O.setText(str(self.pont_o))
            self.vit_o = False
            print('O')

#//////////////////////////////////////////////////////////////////////

class Forca:
    def __init__(self):
        '''self.dif = str()'''
        self.dic_fac = dict()
        self.dic_med = dict()
        self.dic_dif = dict()
        self.erros = list()
        '''self.palavra = str()
        self.pal_escolhido = str()
        self.dic_escolhida = str()'''
        self.life = 5

    def definicao_dificuldade(self, dificul):
        self.dif = dificul
    
    def import_palav(self):
        cont = 0
        c = 1
        with open('palavras.txt', 'r', encoding='utf-8') as arq:
            for i in arq.readlines():
                i = i.split(';')
                cont = cont + 1
                if cont == 1:
                    for z in i:
                        if c % 2 == 0:
                            self.dic_fac.update({aux : z})
                        aux = z
                        c = c + 1
                c = 1
                if cont == 2:
                    for k in i:
                        if c % 2 == 0:
                            self.dic_med.update({auxi : k})
                        auxi = k
                        c = c + 1
                c = 1
                if cont == 3:
                    for w in i:
                        if c % 2 == 0:
                            self.dic_dif.update({auxil : w})
                        auxil = w
                        c = c + 1
    def dica_palavra(self, sorteio):
        if (self.dif == 'facil'):
            cont = 0
            for i in self.dic_fac:
                if cont == sorteio:
                    self.pal_escolhido = i
                cont = cont + 1
            self.dic_escolhida = self.dic_fac[self.pal_escolhido]

        elif(self.dif == 'medio'):
            cont = 0
            for i in self.dic_med:
                if cont == sorteio:
                    self.pal_escolhido = i
                cont = cont + 1
            self.dic_escolhida = self.dic_med[self.pal_escolhido]

        elif(self.dif == 'dificil'):
            cont = 0
            for i in self.dic_dif:
                if cont == sorteio:
                    self.pal_escolhido = i
                cont = cont + 1
            self.dic_escolhida = self.dic_dif[self.pal_escolhido]
        
        tela_forca.Browser_dica.setText(self.dic_escolhida)

        self.tamanho = len(self.pal_escolhido)
        self.listagem = list(self.pal_escolhido)
        self.list_ocul = list('_' * self.tamanho)

    def oculto(self):
        palavra_oculta = ''
        for i in self.list_ocul:
            palavra_oculta = palavra_oculta + ' ' + i
        tela_forca.Browser_oculto.setText(palavra_oculta)

    def chutes(self):
        erros = ''
        for i in self.erros:
            erros = erros + '   ' + i
        tela_forca.Browser_chutes.setText(erros)
    
    def logica(self, palpite):
        palpite = palpite.lower()
        vr = bool(False)

        for i in range(self.tamanho):
            if self.listagem[i] == palpite:
                self.list_ocul[i] = palpite
                vr = True
        
        if palpite == self.pal_escolhido:
            vr = True
            self.life = 5
            self.erros.clear()
            tela_forca.Browser_chutes.clear()
            tela_forca.Browser_vida.setText(str(self.life))
            return True

        if vr == False:
            self.life = self.life - 1
            self.erros.append(palpite)
            if self.life == 0:
                self.life = 5
                self.erros.clear()
                tela_forca.Browser_chutes.clear()
                tela_forca.Browser_vida.setText(str(self.life))
                return False
            tela_forca.Browser_vida.setText(str(self.life))
        
        if self.list_ocul == self.listagem:
            self.life = 5
            self.erros.clear()
            tela_forca.Browser_chutes.clear()
            tela_forca.Browser_vida.setText(str(self.life))
            return True

#//////////////////////////////////////////////////////////////////////

class Jokenpo:
    def __init__(self):
        self.pc_jogada = str()
        self.resultado = str()
        self.pont_user = 0
        self.pont_pc = 0

    def escolha_pc(self, pc_sorte):
        if pc_sorte == 0:
            self.pc_jogada = 'pedra'
        elif pc_sorte == 1:
            self.pc_jogada = 'papel'
        elif pc_sorte == 2:
            self.pc_jogada = 'tesoura'
        
        print(self.pc_jogada)
    
    def disputa(self, escolha):
        if escolha == 'pedra' and self.pc_jogada == 'pedra':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/pedra_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/pedra_pixel.png'))
            
            self.resultado = 'EMPATE!'
            tela_jokenpo.resultado.setText('EMPATE!')
        elif escolha == 'pedra' and self.pc_jogada == 'papel':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/pedra_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/papel_pixel.png'))

            self.resultado = 'VOCÊ PERDEU!'
            self.pont_pc = self.pont_pc + 1
            tela_jokenpo.pontos_pc.setText(str(self.pont_pc))
            tela_jokenpo.resultado.setText('VOCÊ PERDEU!')
        elif escolha == 'pedra' and self.pc_jogada == 'tesoura':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/pedra_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/tesoura_pixel.png'))

            self.resultado = 'VOCÊ GANHOU!'
            self.pont_user = self.pont_user + 1
            tela_jokenpo.pontos_user.setText(str(self.pont_user))
            tela_jokenpo.resultado.setText('VOCÊ GANHOU!')

        elif escolha == 'papel' and self.pc_jogada == 'papel':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/papel_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/papel_pixel.png'))

            self.resultado = 'EMPATOU!'
            tela_jokenpo.resultado.setText('EMPATE!')
        elif escolha == 'papel' and self.pc_jogada == 'tesoura':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/papel_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/tesoura_pixel.png'))

            self.resultado = 'VOCÊ PERDEU!'
            self.pont_pc = self.pont_pc + 1
            tela_jokenpo.pontos_pc.setText(str(self.pont_pc))
            tela_jokenpo.resultado.setText('VOCÊ PERDEU!')
        elif escolha == 'papel' and self.pc_jogada == 'pedra':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/papel_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/pedra_pixel.png'))

            self.resultado = 'VOCÊ GANHOU!'
            self.pont_user = self.pont_user + 1
            tela_jokenpo.pontos_user.setText(str(self.pont_user))
            tela_jokenpo.resultado.setText('VOCÊ GANHOU!')
        
        elif escolha == 'tesoura' and self.pc_jogada == 'tesoura':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/tesoura_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/tesoura_pixel.png'))

            self.resultado = 'EMPATOU!'
            tela_jokenpo.resultado.setText('EMPATE!')
        elif escolha == 'tesoura' and self.pc_jogada == 'pedra':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/tesoura_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/pedra_pixel.png'))

            self.resultado = 'VOCÊ PERDEU!'
            self.pont_pc = self.pont_pc + 1
            tela_jokenpo.pontos_pc.setText(str(self.pont_pc))
            tela_jokenpo.resultado.setText('VOCÊ PERDEU!')
        elif escolha == 'tesoura' and self.pc_jogada == 'papel':
            tela_jokenpo.user_escolha.setPixmap(QtGui.QPixmap('imagens/tesoura_pixel.png'))
            tela_jokenpo.pc_escolha.setPixmap(QtGui.QPixmap('imagens/papel_pixel.png'))

            self.resultado = 'VOCÊ GANHOU!'
            self.pont_user = self.pont_user + 1
            tela_jokenpo.pontos_user.setText(str(self.pont_user))
            tela_jokenpo.resultado.setText('VOCÊ GANHOU!')

    def resetar(self):
        self.pont_pc = 0
        self.pont_user = 0
        tela_jokenpo.pontos_user.setText('0')
        tela_jokenpo.pontos_pc.setText('0')
        tela_jokenpo.resultado.setText('Jogue novamente')
        tela_jokenpo.user_escolha.clear()
        tela_jokenpo.pc_escolha.clear()

#//////////////////////////////////////////////////////////////////////

class Memoria:
    def __init__(self):
        self.list_pura = ['imagens/barriu_pixel_art','imagens/diamente_pixel_art','imagens/moeda_pixel_art','imagens/sino_pixel_art','imagens/dinheiro_pixel_art','imagens/pedra_pixel_art','imagens/lanche_pixel_art','imagens/tijolo_pixel_art','imagens/barriu_pixel_art','imagens/diamente_pixel_art','imagens/moeda_pixel_art','imagens/sino_pixel_art','imagens/dinheiro_pixel_art','imagens/pedra_pixel_art','imagens/lanche_pixel_art','imagens/tijolo_pixel_art']
        self.list_mist = list()
        self.contador = 1
        self.cont = 3
        self.vr = False
        self.timer = QTimer()

    def sorteio_posicoes(self):
        self.list_mist.clear()
        self.pos_sorteadas = random.sample(range(0, 16), 16)
        for i in self.pos_sorteadas:
            self.list_mist.append(self.list_pura[i])

    def mostrar_img(self, num, btn):
        icon = QtGui.QIcon(str(self.list_mist[num]))
        btn.setIcon(icon)
        btn.setEnabled(False)
        self.icone_btn = self.list_mist[num]
        self.btn = btn

    def tempo(self):
        self.timer.timeout.connect(self.verif_igualdade_2)
        self.timer.start(1000)

        #self.timer.setInterval(1000)

    def verif_igualdade(self):
        if self.contador % 2 != 0:
            self.pri_icone = self.icone_btn
            self.pri_btn = self.btn
            self.vr = False
        else:
            self.vr = True
        
        self.contador = self.contador + 1
    
    def verif_igualdade_2(self):
        if self.vr == True:
            if self.pri_icone == self.icone_btn:
                print('as imagens são iguais')
                self.pri_btn.setEnabled(True)
                self.btn.setEnabled(True)
            else:
                print('as imagens não são iguais')
                icone = QtGui.QIcon('')
                self.pri_btn.setIcon(icone)
                self.pri_btn.setEnabled(True)
                self.btn.setIcon(icone)
                self.btn.setEnabled(True)

    def reset(self):
        self.contador = 1
        icon = QtGui.QIcon('')
        tela_memoria.btn_1.setIcon(icon)
        tela_memoria.btn_1.setEnabled(True)
        tela_memoria.btn_2.setIcon(icon)
        tela_memoria.btn_2.setEnabled(True)
        tela_memoria.btn_3.setIcon(icon)
        tela_memoria.btn_3.setEnabled(True)
        tela_memoria.btn_4.setIcon(icon)
        tela_memoria.btn_4.setEnabled(True)
        tela_memoria.btn_5.setIcon(icon)
        tela_memoria.btn_5.setEnabled(True)
        tela_memoria.btn_6.setIcon(icon)
        tela_memoria.btn_6.setEnabled(True)
        tela_memoria.btn_7.setIcon(icon)
        tela_memoria.btn_7.setEnabled(True)
        tela_memoria.btn_8.setIcon(icon)
        tela_memoria.btn_8.setEnabled(True)
        tela_memoria.btn_9.setIcon(icon)
        tela_memoria.btn_9.setEnabled(True)
        tela_memoria.btn_10.setIcon(icon)
        tela_memoria.btn_10.setEnabled(True)
        tela_memoria.btn_11.setIcon(icon)
        tela_memoria.btn_11.setEnabled(True)
        tela_memoria.btn_12.setIcon(icon)
        tela_memoria.btn_12.setEnabled(True)
        tela_memoria.btn_13.setIcon(icon)
        tela_memoria.btn_13.setEnabled(True)
        tela_memoria.btn_14.setIcon(icon)
        tela_memoria.btn_14.setEnabled(True)
        tela_memoria.btn_15.setIcon(icon)
        tela_memoria.btn_15.setEnabled(True)
        tela_memoria.btn_16.setIcon(icon)
        tela_memoria.btn_16.setEnabled(True)

#//////////////////////////////////////////////////////////////////////

jogo_memoria = Memoria()
jogo_forca = Forca()
jogo_velha = Velha()
jogo_jokenpo = Jokenpo()
jogo_memoria = Memoria()

#TELA CLICK
tela_click_jog.Button.clicked.connect(Main.exibicao_home)

#BTN TELA HOME
tela_home.Button_velha.clicked.connect(Main.exibicao_velha)
tela_home.Button_forca.clicked.connect(Main.exibicao_dificuldade)
tela_home.Button_jokenpo.clicked.connect(Main.exibicao_jokenpo)
tela_home.Button_memoria.clicked.connect(Main.chamada_memoria)

#BTN TELA FORCA
tela_forca.Button_enviar.clicked.connect(Main.enviar_forca)

#BTN TELA DIFICULDADE
tela_dificuldade.Button_dificil.clicked.connect(lambda: Main.chamada_forca('dificil'))
tela_dificuldade.Button_medio.clicked.connect(lambda: Main.chamada_forca('medio'))
tela_dificuldade.Button_facil.clicked.connect(lambda: Main.chamada_forca('facil'))

#BTN TELA VELHA
tela_velha.cse.clicked.connect(lambda: Main.chamada_velha(tela_velha.cse))
tela_velha.ms.clicked.connect(lambda: Main.chamada_velha(tela_velha.ms))
tela_velha.csd.clicked.connect(lambda: Main.chamada_velha(tela_velha.csd))
tela_velha.me.clicked.connect(lambda: Main.chamada_velha(tela_velha.me))
tela_velha.meio.clicked.connect(lambda: Main.chamada_velha(tela_velha.meio))
tela_velha.md.clicked.connect(lambda: Main.chamada_velha(tela_velha.md))
tela_velha.cie.clicked.connect(lambda: Main.chamada_velha(tela_velha.cie))
tela_velha.mi.clicked.connect(lambda: Main.chamada_velha(tela_velha.mi))
tela_velha.cid.clicked.connect(lambda: Main.chamada_velha(tela_velha.cid))
tela_velha.Button_reset.clicked.connect(Main.resetar_velha)

#BTN TELA JOKENPO
tela_jokenpo.Button_pedra.clicked.connect(lambda: Main.chamada_jokenpo('pedra'))
tela_jokenpo.Button_papel.clicked.connect(lambda: Main.chamada_jokenpo('papel'))
tela_jokenpo.Button_tesoura.clicked.connect(lambda: Main.chamada_jokenpo('tesoura'))
tela_jokenpo.Button_reset.clicked.connect(Main.resetar_jokenpo)

#BTN TELA MEMORIA
tela_memoria.Button_reset.clicked.connect(Main.chamada_memoria)
tela_memoria.btn_1.clicked.connect(lambda: Main.memoria_btn_img(0, tela_memoria.btn_1))
tela_memoria.btn_2.clicked.connect(lambda: Main.memoria_btn_img(1, tela_memoria.btn_2))
tela_memoria.btn_3.clicked.connect(lambda: Main.memoria_btn_img(2, tela_memoria.btn_3))
tela_memoria.btn_4.clicked.connect(lambda: Main.memoria_btn_img(3, tela_memoria.btn_4))
tela_memoria.btn_5.clicked.connect(lambda: Main.memoria_btn_img(4, tela_memoria.btn_5))
tela_memoria.btn_6.clicked.connect(lambda: Main.memoria_btn_img(5, tela_memoria.btn_6))
tela_memoria.btn_7.clicked.connect(lambda: Main.memoria_btn_img(6, tela_memoria.btn_7))
tela_memoria.btn_8.clicked.connect(lambda: Main.memoria_btn_img(7, tela_memoria.btn_8))
tela_memoria.btn_9.clicked.connect(lambda: Main.memoria_btn_img(8, tela_memoria.btn_9))
tela_memoria.btn_10.clicked.connect(lambda: Main.memoria_btn_img(9, tela_memoria.btn_10))
tela_memoria.btn_11.clicked.connect(lambda: Main.memoria_btn_img(10, tela_memoria.btn_11))
tela_memoria.btn_12.clicked.connect(lambda: Main.memoria_btn_img(11, tela_memoria.btn_12))
tela_memoria.btn_13.clicked.connect(lambda: Main.memoria_btn_img(12, tela_memoria.btn_13))
tela_memoria.btn_14.clicked.connect(lambda: Main.memoria_btn_img(13, tela_memoria.btn_14))
tela_memoria.btn_15.clicked.connect(lambda: Main.memoria_btn_img(14, tela_memoria.btn_15))
tela_memoria.btn_16.clicked.connect(lambda: Main.memoria_btn_img(15, tela_memoria.btn_16))


tela_click_jog.show()
app.exec()