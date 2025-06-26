# strategy_1.py
import pandas as pd
import matplotlib.pyplot as plt

def strategy_1(front_price, back_price, window=1, type='contango'):
    if type not in ['contango', 'backwardation']:
        print("Seasonal must be converted to contango or backwardated types")
        return

    front_deriv = front_price.diff().rolling(window).mean()
    back_deriv = back_price.diff().rolling(window).mean()
    back_deriv = back_deriv.loc[front_deriv.index]

    weight = pd.DataFrame(index=front_deriv.index, columns=[front_price.name, back_price.name])

    if type == 'contango':
        weight[front_deriv > back_deriv] = -1
        weight[front_deriv < back_deriv] = 1
        weight[back_price.name] = -weight[front_price.name]
    else:
        weight[front_deriv > back_deriv] = 1
        weight[front_deriv < back_deriv] = -1
        weight[back_price.name] = -weight[front_price.name]

    weight = weight.shift(1).fillna(0)

    front_return = front_price.diff().fillna(0)
    back_return = back_price.diff().fillna(0)

    pnl = weight[front_price.name] * front_return - weight[back_price.name] * back_return

    results = pd.DataFrame({
        'Front_Price': front_price,
        'Back_Price': back_price,
        'Weight_Front': weight[front_price.name],
        'Weight_Back': weight[back_price.name],
        'Front_Change': front_return,
        'Back_Change': back_return,
        'PnL': pnl
    })

    return weight, pnl, results

def max_drawdown(cumulative_values):
    running_max = cumulative_values.cummax()
    drawdown = (cumulative_values - running_max) / running_max
    return drawdown.min()