from att_matrix import AttMatrix
from farmer_act import FarmerAct
from market_act import MarketAct


att_m = AttMatrix()
farmer_act = FarmerAct()
market_act = MarketAct()

def dummy(obs):
    
    att_m.update(obs)    
    act = farmer_act.next_action(obs, att_m)
    market_cmd = market_act.next_actions(obs)
    
    cmd = {"farmer": act, "hands": [], "market": market_cmd}
    print(cmd)
    return cmd
