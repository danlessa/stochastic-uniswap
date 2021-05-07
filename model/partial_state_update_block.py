from .parts.uniswap_model import *


from random import choice, random

def s_generate_action(params, _2, _3, state, _5):

    action = {'event': None,
              'eth_balance': state['ETH_balance'],
              'token_balance': state['DAI_balance'],
              'eth_delta': 0.0,
              'token_delta': 0.0,
              'uni_delta': 0.0,
              'UNI_supply': state['UNI_supply']}

    events = {'TokenPurchase',
              'EthPurchase',
              'AddLiquidity',
              'Transfer'}

    event = choice(events)


    if event is 'TokenPurchase':
        delta_I = random()
        I_t = state['DAI_balance']
        O_t = state['ETH_balance']
        delta_O = get_output_amount(delta_I, I_t, O_t, params)
        action['eth_delta'] = delta_I
        action['eth_balance'] = I_t + delta_I
        action['token_delta'] = delta_O
        action['token_balance'] = O_t - delta_O
    elif event is 'EthPurchase':
        amount = random()
        pass
    elif event is 'AddLiquidity':
        delta_ETH = random()
        delta_DAI = random()
        pass
    elif event is 'Transfer':
        amount = random()
        pass

    return ('uniswap_action', action)


PSUBs = [
    {
        'policies': {

        },
        'variables': {
            'uniswap_action': s_generate_action
        }
    }
    {
        'policies': {
            'user_action': p_actionDecoder
        },
        'variables': {
            'DAI_balance': s_mechanismHub_DAI,
            'ETH_balance': s_mechanismHub_ETH,
            'UNI_supply': s_mechanismHub_UNI,
            'price_ratio': s_price_ratio
        }
    }

]
