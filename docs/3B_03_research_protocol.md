# Phase 3B.03 — Research Protocol Finalization

## 1. Research Objective

**Project:** Robustness of Time-Series Momentum Across Asset Classes

L'objectif de cette séance est de **fixer les règles de notre étude avant l'analyse empirique**, afin d'éviter d'adapter les hypothèses ou les paramètres aux résultats observés.

Nous étudierons d'abord le **pouvoir prédictif directionnel** du Time-Series Momentum, indépendamment de la rentabilité d'une stratégie de trading.

## 2. Data & Sample Definition

L'univers défini en 3B.02 comprend **16 ETF**, répartis également entre Equities, Commodities, Bonds et Forex.

- **Source :** Yahoo Finance (`yfinance`), clôtures ajustées en USD.
- **Fréquence :** prix de fin de mois issus des données quotidiennes.
- **Historique téléchargé :** depuis janvier 2008, pour disposer d'une période préalable aux premiers signaux.
- **Période d'évaluation :** janvier 2010 à décembre 2025.

La disponibilité et l'intégrité des données ont été examinées dans `3B_02_data_availability.ipynb`. Les contrôles chiffrés détaillés déjà documentés portent sur 2009–2025 ; l'extension à 2008 a été confirmée pendant la séance, sans reproduire ici l'ensemble des résultats de contrôle.

## 3. Chronological Train / Validation / Test

| Ensemble | Période | Utilisation |
|---|---|---|
| **Train** | 2010–2017 | Étudier le comportement initial du signal et développer l'analyse |
| **Validation** | 2018–2021 | Examiner sa stabilité et les spécifications secondaires |
| **Test** | 2022–2025 | Évaluation finale *Out-of-Sample*, sans modification du protocole |

Les périodes sont définies selon le **mois du rendement futur à prédire**, et non selon les dates utilisées pour construire le signal.

L'historique antérieur à une frontière peut être utilisé : par exemple, le signal de janvier 2022 est construit fin décembre 2021. Ce n'est pas un *data leakage*, puisque ces prix sont déjà connus au moment de la prédiction. Le signal est recalculé chaque mois, sans réinitialisation de son historique.

**Out-of-Sample Protection :** la période Test (2022–2025) restera strictement réservée à la Phase 3F. Les Phases 3C, 3D et 3E utiliseront uniquement Train et Validation pour analyser les signaux, construire la stratégie et réaliser les backtests de développement.

Les performances prédictives et économiques du Test ne seront examinées qu'après avoir figé les paramètres, les règles de trading et la méthode d'évaluation statistique. Aucune modification ne pourra être justifiée par les résultats du Test sans compromettre son indépendance.

## 4. Signal & Prediction Target

- **Primary lookback :** rendement composé des 12 derniers mois, horizon fixé à l'avance.
- **Robustness lookbacks :** 3 et 6 mois, sans remplacer automatiquement le modèle principal selon leurs résultats.
- **Signal frequency :** mensuelle, après la dernière clôture disponible du mois.
- **Prediction horizon :** rendement du mois suivant.
- **Positive momentum :** prédiction de hausse (`1`).
- **Negative momentum :** prédiction de baisse (`0`).
- **Zero momentum :** signal neutre, sans prédiction binaire ; occurrence documentée.
- **Zero forward return :** observation exclue de l'évaluation binaire ; exclusion comptabilisée.

La **couverture des prédictions** (observations évaluables / observations disponibles) devra être indiquée. Le maintien éventuel d'une position lors d'un signal neutre relève de la Phase 3D, pas de cette étude prédictive.

## 5. Evaluation Metrics & Model Selection

La **Balanced Accuracy** est notre métrique principale : elle correspond à la moyenne du *Recall* des hausses et du *Recall* des baisses. Elle évite qu'une classe majoritaire domine artificiellement l'évaluation.

- **Secondary metrics :** Accuracy, Recall de chaque classe et Confusion Matrix.
- **Baselines :** prédictions *Always Long* et *Always Short*.
- **Primary specification :** lookback de **12 mois conservé**, même si 3 ou 6 mois affichent une meilleure performance en Validation.
- **Test discipline :** aucune sélection de paramètres ni révision des règles après consultation des résultats Test.

Une performance supérieure à 50 % en Balanced Accuracy ne constitue pas, à elle seule, une preuve statistique de pouvoir prédictif.

## 6. Cross-Asset Robustness & Statistical Limits

Les résultats seront présentés à **trois niveaux** : chaque ETF, chaque classe d'actifs et l'ensemble de l'univers. Les moyennes par classe donneront le même poids à chacun de leurs quatre instruments ; la moyenne globale donnera le même poids aux quatre classes. La dispersion des performances devra aussi être présentée.

Un contrôle *leave-one-asset-out* permettra de vérifier si les conclusions dépendent excessivement d'un instrument particulier.

Les principales limites à documenter sont :

- **Cross-Asset Dependence :** corrélation entre ETF, exposition commune au dollar et chevauchement de certaines expositions.
- **Temporal Dependence :** signaux calculés avec des fenêtres historiques glissantes et observations potentiellement dépendantes.
- **Selection & Survivorship Bias :** univers constitué d'ETF disponibles aujourd'hui, sans sélection sur leurs performances de momentum.
- **Statistical Uncertainty :** taille limitée du Test (48 mois par ETF), risques de faux positifs et comparaisons multiples.

En Phase 3F, nous estimerons l'incertitude (notamment par intervalles de confiance) et utiliserons des tests adaptés aux dépendances des données. **La méthode d'inférence précise devra être arrêtée avant l'examen des performances Test**, sans supposer qu'un *t-test* classique convient automatiquement à la Balanced Accuracy.

## 7. Session Conclusion & Next Steps

**Séance 3B.03 terminée :** les périodes d'évaluation, l'horizon principal, les conventions de classification, les métriques et les principes d'agrégation ont été définis.

**Phase 3B — Research Hypotheses & Experimental Protocol : terminée sur le plan du protocole prédictif.** Les choix encore nécessaires pour l'inférence statistique seront précisés avant toute utilisation confirmatoire du Test.

**Prochaines phases :** 3C — Predictive Signal Analysis, 3D — Strategy Construction et 3E — Realistic Backtesting seront réalisées sur Train et Validation. La Phase 3F permettra ensuite l'évaluation finale Out-of-Sample sur Test (2022–2025), avant la publication des résultats en Phase 3G.