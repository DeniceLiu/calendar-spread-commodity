# strategy_2.py
import pandas as pd

def seasonal_strategy(data, product_name):
    spread_column = f"{product_name}_Spread"
    data = data[['Date', spread_column]].dropna().sort_values(by='Date')
    data['Year'] = data['Date'].dt.year

    yearly_stats = data.groupby('Year')[spread_column].agg(['mean', 'var']).reset_index()
    yearly_stats.rename(columns={'mean': 'Yearly_Mean', 'var': 'Yearly_Var'}, inplace=True)

    data = data.merge(yearly_stats, on='Year', how='left')
    data['Up'] = data['Yearly_Mean'] + 0.25 * data['Yearly_Var']
    data['Down'] = data['Yearly_Mean'] - 0.25 * data['Yearly_Var']
    data['Up_Stop'] = data['Yearly_Mean'] + 3 * data['Yearly_Var']
    data['Down_Stop'] = data['Yearly_Mean'] - 3 * data['Yearly_Var']

    data[f'W_{product_name}_1'] = 0
    data[f'W_{product_name}_6'] = 0

    for i in range(1, len(data)):
        prev = data.iloc[i - 1]
        pos1 = prev[f'W_{product_name}_1']
        pos2 = prev[f'W_{product_name}_6']
        spread = prev[spread_column]

        if pos1 == 0 and pos2 == 0:
            if spread > prev['Up']:
                pos1, pos2 = 1, -1
            elif spread < prev['Down']:
                pos1, pos2 = -1, 1
        elif pos1 > 0:
            if spread <= prev['Yearly_Mean'] or spread > prev['Up_Stop']:
                pos1, pos2 = 0, 0
        elif pos1 < 0:
            if spread >= prev['Yearly_Mean'] or spread < prev['Down_Stop']:
                pos1, pos2 = 0, 0

        data.loc[i, f'W_{product_name}_1'] = pos1
        data.loc[i, f'W_{product_name}_6'] = pos2

    return data
