# Plan de départ — Arena_IA — Compétition VT Markets MT5
**2026-10-18 → 2026-12-18 | 1 000 $ | Rendement net = (equity finale - 1000)/1000**

> Outils `get_rules`/`get_arena` indisponibles dans cette session Arena (pas de pont MT5). Plan rédigé pour être exécuté manuellement par Pascal sur GO.

## En 5 lignes (exigence du premier passage)

1. **Survie d'abord :** 1-2 % Risque/trade au début (10-20 $), ≤3 positions simultanées (<6 % risque total, <10:1 levier) ; jamais plafond 5 % d'emblée.
2. **Univers restreint :** Forex majeures (EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD) + BTCUSD confirmés ; Or/Pétrole/Indices seulement après confirmation `get_rules` du nom exact avec suffixe VT Markets (XAUUSD-STD/ECN, USOIL, NAS100., etc.).
3. **Méthode :** Swing 4H/Daily trend-following sur repli, SL obligatoire technique (structure/ATR), R:R ≥1:1.5, pas de martingale, pas de moyenne à la baisse sans SL neuf, pas de hedge même symbole.
4. **Cadence :** 1-2 trades/semaine max, laisser SL/TP travailler entre passages, viser +8-12 % net sur 61 jours plutôt qu'un coup.
5. **Veille adversaires :** Lire `get_arena` à chaque passage, s'inspirer seulement si thèse validée et notée explicitement dans journal.

## Détails opérationnels

- **SL obligatoire et rapprochable seulement** (`modify_position` ne peut que rapprocher) → placer le SL définitif dès `place_order`, large techniquement mais serré en $ via taille.
- **Calcul taille :** volume = (risque $) / (distance SL en $ par lot). Vérifier aussi levier effectif = notionnel/equity ≤10.
- **Frais :** spreads + commissions + swaps inclus dans rendement net → éviter holds trop longs sur indices/forex à swap négatif sauf tendance forte ; privilégier entrées limit.
- **Journal :** chaque passage dans `JOURNAL.md` au format imposé avant/avec l'ordre, avec thèse (2-3 phrases), invalidation (prix/événement), influence adversaire, confiance 1-5.

## Ce que j'attends de Pascal avant GO

- Sortie exacte de `get_rules` : liste symboles autorisés avec orthographe exacte (suffixe) pour Or/Pétrole/Indices + levier max par symbole + specs contrat.
- Sortie `get_arena` : equity/balance/drawdown des 3 comptes + positions ouvertes adverses.

## Premier trade envisagé après GO (à confirmer avec prix live)

Aucun ordre avant GO. Piste prioritaire : pullback sur EURUSD ou AUDUSD en tendance Daily, ou XAUUSD si `get_rules` confirme le symbole, avec risque 1,5 % (≈15 $), SL 25-40 pips, TP 1,5-2R. Alternative si BTCUSD survendu/suracheté extrême Daily avec SL ATR.

