
# Robustness of Time-Series Momentum Across Asset Classes

## Project Overview

This project investigates the predictive properties and robustness of **Time-Series Momentum (TSMOM)** across different financial asset classes.

The main objective is to determine whether past asset returns contain useful information about the direction of future returns, and whether this relationship remains consistent across markets, time periods, and model specifications.

The project follows a systematic quantitative research process, from hypothesis formulation and data validation to statistical testing, strategy construction, realistic backtesting, and robustness analysis.

**The goal is not to prove that momentum works, but to evaluate the hypothesis using a rigorous and reproducible methodology.**

## Research Objectives

The research focuses on five questions:

1. Do past returns contain predictive information about future return direction?
2. Does the predictive relationship vary across asset classes?
3. How sensitive are the results to momentum lookback horizons?
4. Does the signal remain effective on unseen data?
5. Can any detected predictive relationship be translated into an economically meaningful trading strategy after accounting for risk and transaction costs?

## Asset Classes

The intended research universe includes:

- **Equities:** SPY, VGK, EWJ, EEM.
- **Commodities:** USO, DBA, DBB, DBC.
- **Foreign Exchange:** FXE, FXY, FXB, FXA.
- **Fixed Income:** IEF, TLT, LQD, HYG.

Session 3B.02 selected these 16 USD-listed ETFs. Historical data cover January 2008 through December 2025, with structural data checks documented in Phase 3B.02. The predictive research protocol was finalized in Phase 3B.03. ETF returns may reflect currency exposure, fees, credit risk, and commodity futures roll effects.

## Research Methodology

The research is organized around the following workflow:

**Research Question → Economic Intuition → Hypothesis → Data Collection → Data Validation → Signal Analysis → Statistical Testing → Strategy Construction → Backtesting → Robustness → Publication**

**Out-of-Sample Protection:** The Test period (2022–2025) will remain untouched during Phases 3C, 3D, and 3E. Signal analysis, strategy development, and preliminary backtesting will use only Train (2010–2017) and Validation (2018–2021). Final predictive and economic evaluation on Test will occur exclusively in Phase 3F, after all model specifications and evaluation procedures have been fixed.

The predictive research protocol includes:

- Monthly momentum signals based on historical returns.
- A 12-month reference lookback, with alternative horizons.
- One-month forward return evaluation.
- Directional prediction metrics, including Balanced Accuracy.
- Chronological Train / Validation / Test separation.
- Cross-asset and cross-period robustness analysis.
- Explicit controls for look-ahead bias, data snooping, overfitting, and other methodological risks.

The primary lookback is fixed at 12 months, with 3- and 6-month horizons used for robustness analysis. Statistical inference procedures will be specified before confirmatory evaluation of Test results.

## Project Roadmap

| Phase | Description | Status |
|---|---|---|
| 3A | Python & Research Infrastructure | Completed |
| 3B | Research Hypotheses & Experimental Protocol | Completed |
| 3C | Predictive Signal Analysis | Completed |
| 3D | Strategy Construction | Completed |
| 3E | Realistic Backtesting | In Progress |
| 3F | Statistical Robustness & Out-of-Sample Evaluation | Planned |
| 3G | Research Publication | Planned |

### Completed Sessions

**Phase 3A — Python & Research Infrastructure**

- Session 01: Temporal data manipulation, resampling, and financial returns.
- Session 02: Multi-asset data structures, groupby operations, merge/join, and alignment.
- Session 03: Data validation, debugging, and exception handling.

**Phase 3B — Research Design**

- Session 01: Research question, hypotheses, preliminary signal specifications, evaluation metrics, and methodological considerations.
- Session 02: Selection of 16 ETFs, data-source conventions, and historical data availability audit (2009–2025 checks completed).
- Session 03: Research protocol finalization, chronological Train / Validation / Test split, signal specifications, evaluation metrics, and robustness framework.

**Phase 3C — Predictive Signal Analysis**

- Session 01: Momentum signal construction, forward directional targets, temporal alignment, and data cleaning.
- Session 02: Predictive performance evaluation, Accuracy, Balanced Accuracy, Recall, confusion matrices, and naive baselines.
- Session 03: Cross-asset predictive analysis, lookback robustness, baseline comparisons, and reproducibility validation.

**Phase 3D — Strategy Construction**

- Session 01: Implementation and validation of 12-month TSMOM Long/Short/Flat positions, temporal alignment, position changes, and directional exposure analysis.
- Session 02: Equal Notional Weighting across 16 ETFs, monthly target portfolio weights, gross/net exposure calculations, and validation of portfolio exposure constraints.

**Phase 3E — Realistic Backtesting**

- Session 01: Monthly asset returns, gross portfolio return calculation, temporal alignment validation, and visual analysis of portfolio returns and exposures.
- Session 02: Completed and validated Train/Validation performance analysis, Equal-Weighted Long-Only benchmark comparison, CAGR, annualized volatility, Sharpe Ratio, Maximum Drawdown, comparative visualizations, and reusable performance metrics with numerical consistency verification.

### Next Steps

- **3E.03 — Transaction Costs, Turnover & Net Performance:** Implement portfolio turnover calculations, transaction cost modeling, and net performance evaluation across Train and Validation.
- **3F — Statistical Robustness & Out-of-Sample Evaluation:** Conduct robustness testing and perform the final evaluation on the untouched Test period (2022–2025).
- **3G — Research Publication:** Document the methodology, results, limitations, and conclusions in a final research report.

## Repository Structure

```text
time-series-momentum-research/
│
├── notebooks/
│   ├── 3A_01_temporal_data.ipynb
│   ├── 3A_02_data_manipulation.ipynb
│   ├── 3A_03_validation_debugging.ipynb
│   ├── 3B_02_data_availability.ipynb
│   ├── 3C_01_signal_construction.ipynb
│   ├── 3C_02_predictive_analysis.ipynb
│   ├── 3C_03_cross_asset_lookback_robustness.ipynb
│   ├── 3D_01_strategy_rules.ipynb
│   ├── 3D_02_portfolio_construction.ipynb
│   ├── 3E_01_portfolio_returns.ipynb
│   └── 3E_02_performance_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── signals.py
│   ├── research.py
│   ├── strategy.py
│   ├── metrics.py
│   └── utils.py
│
├── docs/
│   ├── 3B_01_research_foundations.md
│   ├── 3B_02_experimental_design.md
│   └── 3B_03_research_protocol.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

The repository evolves progressively as the research advances. Research notebooks document the experimental process, while reusable Python functions are maintained in `src/` to improve reproducibility, modularity, and maintainability.

### Research Infrastructure

- **`data.py`:** Market data downloading, monthly price resampling, data integrity validation, and reusable monthly price preparation.
- **`signals.py`:** Momentum calculation, directional signal and target generation, and signal-target cleaning.
- **`research.py`:** Sample preparation, predictive metrics, naive baselines, and robustness analysis.
- **`strategy.py`:** TSMOM position construction, Equal Notional portfolio weighting, gross/net exposure calculations, and reusable monthly gross portfolio return calculations.
- **`metrics.py`:** Reusable portfolio performance and risk metrics, including CAGR, annualized volatility, Sharpe Ratio, and Maximum Drawdown.

### Current Development Status

**Phase 3D — Strategy Construction: Completed and validated.**

**Phase 3E — Realistic Backtesting: In Progress.**

- **3E.01 (Completed):** Monthly gross portfolio returns, temporal alignment validation, and exposure visualizations.
- **3E.02 (Completed):** Train/Validation performance and risk analysis against an Equal-Weighted Long-Only benchmark.
- Implemented CAGR, annualized volatility, Sharpe Ratio, and Maximum Drawdown calculations.
- Developed comparative equity curves, drawdown charts, performance tables, and metric visualizations.
- Created the reusable `calculate_performance_metrics()` function in `src/metrics.py`.
- Verified numerical consistency between the original calculations and the reusable function using `DataFrame.equals()`.

**Current focus: Phase 3E.03 — Transaction Costs, Turnover & Net Performance.**

Transaction costs, slippage, and financing costs have not yet been incorporated into strategy returns.

The Test period (2022–2025) remains untouched until Phase 3F.

## Research Documentation

- [Phase 3B.01 — Research Foundations](docs/3B_01_research_foundations.md)
- [Phase 3B.02 — Experimental Design & Data Availability Audit](docs/3B_02_experimental_design.md)
- [Phase 3B.03 — Research Protocol Finalization](docs/3B_03_research_protocol.md)

Additional documentation, experimental protocols, research results, and reproducible analyses will be added progressively.

## Technical Environment

The project uses Python and standard data analysis libraries, including:

- pandas
- NumPy
- matplotlib
- yfinance

Dependencies are managed through `requirements.txt`.

To install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

## Research Limitations

Phase 3C found limited evidence of directional predictive ability. Across 16 ETFs and three momentum lookbacks (3M, 6M, 12M), no ETF consistently outperformed both naive baselines across all periods and specifications.

Phase 3D established systematic trading positions and Equal Notional portfolio weights. However, successful position and exposure validation does not establish economic profitability.

Phase 3E.01 implemented and validated monthly gross portfolio returns.

Phase 3E.02 evaluated TSMOM performance against an Equal-Weighted Long-Only benchmark across Train (2010–2017) and Validation (2018–2021).

TSMOM exhibited lower CAGR and Sharpe Ratios than the benchmark in both periods, alongside lower annualized volatility and smaller maximum drawdowns.

These findings do not establish economic profitability or statistical significance. The analysis remains based on gross returns and excludes transaction costs, slippage, financing costs, and other implementation frictions.

Key limitations include:

- **Statistical inference:** Predictive results have not yet established statistical significance.
- **ETF proxies:** Returns may be affected by management fees, tracking differences, currency exposure, credit risk, and futures roll effects.
- **Portfolio construction:** Equal Notional Weighting does not account for differences in asset volatility, correlations, or risk contributions.
- **Trading frictions:** Transaction costs, slippage, financing costs, short-selling constraints, and realized portfolio turnover have not yet been modeled.
- **Selection and model risk:** Survivorship bias, data snooping, and overfitting remain relevant methodological risks.

Phase 3E will evaluate economic performance and realistic trading frictions on Train and Validation.

The Test period (2022–2025) remains untouched until Phase 3F.

## Author

**Kenael Martini**

Independent Quantitative Finance Research Project

*Focus: Quantitative Research, Systematic Strategies, Financial Data Analysis, and Backtesting.*
