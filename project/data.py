

# ==========================================
# OBJETOS (Culturas, Animais e Itens)
# ==========================================
# Combina as tabelas "Object Types" e "Market Mechanics" para facilitar o acesso.

OBJECTS = {
    "WHEAT": {
        "type": "CROP",
        "yield_type": "One-time",
        "seed_cost": 10,
        "base_market_price": 25,
        "time_to_first_yield_days": 2,
        "time_to_max_yield_days": 4,
        "subsequent_yields": None,
        "max_yield": 6,
        "max_yield_unfertilized": 4,
        "action_cost": 1,
        "yield_per_tile_per_day": 0.80,
        "market": {
            "I0": 10000, "T": 400,
            "below_func": "sqrt", "below_target": 0.80,
            "above_func": "log", "above_target": 0.20
        }
    },
    "CARROT": {
        "type": "CROP",
        "yield_type": "One-time",
        "seed_cost": 20,
        "base_market_price": 35,
        "time_to_first_yield_days": 2,
        "time_to_max_yield_days": 3,
        "subsequent_yields": None,
        "max_yield": 4,
        "max_yield_unfertilized": 3,
        "action_cost": 1,
        "yield_per_tile_per_day": 0.75,
        "market": {
            "I0": 10000, "T": 450,
            "below_func": "log", "below_target": 0.20,
            "above_func": "sqrt", "above_target": 0.70
        }
    },
    "TOMATO": {
        "type": "CROP",
        "yield_type": "Ongoing",
        "seed_cost": 50,
        "base_market_price": 60,
        "time_to_first_yield_days": 8,
        "time_to_max_yield_days": 11,
        "subsequent_yields": "every day x4",
        "max_yield": 4,
        "max_yield_unfertilized": 4,
        "action_cost": 1,
        "yield_per_tile_per_day": 0.33,
        "market": {
            "I0": 10000, "T": 200,
            "below_func": "linear", "below_target": 0.40,
            "above_func": "sqrt", "above_target": 0.60
        }
    },
    "STRAWBERRY": {
        "type": "CROP",
        "yield_type": "Ongoing",
        "seed_cost": 100,
        "base_market_price": 120,
        "time_to_first_yield_days": 10,
        "time_to_max_yield_days": 16,
        "subsequent_yields": "every other day x4",
        "max_yield": 4,
        "max_yield_unfertilized": 4,
        "action_cost": 1,
        "yield_per_tile_per_day": 0.24,
        "market": {
            "I0": 10000, "T": 100,
            "below_func": "sqrt", "below_target": 0.70,
            "above_func": "linear", "above_target": 1.60
        }
    },
    "MELON": {
        "type": "CROP",
        "yield_type": "One-time",
        "seed_cost": 80,
        "base_market_price": 250,
        "time_to_first_yield_days": 10,
        "time_to_max_yield_days": 10,
        "subsequent_yields": None,
        "max_yield": 6,
        "max_yield_unfertilized": 6,
        "action_cost": 1,
        "yield_per_tile_per_day": 0.55,
        "market": {
            "I0": 10000, "T": 300,
            "below_func": "log", "below_target": 0.20,
            "above_func": "sq", "above_target": 3.60
        }
    },
    "GOOSE": {
        "type": "ANIMAL",
        "product": "EGG",
        "yield_type": "Ongoing",
        "seed_cost": 300,
        "base_market_price": 50, # Preço do ovo (Egg)
        "time_to_first_yield_days": 4,
        "time_to_max_yield_days": None,
        "subsequent_yields": "every day, indefinitely",
        "max_yield": 4, # held
        "max_yield_unfertilized": 4,
        "action_cost": 2, # 1 + 1 (build coop)
        "yield_per_tile_per_day": 1.00,
        "market": {
            "I0": 10000, "T": 332,
            "below_func": "linear", "below_target": 0.40,
            "above_func": "log", "above_target": 0.20
        }
    },
    "COW": {
        "type": "ANIMAL",
        "product": "MILK",
        "yield_type": "Ongoing",
        "seed_cost": 400,
        "base_market_price": 160, # Preço do leite (Milk)
        "time_to_first_yield_days": 8,
        "time_to_max_yield_days": None,
        "subsequent_yields": "every two days, indefinitely",
        "max_yield": 6, # held
        "max_yield_unfertilized": 6,
        "action_cost": 2, # 1 + 1 (build pasture)
        "yield_per_tile_per_day": 0.50,
        "market": {
            "I0": 10000, "T": 122,
            "below_func": "sqrt", "below_target": 0.60,
            "above_func": "linear", "above_target": 1.60
        }
    },
    "SHEEP": {
        "type": "ANIMAL",
        "product": "WOOL",
        "yield_type": "Ongoing",
        "seed_cost": 500,
        "base_market_price": 200, # Preço da lã (Wool)
        "time_to_first_yield_days": 6,
        "time_to_max_yield_days": None,
        "subsequent_yields": "every three days, indefinitely",
        "max_yield": 6, # held
        "max_yield_unfertilized": 6,
        "action_cost": 2, # 1 + 1 (build pasture)
        "yield_per_tile_per_day": 0.33,
        "market": {
            "I0": 10000, "T": 105,
            "below_func": "log", "below_target": 0.20,
            "above_func": "sq", "above_target": 3.20
        }
    },
    "FERTILIZER": {
        "type": "ITEM",
        "yield_type": None,
        "seed_cost": 100,
        "base_market_price": 100,
        "time_to_first_yield_days": None,
        "time_to_max_yield_days": None,
        "subsequent_yields": None,
        "max_yield": None,
        "max_yield_unfertilized": None,
        "action_cost": 1,
        "yield_per_tile_per_day": None,
        "market": {
            "I0": 10000, "T": 200,
            "below_func": "linear", "below_target": 0.40,
            "above_func": "linear", "above_target": 0.40
        }
    }
}

# ==========================================
# LOJAS DA CIDADE (TOWN BUILDINGS)
# ==========================================
# O que cada loja demanda (pode ter 2x do mesmo item, representado repetindo o item na lista)
TOWN_SHOPS = {
    "BAKERY": ["EGG", "WHEAT"],
    "PIZZA_SHOP": ["MILK", "TOMATO", "WHEAT"],
    "BRUNCH_SPOT": ["EGG", "WHEAT", "STRAWBERRY"],
    "YARN_STORE": ["WOOL", "WOOL"],
    "ICE_CREAM_SHOP": ["STRAWBERRY", "MILK", "WHEAT"],
    "PET_CAFE": ["CARROT", "CARROT"],
    "SMOOTHIE_SHOP": ["STRAWBERRY", "MILK"],
    "FARMERS_MARKET": ["WHEAT", "CARROT", "TOMATO", "STRAWBERRY"]
}

# ==========================================
# CONFIGURAÇÕES PADRÃO
# ==========================================
CONFIG_DEFAULTS = {
    "episodeSteps": 720,
    "boardSize": 10,
    "startingMoney": 3000,
    "maxMarketOrdersPerTurn": 10,
    "turnsPerDay": 24,
    "shedCapacity": 100,
    "weedSpawnChance": 0.005,
    "townShopUnlockInterval": 3,
    "townShopSellInterval": 4,
    "townCenterSellInterval": 24,
    "seed": None
}

# Helpers e Funções de Listagem
def get_crops():
    #Filtra e retorna apenas as culturas (CROP) do dicionário OBJECTS.#
    return {k: v for k, v in OBJECTS.items() if v.get("type") == "CROP"}

def get_animals():
    #Filtra e retorna apenas os animais (ANIMAL) do dicionário OBJECTS.
    return {k: v for k, v in OBJECTS.items() if v.get("type") == "ANIMAL"}

def get_products():
    #Retorna o mapeamento de produtos para o animal/item fonte original
    products = {}
    for k, v in OBJECTS.items():
        if v.get("type") == "ANIMAL":
            products[v.get("product")] = k
        elif v.get("type") == "CROP":
            products[k] = k
    products["FERTILIZER"] = "FERTILIZER"
    return products

def get_objects_dataframe():
   # Converte o dicionário OBJECTS para o formato de DF
    try:
        import pandas as pd
        df = pd.DataFrame.from_dict(OBJECTS, orient='index')
        market_df = df['market'].apply(pd.Series)
        df = pd.concat([df.drop(['market'], axis=1), market_df], axis=1)
        return df
    except ImportError:
        print("Pandas não está instalado.")
        return None
