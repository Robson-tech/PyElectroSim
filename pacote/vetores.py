from typing import Any
import math


class Vetor:
    """
    Classe que representa um vetor no plano cartesiano.

    ...

    Attributes
    ----------
    modulo : float
        módulo (intensidade) do vetor
    angulo : str
        direção do vetor, indicado em graus pelo ângulo formado com o eixo das abscissas
    sentido : str
        sentido do vetor, indicado por um número inteiro positivo ou negativo
    """
    def __init__(self, modulo: float, angulo: float, sentido: int):
        """
        Parameters
        ----------
        modulo : float
            módulo (intensidade) do vetor
        angulo : str
            direção do vetor, indicado em graus pelo ângulo formado com o eixo das abscissas
        sentido : str
            sentido do vetor, indicado por um número inteiro positivo ou negativo
        """
        self.modulo = modulo
        self.angulo = angulo
        self.sentido = sentido
        if self.modulo < 0:
            self.modulo *= -1
            self.sentido *= -1

    def __str__(self) -> str:
        return f'Vetor({self.modulo}, {self.angulo}, {self.sentido})'
    
    def __repr__(self) -> str:
        return self.modulo

    def __bool__(self) -> bool:
        return self.modulo != 0

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Vetor) and self and __value:
            # Para serem iguais, os vetores devem ter o mesmo módulo, direção e sentido
            return self.modulo == __value.modulo \
                and self.angulo == __value.angulo \
                and self.sentido == __value.sentido
        return False
    
    def __ne__(self, __value: object) -> bool:
        return not self == __value
    
    def __pos__(self) -> 'Vetor':
        return Vetor(self.modulo, self.angulo, self.sentido)
    
    def __neg__(self) -> 'Vetor':
        return Vetor(self.modulo, self.angulo, -self.sentido)
    
    def __add__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, Vetor) and self and __value:
            soma_x = self.modulo * math.cos(math.radians(self.angulo)) \
                + __value.modulo * math.cos(math.radians(__value.angulo))
            soma_y = self.modulo * math.sin(math.radians(self.angulo)) \
                + __value.modulo * math.sin(math.radians(__value.angulo))
            modulo = math.sqrt(soma_x ** 2 + soma_y ** 2)
            angulo = math.degrees(math.atan2(soma_y, soma_x))
            return Vetor(modulo, angulo, self.sentido)
        raise TypeError('Os valores devem ser do tipo Vetor.')
    
    def __sub__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, Vetor) and self and __value:
            if self.angulo == __value.angulo and self.sentido == __value.sentido:
                # Para subtrair dois vetores, eles devem ter a mesma direção e o mesmo sentido
                return Vetor(self.modulo - __value.modulo, self.angulo, self.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção e o mesmo sentido.')
        raise TypeError('Os valores devem ser do tipo Vetor.')
    
    def __mul__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, (int, float)):
            return Vetor(self.modulo * __value, self.angulo, self.sentido)
        elif isinstance(__value, Vetor) and self and __value:
            if self.angulo == __value.angulo:
                # Para multiplicar dois vetores, eles devem ter a mesma direção
                return Vetor(self.modulo * __value.modulo, self.angulo, self.sentido * __value.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção.')
        raise TypeError('O valor deve ser do tipo int, float ou Vetor.')
    
    def __truediv__(self, __value: Any) -> 'Vetor':
        if isinstance(__value, (int, float)):
            return Vetor(self.modulo / __value, self.angulo, self.sentido)
        elif isinstance(__value, Vetor) and self and __value:
            if self.angulo == __value.angulo:
                # Para dividir dois vetores, eles devem ter a mesma direção
                return Vetor(self.modulo / __value.modulo, self.angulo, self.sentido * __value.sentido)
            else:
                raise ValueError('Os vetores devem ter a mesma direção.')
        raise TypeError('O valor deve ser do tipo int ou float.')


if __name__ == '__main__':
    v1 = Vetor(30, 0, 1)
    v2 = Vetor(40, 90, 1)
    print(v1 + v2)