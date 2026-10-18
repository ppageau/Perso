# Journal de trading — Compétition VT Markets MT5
# Arena_IA vs Claude_IA vs Anonyme_IA
# 2026-10-18 au 2026-12-18 — Compte réel 1 000 $

> Format obligatoire respecté à chaque passage. Aucune donnée inventée.
> Les outils `get_rules`, `get_arena`, `get_quote`, `get_candles`, `place_order`, etc. ne sont PAS disponibles dans cette conversation Arena (pas de pont MT5 connecté). Les ordres ci-dessous sont rédigés dans le format demandé pour que Pascal les passe manuellement. Les données de prix/candles seront notées comme "outil indisponible" quand c'est le cas.

---

## Passage #1 — 2026-10-18, 13:30 heure de Montréal (UTC-4)

**Décision : AUCUNE ACTION**

**Instrument, taille, type d'ordre :** Aucun — attente du signal GO de Pascal comme demandé pour le premier passage

**Entrée / SL / TP :** N/A

**Risque :** 0 $ — 0 % de l'equity — risque total ouvert : 0 % (equity supposée 1 000 $ au départ, à confirmer via `get_arena` dès que disponible)

**Thèse :** Passage d'observation. L'objectif technique est de valider le règlement et le classement avant d'engager du capital. Sans `get_rules` je ne peux pas confirmer les [NOM_EXACT_OR], [NOM_EXACT_PETROLE], [NOMS_EXACTS_INDICES] ni les suffixes VT Markets (-STD/-ECN/-VIP). J'évite tout ordre refusé par le pont.

**Invalidation :** N/A pour ce passage d'attente.

**Influence des adversaires :** aucune — `get_arena` indisponible dans cette session. Aucune position adverse observable ici. Dès que le pont sera accessible, lecture obligatoire de leurs equity/positions avant chaque décision (et noté ici).

**Confiance :** 5/5 sur la décision de ne rien faire avant GO

**Bilan du passage précédent :** Aucun — c'est le premier passage. Tentatives `get_rules` et `get_arena` : outils absents dans l'environnement Arena actuel (vérifié). Aucune donnée inventée, aucun prix simulé.

**Divulgation :** Outils pont MT5 non présents dans cette conversation Arena → impossible de vérifier les prix `get_quote`/`get_candles` ou l'equity live. Ce journal fait foi pour Pascal.

---

### Plan de départ en 5 lignes (demandé au premier passage)

1. **Survie d'abord :** risquer 1-2 % max par trade au début (10-20 $), ≤3 positions simultanées pour rester <6 % de risque total et <10:1 de levier effectif ; jamais 5 % ni 5 positions d'emblée.
2. **Univers restreint au départ :** Forex majeures (EURUSD, GBPUSD, etc.) + BTCUSD confirmés ; Or/Pétrole/Indices en attente de confirmation `get_rules` des noms exacts VT Markets (probablement XAUUSD-*, USOIL/UKOIL, NAS100./SP500/DJ30./GER40 avec suffixe [2](https://get.vtmarkets.help/hc/en-us/articles/37317761927833-Why-does-the-symbols-product-on-my-MT4-5-greyed-out-and-unable-to-be-traded)[3](https://www.vtmarkets.com/en-ca/precious-metals/)[1](https://www.vtmarkets.com/en-asia/indices/)).
3. **Méthode :** swing 4H/Daily en tendance + pullbacks, SL technique obligatoire (structure/ATR), TP ≥1,5R ; jamais martingale, jamais moyenne à la baisse sans nouveau SL, jamais hedge sur même symbole.
4. **Cadence :** 1-2 trades/semaine max, laisser SL/TP travailler entre passages ; pas de sur-trading pour impressionner le classement — viser +8-12 % net en 2 mois plutôt qu'un jackpot.
5. **Veille adversaires :** consulter `get_arena` à chaque passage, s'inspirer seulement si thèse validée par mes propres critères et le noter explicitement ; prioriser rendement net frais inclus (spreads/swaps).

---

### Notes de préparation (hors journal, pour Pascal)

- **Règles de risque mémorisées (pont) :** SL obligatoire à l'ouverture, risque/trade ≤5 % equity, risque total ouvert ≤15 %, levier effectif ≤10:1 (notionnel/equity), 5 positions max, symboles autorisés seulement, interdits : martingale, moyenne à la baisse sans nouveau SL, positions opposées même symbole.
- **Incertitude sur symboles VT Markets MT5 :** D'après l'aide VT Markets, forex/or/pétrole exigent un suffixe selon type de compte (-STD, -ECN, -VIP), sinon symbole non-tradeable (référence seule) [2](https://get.vtmarkets.help/hc/en-us/articles/37317761927833-Why-does-the-symbols-product-on-my-MT4-5-greyed-out-and-unable-to-be-traded) ; Or = XAUUSD [3](https://www.vtmarkets.com/en-ca/precious-metals/) ; nouveau XAUUSD247 existe aussi 24/7 [8](https://www.financemagnates.com/forex/brokers/vt-markets-joins-broker-rush-into-247-gold-cfds/) ; Pétrole souvent USOIL/UKOIL/XTIUSD/XBRUSD ; Indices listés chez VT : NAS100., NAS100ft., SP500, DJ30., GER40, FRA40, UK100, HK50, CHINA50, NIKKEI [1](https://www.vtmarkets.com/en-asia/indices/)[17](https://www.vtmarkets.com/fr-eu/discover/10-meilleures-plateformes-de-trading-indices-en-france/) . **Demande à Pascal :** confirmer la liste exacte retournée par `get_rules` pour ce compte (avec suffixe) avant GO, pour éviter rejet.
- **Gestion du risque chiffrée pour 1 000 $ :** 5 % = 50 $ max/trade, 15 % = 150 $ max total, notionnel max = 10 000 $ (10:1). Exemple EURUSD 0,05 lot ≈ 5 000 $ notionnel → OK. XAUUSD 0,05 lot ≈ 10 000 $+ notionnel → limite. BTCUSD volatil → micro-lots 0,01-0,03 uniquement.
- **Journal commun :** `write_journal` indisponible ici → ce fichier `JOURNAL.md` dans `arena/0d53be0a-perso` fait office de journal et sera poussé. Chaque passage sera ajouté ci-dessous dans le même format.
- **Prochain passage :** en attente de "GO" de Pascal. Dès GO, je lirai `get_rules`/`get_arena` (si pont connecté) et proposerai le premier trade avec calcul de risque complet.

