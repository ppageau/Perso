# LEDGER Arena_IA (Anonyme IA) — compétition VT Markets 2026-10-18 → 2026-12-18

## Paramètres compte (règles v2 du 20 oct., remplacent les précédentes)
- Equity départ 1 000 USD. Plafonds : 5 %/trade (groupes corrélés = 1 trade), **15 % total open+limites** (risque = perte au SL ; SL au-delà de l'entrée = 0), levier ≤10:1 continu, R:R ≥2:1 au SL/TP d'origine, 5-8 symboles.
- Freins : −5 %/jour (stop nouveaux trades) ; −10 %/semaine (risque ÷2 fin de semaine) ; **élimination si capital ≤750 $** (marge avant élimination = capital−750 ; je garde « capital si SL » ≥780 $ à tout passage).
- Fin : 18 déc. 16 h flat forcé ; gagnant = non éliminée la plus riche ; aucun TP/EXP après 18 déc. 15 h.
- Si retardataire : approche plafonds +1 trade/jour max (jamais pour écart flottant <2-3 %).
- Swaps 17 h ; week-end parfois ×3 (check ven. 13 h 45). TP ≥10× swap prévu. Coûts : spread+commission+|swap|×nuits ≤15 % reward TP (ETF ≈8,40 $/ordre → bannis).
- Journal 3 lignes/passage + revue dimanche.

## Univers (7) : XAUUSD-STD, NAS100, SP500, NVDA.24H, EURUSD-STD, USDJPY-STD, USOUSD-STD (+BTCUSD occasions courtes)
SOXL/ETF ×3 RETIRÉS (commission 16,85 CAD/trade tue le R:R aux tailles utiles). Règle coûts : spread+commission+|swap|×nuits ≤15 % du reward TP.
Note : variantes futures (NAS100ft.) peuvent avoir swap ≠ fiche → toujours lire colonne Swap du PDF.

## Protocole dashboard (chaque passage)
1. Retard : capital si TP > capital leader ? sinon chercher setup qualité (jamais forcé).
2. Tête : toute IA dont capital si TP > mon capital → sécuriser (TP partiel / SL entrée) avant rattrapage.
3. R:R via colonnes ≥3. 4. Capital si SL des autres = carte des effondrements possibles (ne pas copier). 5. Potentiel = scénario.
Avance <2 % → SL à l'entrée sur positions gagnantes prio ; avance >2 % → rulebook BE à +1R.

## Colonnes maison au 19 oct. 23 h (USD)
NAS100 open : TP +119,97 / SL −33,03 (→ −0,03 après SL entrée) | or limite : +125/−30 | NVDA limite : +48/−15 | BTC stop : +51/−17.
Capital si TP 1 354,93 $ ; si SL 948,96 $ (post-sécurisation). Gemini si TP ≈1 233 CAD > mon capital → sécurisation NAS100 déclenchée.

## Positions/ordres au 20 oct. 11 h (tickets MT5, PDF 10:56 + passage #5)
1. #2512780828 XAUUSD-STD VENTE 0,01 @ 4 152 | SL 4 192 | TP 4 072 | open 20/10 10:27 | carry short +0,367 CAD/nuit | gestion : +1R (4 112) → SL BE ; pas de partielle (pas 0,01) ; VEN 13h45 : ≥+1R → SL BE + week-end porté (swap ×3 positif), < +1R → FERMER avant 15h45 (pas de week-end non sécurisé).
2. #2512780832 USOUSD-STD ACHAT limite 0,01 @ 95,50 | SL 93,00 | TP 101,50 | EXP ven. 23 14 h | carry long +0,17/nuit | risque 25 $.
3. NVDA.24H VENTE limite 1,5 @ 222 | SL 232 | TP 202 | EXP mer. 21 14 h (replacée au passage #5, nouveau ticket à confirmer au prochain PDF) | risque 15 $.
Fermé : NAS100ft. #2512319695 SL entrée tagué 20/10 10:27 (−0,22 $). Expiré : stop BTC 80 500. Annulée : SOXL (commission).
Total si tout fillé : 80 $ = 7,9 % ; groupes : or 40 (4,0 %), {NAS100+NVDA} 15 (1,5 %), pétrole 25 (2,5 %) ; levier plein ≈5,4:1.

## Passages (depuis le 20 oct.) : 9h05, 10h45, 13h45, 15h45, 19h + ad hoc + dimanche 19h
- 9h05 : limites ET entrées marché du jour : hors fenêtre ±30 min des annonces 8h30 (finie à 9h00) et 9h45 (début 9h15).
- 10h45 : gestion des fills/SL de l'open US, annulation limites mortes.
- 13h45 : revue swap 17h + réductions ; dernier créneau pré-FOMC (décision 14h).
- 15h45 : exécution finale avant clôture cash 16h, gel Actions/ETF, swap 17h, résultats ~16h10.
- 19h : post-clôture, ouverture Tokyo, swings multi-jours. Ad hoc : chocs/gaps.

## Calendrier noir
FOMC 27-28 oct. (déc. 28 14h ET) ; CPI 10 nov., 10 déc. ; NFP 6 nov., 4 déc. ; GDP/PCE 29 oct., 25 nov. ; FOMC 8-9 déc. (déc. 9) ; résultats Meta+Tesla mer. 21 oct. AC ; Netflix/GM mar. 20 ; P&G jeu. 22.
Règle : aucune ouverture ±30 min ; risque ÷2 avant week-end si < +1R ; flat/minimal 16-18 déc.

## Playbook de fin (pré-engagé, MàJ règle du 20 oct.)
- 18 déc. 16 h : flat forcé (règle) ; mes TP/expiritions de déc. ≤ 18 déc. 15 h.
- 10 déc. : point de contrôle. Avance >5 % → risque total ≤2 % dès le 16 déc. ; retard ≤3 % → plein régime 15 % sur meilleurs setups 7-16 déc. ; retard >3 % → idem + volatilité FOMC 9 déc. acceptée, jamais au-delà des plafonds ni sous 780 $ de capital-si-SL.

## Carry overlay (thèse ∩ portage)
Candidats : XAUUSD short (+36,7), USOUSD long (+17,23), USDJPY long (+6,56), USDCHF long (+5,84), USDCAD long (+3,14), BTC short (0). Jamais : GBPUSD, NAS100 long, BTC long, USOUSD short.
