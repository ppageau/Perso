#!/usr/bin/env python3
"""Calculatrice de dimensionnement Arena_IA.
Usage: python3 size.py SYMBOLE side equity_usd risk_usd entry sl tp [nights]
Ex.:   python3 size.py XAUUSD-STD sell 1000 40 4195 4235 4070 8
Sortie: volume, risque réel, R:R, notionnel, levier, swap/nuit (CAD), check TP>=10x swap, conformité.
"""
import sys

# valeur P&L USD par lot par unité de prix ; unit = $1 or, pétrole, btc, action ; 1 pt indices ; 1 pip FX (0.0001 ou 0.01 jpy)
SYM = {
    # sym: (valeur_usd_par_lot_par_unit, unit_desc, lot_min, pas, swap_cad_lot_nuit_long, short, note_unit)
    "XAUUSD-STD": (100.0, "$1", 0.01, 0.01, -77.44, 36.7, "par $1"),
    "USOUSD-STD": (1000.0, "$1", 0.01, 0.01, 17.23, -56.27, "par $1"),
    "CL-OIL-STD": (1000.0, "$1", 0.01, 0.01, 0.0, 0.0, "par $1"),
    "SP500": (1.0, "pt", 0.1, 0.1, -1.65, 0.32, "par point"),
    "NAS100": (1.0, "pt", 0.1, 0.1, -6.37, 1.24, "par point (cash; ft.=0 obs.)"),
    "BTCUSD": (1.0, "$1", 0.01, 0.01, -20.0, 0.0, "par $1"),
    "EURUSD-STD": (10.0, "pip", 0.01, 0.01, -6.17, 1.72, "par pip"),
    "USDJPY-STD": (6.3, "pip", 0.01, 0.01, 6.56, -21.34, "par pip (~158)"),
    "NVDA.24H": (1.0, "$1", 0.1, 0.1, -7.41, 1.09, "par $1 (1 lot=1 action)"),
}
LIMITES = dict(risk_trade=0.05, risk_total=0.10, levier=10.0, rr_min=3.0)

def main():
    sym, side, eq, risk_usd, entry, sl, tp = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])
    nights = float(sys.argv[8]) if len(sys.argv) > 8 else 5.0
    v_unit, unit, lmin, pas, sw_l, sw_s, note = SYM[sym]
    stop = abs(entry - sl); gain = abs(tp - entry)
    # volume pour risk_usd
    vol = risk_usd / (stop * v_unit)
    vol = max(lmin, round(round(vol / pas) * pas, 4))
    risque = vol * stop * v_unit; reward = vol * gain * v_unit; rr = gain / stop
    sw_lot = sw_s if side == "sell" else sw_l
    sw_nuit = sw_lot * vol  # CAD
    sw_total = sw_nuit * nights
    tp_cad = reward * 1.40
    ok = []
    ok.append(("risque<=5%", risque <= eq * LIMITES["risk_trade"]))
    ok.append(("R:R>=3", rr >= LIMITES["rr_min"]))
    ok.append(("TP>=10x swap" if sw_total < 0 else "swap positif", tp_cad >= 10 * abs(sw_total) if sw_total < 0 else True))
    print(f"{sym} {side} vol={vol} ({unit} {note}) stop={stop} gain={gain}")
    print(f"  risque={risque:.2f}$ ({risque/eq*100:.2f}%)  reward={reward:.2f}$  R:R={rr:.2f}")
    print(f"  swap/nuit={sw_nuit:+.3f} CAD  sur {nights:.0f} nuits={sw_total:+.2f} CAD  TP={tp_cad:.1f} CAD")
    for label, good in ok: print(f"  [{'OK' if good else 'VIOLATION'}] {label}")

if __name__ == "__main__":
    main()
