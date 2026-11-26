# Phase 3B.03 — Research Protocol Finalization

## 1. Research Objective

**Project:** Robustness of Time-Series Momentum Across Asset Classes

Fix the study rules before empirical analysis to avoid adapting hypotheses or parameters to observed results. First evaluate directional predictive ability independently of trading strategy profitability.

## 2. Data & Sample Definition

The Phase 3B.02 universe comprises **16 ETFs**, equally distributed across Equities, Commodities, Bonds and Forex.

- **Source:** Yahoo Finance (`yfinance`), USD adjusted closes.
- **Frequency:** month-end prices derived from daily data.
- **Downloaded history:** from January 2008 for signal warm-up.
- **Evaluation:** January 2010–December 2025.

Data availability and integrity were examined in `3B_02_data_availability.ipynb`. Detailed documented numerical checks cover 2009–2025; the extension to 2008 was confirmed without reproducing all check results here.

## 3. Chronological Train / Validation / Test

| Sample | Period | Purpose |
|---|---|---|
| **Train** | 2010–2017 | Study initial signal behavior and develop the analysis |
| **Validation** | 2018–2021 | Examine stability and secondary specifications |
| **Test** | 2022–2025 | Final out-of-sample evaluation without protocol changes |

Periods are defined by the **realized return month to be predicted**, not the signal formation date. Earlier history may be used across a boundary: the prediction for January 2022 is formed at the end of December 2021 using already available prices. Signals are recalculated monthly without resetting their history.

**Out-of-sample protection:** reserve Test for Phase 3F. Phases 3C, 3D and 3E use Train and Validation for signal analysis, strategy construction and development backtests. Examine Test predictive and economic performance only after fixing parameters, trading rules and statistical evaluation procedures. Test-driven revisions would compromise its independence.

## 4. Signal & Prediction Target

- **Primary lookback:** cumulative return over the preceding 12 months, fixed in advance.
- **Robustness lookbacks:** 3 and 6 months; do not automatically replace the primary model based on results.
- **Signal frequency:** monthly, after the last available closing price.
- **Prediction horizon:** next-month return.
- **Positive momentum:** positive prediction (`1`).
- **Negative momentum:** negative prediction (`0` in the original protocol).
- **Zero momentum:** neutral, no binary prediction; document frequency.
- **Zero forward return:** exclude from binary evaluation and count exclusions.

Report prediction coverage (evaluable observations / available observations). Whether to retain a position on a neutral signal is a Phase 3D decision, not part of predictive analysis.

> Implementation note (documentation harmonization): the subsequent code encodes negative directions as −1, positive as +1, and neutral as 0. This is an encoding change, not a revision of the economic hypothesis or sample boundaries.

## 5. Evaluation Metrics & Model Selection

Balanced Accuracy is the primary metric: the mean of positive and negative Recall, preventing majority-class dominance.

- **Secondary metrics:** Accuracy, class-specific Recall and Confusion Matrix.
- **Baselines:** Always Long and Always Short.
- **Primary specification:** retain 12 months even if 3 or 6 months perform better on Validation.
- **Test discipline:** no parameter selection or rule revision after inspecting Test.

Balanced Accuracy above 50% alone does not establish statistical predictive ability.

## 6. Cross-Asset Robustness & Statistical Limits

Report results at three levels: ETF, asset class and entire universe. Under the planned aggregation, class means give equal weight to each of four instruments and the overall class-based mean gives equal weight to each of four classes. Report dispersion as well. A leave-one-asset-out check will assess whether conclusions depend excessively on one instrument.

Main limitations:

- **Cross-asset dependence:** ETF correlations, common USD exposure and overlapping exposures.
- **Temporal dependence:** rolling historical windows and potentially dependent observations.
- **Selection and survivorship bias:** currently available ETFs, not selected on momentum performance.
- **Statistical uncertainty:** limited Test sample (48 months per ETF), false positives and multiple comparisons.

Phase 3F will estimate uncertainty (including confidence intervals) and use tests appropriate for dependence. Specify the inference method before examining Test performance; do not assume a conventional t-test is automatically appropriate for Balanced Accuracy.

## 7. Session Conclusion & Next Steps

Session 3B.03 completed: evaluation periods, primary horizon, classification conventions, metrics and aggregation principles defined. Phase 3B's predictive protocol is complete; remaining inference choices must be specified before confirmatory Test use.

Phases 3C, 3D and 3E are conducted on Train and Validation. Phase 3F performs final out-of-sample evaluation on Test (2022–2025), followed by Phase 3G publication.
