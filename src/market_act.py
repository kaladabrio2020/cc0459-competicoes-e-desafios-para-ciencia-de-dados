from data import crops, seed_cost, base_price, first_yield, max_yield, get_seeds_available, get_money, get_day, get_days_left

class MarketAct:
    """
    Classe responsável pelas decisões de mercado do agente:
    1. Venda de produtos colhidos armazenados no celeiro (shed).
    2. Compra inteligente de sementes avaliando saldo, estoque e tempo restante na temporada.
    """
    max_seed_stock = 2
    max_orders = 10

    def choose_seed_to_buy(self, obs):
        """
        Determina qual semente comprar avaliando o ROI diário com base
        no saldo atual, preço de mercado e tempo restante da temporada.
        """
        money = get_money(obs)
        days_left = get_days_left(obs)
        market_prices = obs.get('market', {}).get('prices', {})
       
        roi = {}
        for crop in crops:
            maturation = first_yield.get(crop, 999)
            cost = seed_cost.get(crop, 999)
            
            # Não compra se não houver tempo para colher ou saldo insuficiente
            if maturation > days_left or money < cost:
                continue
                
            # Preço atual de mercado (ou preço base) multiplicado pelo rendimento esperado
            unit_price = market_prices.get(crop, base_price.get(crop, 0))
            expected_units = max_yield.get(crop, 1)
            revenue = unit_price * expected_units
            
            # Lucro líquido por dia de ciclo
            roi[crop] = (revenue - cost) / max(maturation, 1)
            
        # Escolhe a semente com maior retorno diário 
        if not roi:
            return None
        return max(roi, key=roi.get)
        
    def sell_orders(self, obs):
        """
        Gera ordens de venda (SELL) para todos os produtos estocados no celeiro (shed).
        """
        orders = []
        shed = obs.get('private', {}).get('shed', {})
        for item, count in shed.items():
            if count > 0:
                orders.append(['SELL', item, count])
        return orders

    def buy_seed_orders(self, obs):
        """
        Gera ordens de compra de semente (BUY_SEED) respeitando o teto de estoque.
        """
        orders = []
        crop = self.choose_seed_to_buy(obs)
        if crop is not None:
            current_stock = get_seeds_available(obs, crop)
            if current_stock < self.max_seed_stock:
                orders.append(['BUY_SEED', crop, self.max_seed_stock-current_stock])
        return orders

    def next_actions(self, obs):
        """
        Retorna a lista de ações de mercado para o turno atual.
        """
        orders = []
        # 1. Vende a produção estocada
        orders.extend(self.sell_orders(obs))
        # 2. Compra sementes se necessário
        orders.extend(self.buy_seed_orders(obs))
        return orders[:self.max_orders]

    # Aliases convenientes
    act = next_actions
    get_orders = next_actions
