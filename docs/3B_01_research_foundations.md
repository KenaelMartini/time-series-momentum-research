# Phase 3B.01 — Research Question & Hypothesis Formulation

## 1. Research Objective

**Project:** Robustness of Time-Series Momentum Across Asset Classes

L'objectif de cette recherche est d'étudier si les rendements passés d'un actif contiennent une information prédictive sur la direction de ses rendements futurs, et si cette relation est robuste à travers différentes classes d'actifs.

Notre approche vise d'abord à **identifier et évaluer un éventuel signal prédictif**, avant de chercher à construire une stratégie de trading exploitable.

## 2. Research Hypotheses

- **H0 — Null Hypothesis :** les rendements passés ne contiennent pas d'information prédictive sur la direction des rendements futurs.
- **H1 — Alternative Hypothesis :** les rendements passés contiennent une information prédictive directionnelle compatible avec un phénomène de Time-Series Momentum.

Nous chercherons également à distinguer le momentum d'un éventuel phénomène de *mean reversion*.

## 3. Preliminary Research Decisions

Les paramètres suivants ont été retenus provisoirement :

- **Primary signal :** rendement passé sur 12 mois.
- **Alternative lookbacks :** 3 et 6 mois.
- **Forward horizon :** 1 mois.
- **Signal frequency :** mensuelle.
- **Primary metric :** Balanced Accuracy.
- **Secondary metrics :** Accuracy, Recall et Confusion Matrix.
- **Baselines :** prédiction systématique de hausse et de baisse.
- **Asset classes :** Equities, Commodities, Forex et Bonds.
- **Universe :** plusieurs instruments par classe d'actifs, idéalement 16 à 20 au total.
- **Sample period :** période commune d'au moins 15 ans si la disponibilité des données le permet.
- **Evaluation :** séparation chronologique Train / Validation / Test.

Ces décisions restent à préciser avant la finalisation du protocole expérimental.

## 4. Methodological Considerations

Plusieurs risques ont été identifiés durant cette séance :

- **Look-ahead Bias :** le signal doit être construit uniquement avec les informations disponibles à sa date de calcul.
- **Overlapping Observations :** les signaux calculés sur 12 mois glissants partagent une grande partie de leur historique.
- **Data Snooping & Overfitting :** les paramètres et critères de sélection doivent être définis avant l'évaluation finale.
- **Sample Selection Bias :** les instruments ne doivent pas être sélectionnés en fonction des performances historiques du momentum.
- **Cross-Asset Comparability :** les résultats devront être analysés par instrument et par classe d'actifs.
- **Statistical Significance :** une Balanced Accuracy supérieure à 50 % ne constitue pas automatiquement une preuve de pouvoir prédictif.

Nous distinguerons systématiquement les performances prédictives du signal de la rentabilité économique d'une éventuelle stratégie.

## 5. Preliminary Research Framework

Notre démarche suivra les étapes suivantes :

Research Question → Hypotheses → Data Selection → Signal Construction → Statistical Evaluation → Robustness → Strategy Development → Backtesting → Research Publication.

Les résultats seront étudiés sur Train et Validation avant une évaluation finale sur Test, qui ne devra pas servir à ajuster les paramètres.

## 6. Next Steps

**Phase 3B.02 — Experimental Design**

- Sélectionner les instruments et les sources de données.
- Définir la période d'étude commune.
- Fixer les frontières Train / Validation / Test.
- Préciser le calcul des signaux et des métriques.
- Définir les tests statistiques et les contrôles de biais.

**Phase 3B.03 — Research Protocol Finalization (if needed)**

- Finaliser et documenter les décisions méthodologiques.
- Définir les critères de sélection des modèles.
- Figer le protocole avant l'analyse empirique principale.

**Following Phases**

- **3C :** Predictive Signal Analysis.
- **3D :** Strategy Construction.
- **3E :** Realistic Backtesting.
- **3F :** Statistical Robustness & Out-of-Sample Evaluation.
- **3G :** Research Publication.

## 7. Session Conclusion

Cette séance nous a permis de définir les fondations conceptuelles de notre recherche et d'identifier les principaux risques méthodologiques.

**Aucune conclusion empirique n'a encore été établie concernant l'existence ou la robustesse du Time-Series Momentum.**

La Phase 3B.01 constitue une étape de préparation scientifique. Le protocole définitif sera construit lors des prochaines séances, avant le début de l'analyse quantitative principale.
