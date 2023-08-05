from typing import Any


class Vetor:
    """
    Classe que representa um vetor no plano cartesiano.

    ...

    Attributes
    ----------
    modulo : float
        módulo do vetor
    direcao : str
        direção do vetor
    sentido : str
        sentido do vetor
    """
    def __init__(self, modulo: float, direcao: str, sentido: int, angulo: float = 0):
        self.modulo = modulo
        self.direcao = direcao
        self.sentido = sentido
        self.angulo = angulo
        if self.modulo < 0:
            self.modulo *= -1
            self.sentido *= -1

    def __str__(self) -> str:
        return f'Vetor({self.modulo}, {self.direcao}, {self.sentido})'
    
    def __repr__(self) -> str:
        return self.modulo

    def __bool__(self) -> bool:
        return self.modulo != 0 and self.direcao != '' and self.sentido != 0

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vetor) and self and __value:
            # Para serem iguais, os vetores devem ter o mesmo módulo, direção e sentido
            return self.modulo == __value.modulo \
                and self.direcao == __value.direcao \
                and self.sentido == __value.sentido
        return False
    
    def __ne__(self, __value: object) -> bool:
        return not self == __value
    
    def __pos__(self) -> 'Vetor':
        return Vetor(self.modulo, self.direcao, self.sentido)
    
    def __neg__(self) -> 'Vetor':
        return Vetor(self.modulo, self.direcao, -self.sentido)
    
    def __add__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, Vetor) and self and __value:
            if self.direcao == __value.direcao and self.sentido == __value.sentido:
                # Para somar dois vetores, eles devem ter a mesma direção e o mesmo sentido
                return Vetor(self.modulo + __value.modulo, self.direcao, self.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção e o mesmo sentido.')
        raise TypeError('Os valores devem ser do tipo Vetor.')
    
    def __sub__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, Vetor) and self and __value:
            if self.direcao == __value.direcao and self.sentido == __value.sentido:
                # Para subtrair dois vetores, eles devem ter a mesma direção e o mesmo sentido
                return Vetor(self.modulo - __value.modulo, self.direcao, self.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção e o mesmo sentido.')
        raise TypeError('Os valores devem ser do tipo Vetor.')
    
    def __mul__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, (int, float)):
            return Vetor(self.modulo * __value, self.direcao, self.sentido)
        elif isinstance(__value, Vetor) and self and __value:
            if self.direcao == __value.direcao:
                # Para multiplicar dois vetores, eles devem ter a mesma direção
                return Vetor(self.modulo * __value.modulo, self.direcao, self.sentido * __value.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção.')
        raise TypeError('O valor deve ser do tipo int, float ou Vetor.')
    
    def __truediv__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, (int, float)):
            return Vetor(self.modulo / __value, self.direcao, self.sentido)
        elif isinstance(__value, Vetor) and self and __value:
            if self.direcao == __value.direcao:
                # Para dividir dois vetores, eles devem ter a mesma direção
                return Vetor(self.modulo / __value.modulo, self.direcao, self.sentido * __value.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção.')
        raise TypeError('O valor deve ser do tipo int ou float.')


if __name__ == '__main__':
    v1 = Vetor(10, 'N', 1)
    v2 = Vetor(20, 'N', 1)
    if v1 == -v2:
        print('iguais')
    else:
        print('diferentes')
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * (1/2))
    print(v1 * (-2))
    print(v1 * v2)
    print(v1 * v1)
    print(v1 / 2)
    print(v1 / (-2))
    print(v1 / v2)