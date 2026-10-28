import numpy as np
from data import can_harvest, get_tile, get_farmer, get_tile_kind, crops, get_seeds_available

class FarmerAct:
    """
    Classe responsável pelas decisões de ação e movimento do fazendeiro, 
    utilizando a matriz de atratividade para escolher as melhores opções.
    """
    def __init__(self, **kwargs):
        # Tupla com as direções e seus deltas (ação, delta_linha, delta_coluna)
        self.moves = (
            ('NORTH', -1,  0),
            ('SOUTH',  1,  0),
            ('EAST',   0,  1),
            ('WEST',   0, -1),
        )
        # Carregar scores base de ações 
        self.score_dig = kwargs.get('score_weeds',1)*10
        self.score_water = kwargs.get('score_unwatered',10)*10
        self.score_harvest = kwargs.get('score_harvest',100)*10
        self.score_plant = kwargs.get('score_empty',2)*10
               
    def _moves(self, obs, att):
        """
        Determina a melhor direção para o fazendeiro se mover, 
        baseando-se na pontuação (atratividade) das células adjacentes.
        """        
        # Posição atual do fazendeiro (x=coluna, y=linha)
        # No jogo, as coordenadas vêm invertidas [x, y], então desempacotamos como j(coluna), i(linha)
        j, i = get_farmer(obs)
        
        # Opcional: print para debug da posição atual
        print(i, j)
        
        # Dicionário para armazenar a pontuação de cada movimento possível
        m = {}
        for move, di, dj in self.moves:
            ni, nj = i + di, j + dj
            
            # Verifica se o movimento tenta sair das bordas do mapa (10x10)
            if ni < 0 or ni > 9 or nj < 0 or nj > 9:
                continue
                
            # Verifica se o ladrilho está bloqueado (terreno não comprado)
            if get_tile(obs, ni, nj) == 'LOCKED':
                m[move] = -np.inf
            else:
                # Consulta a matriz de atratividade para obter a pontuação do tile destino
                m[move] = att.get_score(ni, nj)                        
        return m

    def _fill_plants(self, obs, m):
        """
        Atribui um score para cada cultura com semente disponível
        """
        for crop in crops:
            if get_seeds_available(obs, crop) > 0:
                m[('PLANT', crop)] =  self.score_plant

    def _plants(self, obs, att):
        """
        Determina a melhor ação relacionada a plantio/interação com o ladrilho atual.
        """
        # Pega a posição atual do fazendeiro e o conteúdo do ladrilho (tile)
        j, i = get_farmer(obs)
        tile = get_tile(obs, i, j)
        
        # Determina o tipo de conteúdo do tile padronizado como string ('EMPTY', 'PLANT', 'WEED', 'LOCKED')
        kind = get_tile_kind(tile)
        
        # Dicionário de pontuação para as ações no tile (PASS = não faz nada)
        m = {'PASS': 0}
        
        if kind == 'EMPTY':
            self._fill_plants(obs, m)
        elif kind == 'PLANT':
            if can_harvest(obs, tile):
                m['HARVEST'] =  self.score_harvest
            if tile['watered_today'] == False:
                m['WATER'] = self.score_water  
        elif kind == 'WEED':
            m['DIG'] = self.score_dig
        return m
        
    def next_action(self, obs, att):
        m = {}
        m.update(self._moves(obs, att))
        m.update(self._plants(obs, att))
        best = max(m, key=m.get)
        if isinstance(best, tuple):
            best = list(best)
        elif not isinstance(best, list):
            # action precisa ser uma lista
            best = [best]
        return best
            
        