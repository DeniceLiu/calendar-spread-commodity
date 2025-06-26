# main.py
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from strategy.curve import strategy_1, max_drawdown
from strategy.meanreversion import seasonal_strategy


def evaluate_results(results_dict, start_date='2023-01-01', initial_value=10000):
    summary = {}
    for key, value in results_dict.items():
        strategy, ticker_pair = key
        label = f"{ticker_pair[0]}-{ticker_pair[1]}"
        results = value['Results'].loc[start_date:].copy()

        if results.empty:
            continue

        cumulative_value = results['PnL'].cumsum() + initial_value
        total_return = (cumulative_value.iloc[-1] - initial_value) / initial_value
        mdd = max_drawdown(cumulative_value)

        summary[label] = {
            'Strategy': strategy,
            'Cumulative_Value': cumulative_value,
            'Total_Return': total_return,
            'Max_Drawdown': mdd
        }
    return summary

# Example plotting function for cumulative PnL
def plot_cumulative_pnl(summary_dict, initial_value=10000):
    fig, axes = plt.subplots(3, 3, figsize=(18, 12))
    axes = axes.flatten()

    for i, (label, data) in enumerate(summary_dict.items()):
        cum_val = data['Cumulative_Value']
        axes[i].plot(cum_val / initial_value - 1, label=label, linewidth=1.5)
        axes[i].set_title(label)
        axes[i].set_xlabel("Date")
        axes[i].set_ylabel("Cumulative Return")
        axes[i].grid(True, linestyle='--', linewidth=0.5)
        axes[i].tick_params(axis='x', rotation=45)
        axes[i].legend()

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.suptitle("Cumulative PnL Over Time by Product", y=1.02, fontsize=16)
    plt.show()

# Display final stats
def print_final_stats(summary_dict):
    print(f"{'Ticker':<20} {'Strategy':<15} {'Total Return (%)':>10} {'Max Drawdown (%)':>15}")
    print("-" * 70)
    for label, data in summary_dict.items():
        total_return = data['Total_Return'] * 100
        mdd = data['Max_Drawdown'] * 100
        print(f"{label:<20} {data['Strategy'].upper():<15} {total_return:>10.2f} {mdd:>15.2f}")

