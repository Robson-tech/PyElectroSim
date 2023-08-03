from conf import *
import pygame as py
from cargas import Carga


class Simulador:
    def __init__(self):
        self.largura = LARGURA
        self.altura = ALTURA
        self.resolucao = (self.largura, self.altura)
        self.tela = py.display.set_mode(self.resolucao)
        py.display.set_caption('Simulador de Campo Elétrico')
        self.relogio = py.time.Clock()
        self.executando = True
        self.carga1 = Carga(100, 100, RAIO, 1, 'q1')
        self.carga2 = Carga(200, 200, RAIO, -1, 'q2')

    def iniciar(self):
        py.init()
        while self.executando:
            self.relogio.tick(FPS)
            self.eventos()
            self.desenhar()
            self.atualizar()
        py.quit()
    
    def eventos(self):
        for evento in py.event.get():
            if evento.type == py.QUIT:
                self.executando = False

    def desenhar(self):
        self.tela.fill((100, 100, 100))
        self.carga1.desenhar(self.tela)
        self.carga2.desenhar(self.tela)
    
    def atualizar(self):
        py.display.update()


if __name__ == '__main__':
    simulador = Simulador()
    simulador.iniciar()