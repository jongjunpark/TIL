a = "ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
list_a = list(a)

result_a = list(map(lambda x: x.count("A"), list_a))
result_b = list(map(lambda x: x.count("B"), list_a))
result_c = list(map(lambda x: x.count("C"), list_a))
result_d = list(map(lambda x: x.count("D"), list_a))

A = result_a.count(1) * 4
B = result_b.count(1) * 3
C = result_c.count(1) * 2
D = result_d.count(1)

summary = A + B + C + D
print(summary)