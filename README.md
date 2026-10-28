
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
| 3C | Predictive Signal Analysis | In Progress — Session 3C.01 Completed |
| 3D | Strategy Construction | Planned |
| 3E | Realistic Backtesting | Planned |
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

- Session 01: Monthly momentum signal construction, one-month forward returns and directional targets, Train / Validation preparation, temporal alignment, data cleaning, and validation checks.

### Next Steps


- **3C.02 — Predictive Analysis:** Begin by refactoring the signal and target cleaning logic into a reusable function in `src/signals.py`. Then evaluate the 12-month momentum signal using Accuracy, Balanced Accuracy, directional Recall, confusion matrices, and baseline comparisons.
- **3C.03 — Cross-Asset & Lookback Robustness:** Analyze predictive performance across assets and asset classes, and compare the predefined 3-, 6-, and 12-month momentum horizons.
- **3D — Strategy Construction:** Translate predictive signals into systematic trading rules without accessing Test results.
- **3E — Realistic Backtesting:** Evaluate strategy performance on Train and Validation, including transaction costs, slippage, turnover, and risk metrics.
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
│   └── 3C_01_signal_construction.ipynb
│
├── src/
│   ├── data.py
│   └── signals.py
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

The repository will evolve as the research progresses. Reusable Python functions are progressively separated from research notebooks to improve code organization, reproducibility, and maintainability.

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

Phase 3C.01 has completed the construction and validation of the primary 12-month momentum dataset, with 1,531 valid Train observations and 765 valid Validation observations.

Predictive performance and statistical robustness have not yet been evaluated. The 16 ETF proxies may introduce structural biases related to fees, currency exposure, credit risk, and futures roll effects.

Future analyses will address temporal dependence, data leakage, overfitting, transaction costs, and model robustness. The Test period (2022–2025) remains untouched until Phase 3F.

No statistically robust predictive relationship or economically exploitable strategy has been established.

## Author

**Kenael Martini**

Independent Quantitative Finance Research Project

*Focus: Quantitative Research, Systematic Strategies, Financial Data Analysis, and Backtesting.*
