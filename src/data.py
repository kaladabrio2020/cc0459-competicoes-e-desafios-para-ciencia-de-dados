
# Constantes e metadados do ambiente Kaggriculture (specs/README.md e specs/AGENTS.md)

# Lista com todos os objetos principais do jogo: culturas (crops), animais (livestock) e fertilizante.
objects = [
    'WHEAT',
    'CARROT',
    'TOMATO',
    'STRAWBERRY',
    'MELON',
    'GOOSE',
    'COW',
    'SHEEP',
    'FERTILIZER',
]

crops = objects[:-4]


# Tipo de produção / rendimento (Yield Type):
# - 'one-time': culturas de colheita única (Wheat, Carrot, Melon); ao colher, a planta é removida.
# - 'ongoing': culturas contínuas (Tomato, Strawberry - até 4 colheitas) e animais (Goose, Cow, Sheep - produção contínua).
# - 'none': itens de utilidade sem colheita direta (Fertilizer).
yield_type = dict(
    zip(
        objects,
        [
            'one-time',
            'one-time',
            'ongoing',
            'ongoing',
            'one-time',
            'ongoing',
            'ongoing',
            'ongoing',
            'none',
        ],
    )
)

# Custo de compra da semente ou animal no mercado (Seed Cost / Animal Cost em $).
# Nota: Fertilizante custa $100 via BUY_PRODUCT.
seed_cost = dict(zip(objects, [10, 20, 50, 100, 80, 300, 400, 500, 100]))

# Preço base de venda no mercado com estoque inicial I0 = 10.000 unidades (Base Market Price em $).
# O preço varia dinamicamente conforme escassez ou saturação (veja specs/README.md - The Price Function).
# Fertilizante coletado de animais pode ser vendido (preço base 100, no código 0/definido no mercado).
base_price = dict(zip(objects, [25, 35, 60, 120, 250, 50, 160, 200, 0]))

# Tempo até o primeiro rendimento (Time to First Yield em dias de jogo).
# Para culturas, indica quando atinge maturidade mínima para colheita.
# Para animais, dias após a alocação (PLACE) até a primeira produção.
first_yield = dict(zip(objects, [2, 2, 8, 10, 10, 4, 8, 6, 0]))

# Tempo até o rendimento máximo (Time to Max Yield em dias de jogo).
# Para culturas de colheita única, idade onde a rega atinge o teto de bônus.
# Culturas contínuas atingem a produção máxima programada aos 11 dias (Tomato) e 16 dias (Strawberry).
# Animais não possuem limite de tempo (NA / 0), pois produzem indefinidamente enquanto forem alimentados.
time_to_max_yield = dict(zip(objects, [4, 3, 11, 16, 10, 0, 0, 0, 0]))

# Frequência de produções subsequentes (Subsequent Yields).
# Culturas 'one-time' não possuem rendimentos extras ('none').
# Tomate: 4 colheitas consecutivas diárias (dias 8 a 11).
# Morango: 4 colheitas em dias alternados (dias 10, 12, 14 e 16).
# Animais: Goose produz todo dia; Cow a cada 2 dias; Sheep a cada 3 dias (desde que alimentados com trigo).
subsequent_yields = dict(
    zip(
        objects,
        [
            'none',
            'none',
            'every day x4',
            'every 2 days x4',
            'none',
            'every day',
            'every 2 days',
            'every 3 days',
            'none',
        ],
    )
)

# Rendimento máximo colhível sem adubação (Max Yield Unfertilized).
# Para animais representa o 'max_held', ou seja, o limite acumulável no tile sem colheita (4 para Goose, 6 para Cow/Sheep).
max_yield = dict(zip(objects, [4, 3, 4, 4, 6, 4, 6, 6, 0]))

# Rendimento máximo com adubação / fertilização (Max Yield Fertilized).
# Trigo sobe de 4 para 6 e Cenoura de 3 para 4 quando fertilizados durante o ciclo.
max_yield_fertilized = dict(zip(objects, [6, 4, 4, 4, 6, 4, 6, 6, 0]))

# Custo em ações (Action Cost):
# Culturas e fertilizante exigem 1 ação de interação direta no tile (PLANT/WATER/HARVEST).
# Animais exigem 2 ações (1 para construir a estrutura BUILD_COOP/BUILD_PASTURE + 1 para colocar o animal PLACE).
action_cost = dict(zip(objects, [1, 1, 1, 1, 1, 2, 2, 2, 1]))

# Rendimento médio de produto por ladrilho por dia (Yield / tile / day).
# Para culturas: total de unidades colhidas dividido pelo tempo de ocupação do solo (com rega diária ideal).
# Para animais: taxa estável de produção em regime permanente (1 / intervalo).
yield_per_day = dict(
    zip(objects, [0.80, 0.75, 0.33, 0.24, 0.55, 1.00, 0.50, 0.33, 0])
)

## AÇÕES DISPONÍVEIS PARA O FAZENDEIRO E AJUDANTES (Farmer & Farm Hand Actions)
# Cada unidade (fazendeiro principal e mãos contratadas) pode executar 1 ação por turno.
actions = {}

# Movimentação pelo grid (NORTH, SOUTH, EAST, WEST).
# Ladrilhos não desbloqueados (LOCKED) são transitáveis, mas não permitem ações de cultivo/construção.
actions['move'] = ['NORTH', 'SOUTH', 'EAST', 'WEST']

# Ações de inventário e celeiro (Shed):
# O celeiro fica no centro do tabuleiro: tiles (4,4), (5,4), (4,5), (5,5) no grid 10x10.
# - PICKUP <item> [n]: retira itens do celeiro para o inventário da unidade (sementes não ficam aqui).
# - DROP: descarrega todo o inventário da unidade no celeiro (excedentes além da capacidade 100 são perdidos).
# - PLACE <item> [n]: transfere itens do inventário para o celeiro quando adjacente a ele.
actions['shed'] = ['PICKUP <item> [n]', 'DROP', 'PLACE <item> [n]']

# Manejo de plantas no ladrilho atual:
# - PLANT <item>: planta semente (consumida diretamente da reserva compartilhada de sementes).
# - WATER: rega a planta (obrigatório pelo menos a cada 2 dias; 2 dias sem regar vira WEED).
# - HARVEST: colhe os produtos disponíveis e adiciona ao inventário da unidade.
# - FERTILIZE: aplica adubo, dobrando o bônus de rega nos próximos 3 dias (requer rega diária).
actions['plants'] = ['PLANT <item>', 'WATER', 'HARVEST', 'FERTILIZE']

# Manejo de animais e estruturas:
# - PLACE <item> [n]: posiciona o animal do inventário no cercado apropriado (Goose no COOP, Sheep/Cow no PASTURE).
# - FEED: alimenta o animal com trigo (1 trigo/dia; 2 dias seguidos sem alimento causam fuga).
# - HARVEST: coleta produtos acumulados (ovos, leite ou lã).
# - COLLECT_FERTILIZER: coleta 1 unidade de adubo diário produzido por animal vivo.
# - CARE: cuida do animal, acumulando bônus para a próxima rodada de produção agendada.
actions['animal'] = [
    'PLACE <item> [n]',
    'FEED',
    'HARVEST',
    'COLLECT_FERTILIZER',
    'CARE',
]

# Modificações de terreno:
# - BUILD_COOP: constrói um galinheiro em ladrilho vazio desbloqueado.
# - BUILD_PASTURE: constrói um pasto em ladrilho vazio desbloqueado.
# - DIG: remove plantas indesejadas, ervas daninhas (WEED) ou estruturas vazias (sem animais).
actions['terrain'] = ['BUILD_COOP', 'BUILD_PASTURE', 'DIG']

# Conjunto consolidado com todas as ações possíveis de unidades no campo.
actions['all'] = set(
    actions['move']
    + actions['shed']
    + actions['plants']
    + actions['animal']
    + actions['terrain']
)

## AÇÕES DE MERCADO (Market Actions)
# Cada jogador pode enviar até maxMarketOrdersPerTurn (padrão 10) ordens de mercado por turno.
# As ordens são processadas em fila simultânea entre os competidores, unidade por unidade.
market = [
    'BUY_SEED <item> <n>',  # Compra n sementes a preço fixo
    'BUY_ANIMAL <item> <n>',  # Compra n animais a preço fixo
    'BUY_PRODUCT <item> <n>',  # Compra n produtos (apenas WHEAT e FERTILIZER são permitidos)
    'SELL <item> <n>',  # Vende n produtos do celeiro ao preço dinâmico de mercado
    'HIRE',  # Contrata 1 ajudante para o dia atual (custo escala via Fibonacci: 1, 1, 2, 3, 5, 8...)
    'BUY_LAND',  # Desbloqueia um novo quadrante 5x5 do terreno
]

# Custos progressivos para desbloqueio dos 3 quadrantes restantes (NE, SW, SE) via BUY_LAND.
# O quadrante inicial NW já inicia desbloqueado.
land_cost = [1000, 2000, 4000]

## DEMANDAS DE COMÉRCIO LOCAL (Town Shops)
# Lojas desbloqueadas a cada town_shop_unlock_interval dias (sorteadas com reposição, máx 8 lojas).
# A cada town_shop_sell_interval turnos, cada loja consome 1 unidade de cada produto listado (2x se foco único),
# drenando a oferta do mercado e elevando os preços de venda.
shop_demands = {}
shop_demands['Bakery'] = ['Goose', 'Wheat']  # Padaria: ovos e trigo
shop_demands['Pizza Shop'] = ['Cow', 'Wheat', 'Tomato']  # Pizzaria: leite, trigo e tomate
shop_demands['Brunch Spot'] = ['Goose', 'Wheat', 'Strawberry']  # Brunch: ovos, trigo e morango
shop_demands['Yarn Store'] = ['Sheep'] * 2  # Loja de lã: 2x lã
shop_demands['Ice Cream Shop'] = ['Strawberry', 'Cow', 'Wheat']  # Sorveteria: morango, leite e trigo
shop_demands['Pet Cafe'] = ['Carrot'] * 2  # Pet café: 2x cenoura
shop_demands['Smoothie Shop'] = ['Strawberry', 'Cow']  # Casa de sucos: morango e leite
shop_demands['Farmers Market'] = [
    'Wheat',
    'Carrot',
    'Tomato',
    'Strawberry',
]  # Feira: trigo, cenoura, tomate e morango

## CONFIGURAÇÕES PADRÃO DO AMBIENTE (Environment Configuration Defaults)
# Parâmetros padrão de simulação definidos nas regras do Kaggriculture.
epsode_steps = 720  # Duração total da temporada em turnos (24 turnos/dia x 30 dias)
board_size = 10  # Dimensão do tabuleiro (10x10 ladrilhos, divididos em quatro quadrantes 5x5)
starting_money = 3000  # Saldo monetário inicial de cada jogador ($)
max_market_orders_per_turn = 10  # Limite máximo de ordens de mercado processadas por turno
turns_per_day = 24  # Quantidade de turnos (horas) em 1 dia de jogo
shed_capacity = 100  # Capacidade máxima de itens no celeiro (exclui sementes; excedentes descartados)
weed_spawn_chance = 0.005  # Probabilidade diária de surgir erva daninha em ladrilho vazio desbloqueado
town_shop_unlock_interval = 3  # Intervalo em dias para sorteio e abertura de uma nova loja na cidade
town_shop_sell_interval = 4  # Intervalo em turnos no qual lojas consom produtos do mercado
town_center_sell_interval = 24  # Intervalo em turnos no qual o centro da cidade consome 1 de cada produto
seed = 0  # Semente pseudoaleatória opcional para determinismo de episódios


## Helper functions

def get_farmer(obs, player=0):
    """
    Retorna a posição [coluna, linha] do fazendeiro do player 0
    """
    return obs['farms'][player]['farmer']

def get_tile(obs,i,j, player=0):
    """
    Retorna o tile da posição (i, j) do tabuleiro para o player 0
    """
    return obs['farms'][player]['tiles'][i][j]

def can_harvest(obs, tile):
    """
    Verifica se uma planta está pronta para a colheita, 
    avaliando os yield_units disponíveis e a idade mínima (first_yield_day).
    """
    if not isinstance(tile, dict) or tile.get('kind', '') != 'PLANT':
        return False
    
    crop_age = obs["day"] - tile.get("planted_day", obs["day"])
    return tile.get('yield_units', 0) > 0 and crop_age >= first_yield.get(tile.get('crop'), 999)

def get_tile_kind(tile):
    """
    Retorna o tipo (kind) do ladrilho sempre padronizado como string ('EMPTY', 'LOCKED', 'PLANT', 'WEED', etc.).
    - Se for None: 'EMPTY'
    - Se for dict: tile.get('kind', '')
    - Se for string (ex: 'LOCKED'): tile
    """
    if tile is None:
        return 'EMPTY'
    if isinstance(tile, dict):
        return str(tile.get('kind', 'EMPTY'))
    return str(tile)

def get_seeds_available(obs, crop=None):
    """
    Retorna a quantidade de sementes disponíveis no inventário privado.
    Se 'crop' for informado, retorna a quantidade dessa cultura; caso contrário, retorna o dicionário completo.
    """
    seeds = obs['private']['seeds']
    return seeds.get(crop, 0) if crop else seeds

def get_money(obs, player=0):
    """
    Retorna o saldo monetário ($) atual do jogador.
    """
    return obs['farms'][player]['money']

def get_day(obs):
    """
    Retorna o dia atual de jogo (0-indexed).
    """
    return obs.get('day', 0)

def get_days_left(obs):
    """
    Retorna a quantidade de dias restantes na temporada.
    """
    return (epsode_steps // turns_per_day) - get_day(obs)

