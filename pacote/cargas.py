from conf import *
import math
import pygame as py


class Carga(py.sprite.Sprite):
    def __init__(self, x: int, y: int, raio: int, num_eletrons: int, identificador: str = None):
        super().__init__()
        self.x = x
        self.y = y
        self.raio = raio
        self.valor = num_eletrons * e
        self.identificador = identificador
        self.sinal, self.cor = self.get_sinal_cor()
        self.massa = MASSA
        self.velocidade_x = VELOCIDADE_INICIAL
        self.velocidade_y = VELOCIDADE_INICIAL

    def get_sinal_cor(self):
        sinal = 0
        cor = CINZA
        if self.valor < 0:
            sinal = -1
            cor = VERMELHO
        elif self.valor > 0:
            sinal = 1
            cor = AZUL
        return sinal, cor
    
    def desenhar(self, tela: py.Surface):
        py.draw.circle(tela, self.cor, (self.x, self.y), self.raio)
        if self.identificador:
            fonte = py.font.SysFont('Arial', 15)
            texto = fonte.render(self.identificador, True, TEXT_COLOR)
            tela.blit(texto, (self.x + self.raio, self.y + self.raio))

    def calcular_forca_eletrica(self, carga: 'Carga') -> tuple:
        forca_x = forca_y = 0
        dx = carga.x - self.x
        dy = carga.y - self.y
        quadrado_distancia = dx ** 2 + dy ** 2
        if quadrado_distancia >= (self.raio * carga.raio) ** 2:
            forca_eletrica = k * self.sinal * carga.sinal / quadrado_distancia
            angulo = math.atan2(dy, dx)
            forca_x += forca_eletrica * math.cos(angulo)
            forca_y += forca_eletrica * math.sin(angulo)
        return forca_x, forca_y

    def atualizar_posicao(self, cargas: list, largura: int, altura: int):
        forca_total_x = forca_total_y = 0
        for carga in cargas:
            if carga != self:
                forca_x, forca_y = self.calcular_forca_eletrica(carga)
                forca_total_x += forca_x
                forca_total_y += forca_y
        # self.velocidade_x += forca_total_x / self.massa * ESCALA
        # self.velocidade_y += forca_total_y / self.massa * ESCALA
        if (self.x + self.raio < largura and self.x + self.raio > 0) and (self.y + self.raio < altura and self.y + self.raio > 0):
            self.x += forca_total_x / self.massa * ESCALA
            self.y += forca_total_y / self.massa * ESCALA


if __name__ == '__main__':
    pass