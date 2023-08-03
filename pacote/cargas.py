from conf import *
import pygame as py


class Carga(py.sprite.Sprite):
    def __init__(self, x: int, y: int, raio: int, num_eletrons: int, identificador: str):
        super().__init__()
        self.x = x
        self.y = y
        self.posicao = (x, y)
        self.carga = num_eletrons * e
        self.identificador = identificador
        self.raio = raio
        self.image = py.Surface((self.raio * 2, self.raio * 2))
        self.rect = self.image.get_rect()
        self.rect.center = self.posicao
    
    def desenhar(self, tela: py.Surface):
        py.draw.circle(tela, (255, 255, 255), self.posicao, self.raio)
        # nome identificador
        fonte = py.font.SysFont('Arial', 15)
        texto = fonte.render(self.identificador, True, (255, 255, 255))
        tela.blit(texto, (self.x + self.raio, self.y + self.raio))


if __name__ == '__main__':
    q1 = Carga(100, 100, 1, 'q1')
    print(q1.carga)