import numpy as np
from math import exp, fabs
from data import can_harvest, get_tile
class AttMatrix:
    """
    Classe responsável por manter e calcular a matriz de atratividade (ou influência)
    do mapa do jogo, ajudando o agente na tomada de decisão sobre para onde se mover.
    """
    def __init__(self,**kwargs):
        # Matriz base que armazena o nível de atratividade inicial de cada tile no mapa (10x10)
        self.matrix = np.zeros((10,10))
        # Cria matrizes de coordenadas X e Y usando broadcasting do NumPy para evitar laços lentos (for loops)
        self.grid_y, self.grid_x = np.ogrid[:10, :10]
        # Temperatura: controla a intensidade do decaimento da atratividade pela distância
        self.T = kwargs.get('T',1)
        self.score_empty = kwargs.get('score_empty',2)
        self.score_weeds = kwargs.get('score_weeds',1)
        self.score_unwatered = kwargs.get('score_unwatered',10)
        self.score_harvest = kwargs.get('score_harvest',100)
   
    def get_score(self,i,j):
        """
        Calcula a atratividade agregada para a posição (i, j).
        A atratividade final em um ponto é a soma da influência de todos os tiles do mapa, 
        que decai exponencialmente conforme a distância.
        """
        # Se a posição estiver fora dos limites do mapa (10x10), retorna atratividade negativa infinita (inválida)
        if i<0 or j<0 or i>9 or j>9:
            return -np.inf        
        
        # Calcula a matriz com as distâncias Manhattan de (i, j) até todos os pontos (x, y) do mapa
        dist_mat = np.abs(self.grid_y - i) + np.abs(self.grid_x - j)
        
        # Calcula a soma das influências dividindo a atratividade base pelo exponencial da distância penalizada pela Temperatura
        return np.sum(self.matrix/np.exp(dist_mat/self.T))
   
    def update(self, obs):
        """
        Atualiza a matriz base de atratividade analisando a observação (obs) atual do ambiente.
        O valor de atratividade de cada tile varia dependendo do que tem nele (ex: planta seca atrai mais).
        """
        # Zera todos os valores da matriz de atratividade para recalculá-la
        self.matrix.fill(0)
        
        # Itera sobre cada tile do grid 10x10 para definir seu grau de atração ou repulsão
        for i,j in np.ndindex(self.matrix.shape):
            tile = get_tile(obs,i,j)
            if tile == 'LOCKED':
                self.matrix[i][j] = 0
            elif tile is None:
                self.matrix[i][j] = self.score_empty
            elif tile.get('kind','') == 'PLANT':
                if can_harvest(obs, tile):
                    self.matrix[i][j] = self.score_harvest
                elif tile['watered_today'] == False:
                    self.matrix[i][j] = self.score_unwatered * (tile.get('consecutive_unwatered', 0) + 1)
                else:
                    self.matrix[i][j] = 0
            elif tile.get('kind','') == 'WEED':
                self.matrix[i][j] = self.score_weeds
                
        
                        
        