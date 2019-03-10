import csv

a = ["トップガン", "危険なビジネス", "少数の研究"]
b = ["タイタニック", "ザ・レベナント", "インセプション"]
c = ["トレーニングデイ", "マンオンファイヤ", "フライト"]

with open("st2.csv", "w", encoding="shift_jis", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(a)
    w.writerow(b)
    w.writerow(c)
