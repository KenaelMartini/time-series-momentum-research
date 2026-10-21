
# Phase 3B.02 — Experimental Design & Data Availability Audit

## 1. Research Objective

**Project:** Robustness of Time-Series Momentum Across Asset Classes

L'objectif de cette séance est de **sélectionner notre univers de recherche**, de définir la source et la période des données, puis de vérifier leur disponibilité avant l'analyse des signaux.

Nous cherchons à construire un cadre expérimental rigoureux, sans présupposer que le Time-Series Momentum fonctionne.

## 2. Research Universe

Nous avons retenu **16 ETF répartis équitablement entre quatre classes d'actifs** :

| Classe | Instruments | Expositions |
|---|---|---|
| Equities | SPY, VGK, EWJ, EEM | États-Unis, Europe, Japon, marchés émergents |
| Commodities | USO, DBA, DBB, DBC | Énergie, agriculture, métaux industriels, panier diversifié |
| Bonds | IEF, TLT, LQD, HYG | Treasuries, crédit Investment Grade et High Yield |
| Forex | FXE, FXY, FXB, FXA | EUR, JPY, GBP et AUD contre USD |

**Principaux arbitrages :**

- **Commodities :** privilégier des ETF exposés aux futures plutôt qu'un mélange de fonds physiques et de fonds sur futures. Les mécanismes de *roll* restent différents ; DBC recoupe certaines expositions.
- **Bonds :** étudier les taux souverains et le risque de crédit, plutôt que quatre ETF de Treasuries similaires.
- **Forex :** reconnaître que les quatre devises partagent une exposition au dollar, ce qui limite leur indépendance.
- **Equities :** les ETF sont cotés en USD ; leurs rendements internationaux peuvent intégrer un effet de change.

Si un ETF présente un historique insuffisant, nous chercherons **un remplaçant économiquement comparable**, sans sélectionner les instruments selon les résultats du momentum.

## 3. Data Source & Sample Period

- **Source :** Yahoo Finance via `yfinance`. L'accès FactSet Formula étudié précédemment n'était pas autorisé par les droits disponibles.
- **Prix :** clôtures ajustées avec `auto_adjust=True`, pour des ETF cotés en USD.
- **Fréquence :** données quotidiennes, agrégées en prix de fin de mois avec `.resample("ME").last()`.
- **Période d'évaluation :** janvier 2010 à décembre 2025.
- **Historique préalable :** téléchargement depuis janvier 2008 pour disposer des prix nécessaires aux premiers rendements passés sur 12 mois.

Les résultats concerneront les **rendements de ces ETF**, et non directement ceux des indices, des cours *spot* ou de contrats futures institutionnels.

## 4. Data Availability Audit

Nous avons vérifié les valeurs manquantes, l'ordre des dates, les doublons et les prix non positifs.

- **2010–2025 :** 4 024 dates × 16 ETF ; aucune valeur manquante.
- **2009–2025 :** 4 276 dates × 16 ETF ; aucune valeur manquante, aucun doublon et aucun prix non positif ; dates ordonnées.
- **Extension à 2008 :** première observation mensuelle confirmée au 31 janvier 2008 ; contrôles complets de 2008–2025 encore à consigner.

**Conclusion provisoire :** les 16 ETF disposent d'un historique exploitable sur 2009–2025. Aucune substitution n'est nécessaire à ce stade. L'absence d'anomalies structurelles ne garantit toutefois pas la qualité économique des séries.

## 5. Python — Notions travaillées

Cette séance a permis de réviser :

- Les dictionnaires de listes, l'accès par clé et la méthode `.values()`.
- La différence entre `.append()` et `.extend()` pour construire la liste des tickers.
- Les fonctions Python et la transmission effective des paramètres à `yf.download()`.
- Les contrôles pandas : `.isna().sum()`, `.index.duplicated().sum()`, `.index.is_monotonic_increasing`, conditions vectorisées et `.shape`.
- Le *resampling* mensuel avec `.resample("ME").last()`.

**Erreurs identifiées :** confusion initiale entre liste et dictionnaire, tickers Forex incorrects, clé `Commodities` mal orthographiée, liste imbriquée avec `.append()` et paramètres déclarés mais codés en dur dans la fonction.

Un rendement passé sur 12 mois a été calculé à titre exploratoire. Cela ne constitue **pas encore une analyse du signal**, qui appartient à la Phase 3C.

## 6. Methodological Considerations

Les limites identifiées sont notamment :

- **Common Factors :** corrélations entre ETF et facteur USD commun aux instruments Forex.
- **Instrument Structure :** frais, ajustements et mécanismes de *roll* des ETF sur matières premières.
- **Selection & Survivorship Bias :** univers composé de fonds actuellement disponibles ; critères de remplacement à documenter.
- **Look-ahead Bias :** utiliser exclusivement des données passées pour construire le signal.

Le protocole issu de 3B.01 reste provisoire : **momentum 12 mois**, alternatives **3 et 6 mois**, prédiction du **mois suivant**, **Balanced Accuracy** et séparation **Train / Validation / Test**.

## 7. Next Steps & Session Conclusion

Une **séance 3B.03** est nécessaire pour :

- Terminer les contrôles de données sur **2008–2025**.
- Fixer les frontières Train / Validation / Test et les règles de sélection des paramètres.
- Préciser les métriques, les *baselines* et les tests de robustesse avant l'analyse empirique.

**Séance 3B.02 terminée :** univers de 16 ETF sélectionné et contrôles structurels satisfaisants sur 2009–2025. Les notions de Python et de validation des données ont été consolidées.

**La Phase 3B reste en cours.** Aucune conclusion concernant le pouvoir prédictif du Time-Series Momentum n'a encore été établie.
