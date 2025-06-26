# Calendar Spread Analysis: Contango, Backwardation & Mean Reversion Strategies
This project analyzes calendar spreads in the commodity futures market and implements two trading strategies based on the structure of the futures curve:

Method 1: Curve-Based Trading (Calendar Spread Slope Comparison)

Method 2: Mean Reversion (Spread Normalization with Threshold-Based Entry/Exit)

### Objective
To study and exploit contango, backwardation, and seasonal price behaviors in futures markets, and to evaluate performance using backtested PnL from 2023 to 2024.

### Key Results Summary
| Strategy     | Category       | Top Product(s) | Total Return (%) | Notes                              |
| ------------ | -------------- | -------------- | ---------------- | ---------------------------------- |
| **Method 1** | Contango       | ALE, GC        | 14.16%, 1.88%    | ALE shows consistent upward trends |
|              | Backwardation  | ZNA            | 5.11%            | Volatile, but potential returns    |
|              | Seasonal       | NG             | 0.09%            | Weak, trend-like seasonal bias     |
| **Method 2** | Mean Reversion | GC, ZNA        | 15.19%, 8.03%    | High variance, strong reversions   |
|              | Seasonal       | HO             | 0.003%           | Low variance, few signals          |

### Dataset
Period: 2014 – 2024
Contracts: Front (1st-nearest), Far (6th or 12th-nearest)
Source: Bloomberg PX_LAST (USD)

Contango: Copper (HG), Aluminum (ALE), Gold (GC)

Backwardation: Crude Oil (CL), Brent (CO), Zinc (ZNA)

Seasonal: Natural Gas (NG), Heating Oil (HO), Gasoline (XB)

Spread = Near-Term Price – Far-Term Price

### Performance Metrics
Initial Capital: $10,000

PnL:
Daily PnL = Position1 × ΔPrice (near) – Position2 × ΔPrice (far)

Total Return = Final Cumulative PnL / Initial Capital

### Conclusion
Curve-Based Strategy:

Effective in contango products with strong slope differentials (e.g., ALE, HG)

Backwardation is unstable, but ZNA showed occasional returns

Mean Reversion Strategy:

Performs best with volatile products (e.g., GC, ZNA)

Seasonal products fail to produce strong reversion signals due to low spread variance

