# src/modulo_auxiliar.py

from constantes import OBJECTS


def _step_toward(fx, fy, tx, ty):
    """Retorna a direção de movimento (NORTH, SOUTH, EAST, WEST) em direção ao destino (tx, ty)."""
    if fx > tx:
        return "WEST"
    if fx < tx:
        return "EAST"
    if fy > ty:
        return "NORTH"
    if fy < ty:
        return "SOUTH"
    return None


def _find_target_tile(farm, board_size, have_seed):
    """Encontra o tile prioritário mais próximo para colher, regar ou plantar melão."""
    fx, fy = farm["farmer"]
    candidates = []
    for y in range(board_size):
        for x in range(board_size):
            tile = farm["tiles"][y][x]
            if isinstance(tile, dict) and tile.get("kind") == "PLANT" and tile["crop"] == "MELON":
                purpose = None
                # Colhe se já tiver produção disponível
                age_ok = tile["yield_units"] > 0
                if age_ok and tile.get("planted_day") is not None:
                    purpose = "harvest"
                if not tile["watered_today"]:
                    purpose = "water" if purpose is None else purpose
                if purpose:
                    candidates.append((x, y, purpose))
            elif tile is None and have_seed:
                candidates.append((x, y, "plant"))

    if not candidates:
        return None

    priority = {"harvest": 0, "water": 1, "plant": 2}
    candidates.sort(key=lambda c: (priority[c[2]], abs(c[0] - fx) + abs(c[1] - fy)))
    return candidates[0]


def get_crops():
    """Filtra e retorna apenas as culturas (CROP) do dicionário OBJECTS."""
    return {k: v for k, v in OBJECTS.items() if v.get("type") == "CROP"}


def get_animals():
    """Filtra e retorna apenas os animais (ANIMAL) do dicionário OBJECTS."""
    return {k: v for k, v in OBJECTS.items() if v.get("type") == "ANIMAL"}


def get_products():
    """Retorna o mapeamento de produtos para o animal/item fonte original."""
    products = {}
    for k, v in OBJECTS.items():
        if v.get("type") == "ANIMAL":
            products[v.get("product")] = k
        elif v.get("type") == "CROP":
            products[k] = k
    products["FERTILIZER"] = "FERTILIZER"
    return products


def get_objects_dataframe():
    """Converte o dicionário OBJECTS para um DataFrame do pandas."""
    try:
        import pandas as pd

        df = pd.DataFrame.from_dict(OBJECTS, orient="index")
        market_df = df["market"].apply(pd.Series)
        df = pd.concat([df.drop(["market"], axis=1), market_df], axis=1)
        return df
    except ImportError:
        print("Pandas não está instalado.")
        return None

