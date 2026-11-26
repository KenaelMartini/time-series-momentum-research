# Phase 3B.01 — Research Question & Hypothesis Formulation

## 1. Research Objective

**Project:** Robustness of Time-Series Momentum Across Asset Classes

Investigate whether past asset returns contain predictive information about future return directions and whether that relationship is robust across asset classes. First identify and evaluate a possible predictive signal before developing a tradable strategy.

## 2. Research Hypotheses

- **H0 — Null Hypothesis:** past returns contain no predictive information about future return direction.
- **H1 — Alternative Hypothesis:** past returns contain directional predictive information consistent with Time-Series Momentum.

Distinguish momentum from possible mean reversion.

## 3. Preliminary Research Decisions

- **Primary signal:** 12-month past return.
- **Alternative lookbacks:** 3 and 6 months.
- **Forward horizon:** 1 month.
- **Signal frequency:** monthly.
- **Primary metric:** Balanced Accuracy.
- **Secondary metrics:** Accuracy, Recall and Confusion Matrix.
- **Baselines:** constant positive and negative predictions.
- **Asset classes:** Equities, Commodities, Forex and Bonds.
- **Universe:** multiple instruments per class, ideally 16–20 overall.
- **Sample period:** a common period of at least 15 years if data availability permits.
- **Evaluation:** chronological Train / Validation / Test split.

These provisional decisions must be specified further before finalizing the experimental protocol.

## 4. Methodological Considerations

- **Look-ahead bias:** use only information available at signal formation.
- **Overlapping observations:** rolling 12-month signals share much of their history.
- **Data snooping and overfitting:** specify parameters and selection criteria before final evaluation.
- **Sample selection bias:** do not select instruments based on historical momentum performance.
- **Cross-asset comparability:** examine results by instrument and asset class.
- **Statistical significance:** Balanced Accuracy above 50% is not automatically evidence of predictive ability.

Distinguish predictive performance from economic profitability.

## 5. Preliminary Research Framework

Research Question → Hypotheses → Data Selection → Signal Construction → Statistical Evaluation → Robustness → Strategy Development → Backtesting → Research Publication.

Study Train and Validation before final Test evaluation; do not tune parameters using Test results.

## 6. Next Steps

**Phase 3B.02 — Experimental Design**

- Select instruments and data sources.
- Define the common study period and Train / Validation / Test boundaries.
- Specify signal and metric calculations, statistical tests and bias controls.

**Phase 3B.03 — Research Protocol Finalization (if needed)**

- Finalize and document methodological decisions and model selection criteria.
- Freeze the protocol before the main empirical analysis.

**Following Phases:** 3C — Predictive Signal Analysis; 3D — Strategy Construction; 3E — Realistic Backtesting; 3F — Statistical Robustness & Out-of-Sample Evaluation; 3G — Research Publication.

## 7. Session Conclusion

The conceptual foundations and main methodological risks have been identified. **No empirical conclusion has yet been established regarding the existence or robustness of TSMOM.** The final protocol will be developed before the main quantitative analysis.
