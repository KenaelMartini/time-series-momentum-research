# Phase 3B.02 — Experimental Design & Data Availability Audit

## 1. Research Objective

**Project:** Robustness of Time-Series Momentum Across Asset Classes

Select the research universe, define the data source and period, and verify availability before signal analysis. Establish a rigorous experimental framework without presupposing that TSMOM works.

## 2. Research Universe

The universe comprises **16 ETFs equally distributed across four asset classes**:

| Class | Instruments | Exposures |
|---|---|---|
| Equities | SPY, VGK, EWJ, EEM | United States, Europe, Japan, emerging markets |
| Commodities | USO, DBA, DBB, DBC | Energy, agriculture, industrial metals, diversified basket |
| Bonds | IEF, TLT, LQD, HYG | Treasuries, investment-grade and high-yield credit |
| Forex | FXE, FXY, FXB, FXA | EUR, JPY, GBP and AUD against USD |

**Key trade-offs:**

- Commodities: prefer futures-exposed ETFs to a mix of physical and futures funds. Roll mechanisms differ, and DBC overlaps some exposures.
- Bonds: study sovereign rates and credit risk rather than four similar Treasury ETFs.
- Forex: recognize the common USD exposure, which limits independence.
- Equities: USD-listed international ETFs may incorporate currency effects.

If an ETF lacks adequate history, seek an economically comparable replacement without selecting instruments based on momentum results.

## 3. Data Source & Sample Period

- **Source:** Yahoo Finance via `yfinance`. The previously explored FactSet Formula access was not authorized under the available permissions.
- **Prices:** adjusted closes with `auto_adjust=True`, for USD-listed ETFs.
- **Frequency:** daily observations aggregated to month-end with `.resample("ME").last()`.
- **Evaluation:** January 2010–December 2025.
- **Warm-up:** download from January 2008 to support initial 12-month returns.

Results relate to ETF returns, not directly to underlying indices, spot prices or institutional futures contracts.

## 4. Data Availability Audit

Check missing values, chronological order, duplicates and nonpositive prices.

- 2010–2025: 4,024 dates × 16 ETFs, no missing values.
- 2009–2025: 4,276 dates × 16 ETFs, no missing values, duplicates or nonpositive prices; dates sorted.
- Extension to 2008: first monthly observation confirmed on January 31, 2008; complete 2008–2025 checks remain to be documented.

**Provisional conclusion:** all 16 ETFs have usable 2009–2025 history; no substitution is currently required. Structural checks do not guarantee economic data quality.

## 5. Python — Topics Covered

- Dictionaries of lists, key access and `.values()`.
- `.append()` versus `.extend()` for ticker lists.
- Python functions and passing parameters to `yf.download()`.
- Pandas checks: `.isna().sum()`, `.index.duplicated().sum()`, `.index.is_monotonic_increasing`, vectorized conditions and `.shape`.
- Monthly resampling with `.resample("ME").last()`.

**Errors identified:** confusion between lists and dictionaries, incorrect Forex tickers, misspelled `Commodities` key, nested list from `.append()`, and hard-coded values instead of declared function parameters.

A 12-month past return was calculated for exploration only, not as formal Phase 3C signal analysis.

## 6. Methodological Considerations

- **Common factors:** ETF correlations and shared USD factor for Forex.
- **Instrument structure:** fees, adjustments and commodity-futures roll effects.
- **Selection and survivorship bias:** currently available funds; document replacement criteria.
- **Look-ahead bias:** use only historical data for signal construction.

The Phase 3B.01 protocol remains provisional: 12-month momentum, 3- and 6-month alternatives, next-month prediction, Balanced Accuracy and chronological Train / Validation / Test separation.

## 7. Next Steps & Session Conclusion

Phase 3B.03 must complete the 2008–2025 data checks, set sample boundaries and parameter selection rules, and specify metrics, baselines and robustness tests before empirical analysis.

**Session 3B.02 completed:** 16 ETFs selected and satisfactory structural checks for 2009–2025. Python and data validation skills consolidated. Phase 3B remains in progress; no conclusion regarding TSMOM predictive power has been established.
