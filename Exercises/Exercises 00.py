import numpy as np

#Uppgift 1
a = 3
b = 4
hypothenuse = np.sqrt(a**2+b**2)

print (f"\nHypotinusan i triangeln {a} och {b}. Hypotinusan är: {hypothenuse}\n")

a = 5
c = 7
cathetus = np.sqrt(c**2-a**2)
print ("Uppgift 1")
print (f"Katen är: {cathetus:.1f}\n")


#Uppgift 2

days = 365
correct_predictions = 300

accuracy = correct_predictions / days * 100
print ("Uppgift 2")
print (f"Träffsäkerheten i denna algoritm är: {round(accuracy)}%\n")

#Uppgift 3

# Svar: Nej. För att fel förutsägelsen i FN är att faktiskt brinner, medans FP är det bara ett falskt larm

tp = 2
fp = 2
fn = 11
tn = 985

correct = (tp + tn) / (tp + fp + fn + tn)
print ("Uppgift 3")
print (f"Träffsäkerheten är för denna model är: {correct}\n")


#Uppgift 4

a = (4, 4)
b = (0, 1)

k = (a[1] - b[1]) / (a[0]-b[0])

m = int(a[1] - k*a[0])
print ("Uppgift 4")
print (f"Lutning på linjen är: {k} och den skär y-axeln: {m}")
print (f"Linjens eqution är: y = {k}*x + {m}\n")


#Uppgift 5
point_a = [3, 5]
point_b = [-2, 4]

a = point_a[0] - point_b[0]
b = point_a[1] - point_b[1]

length_between = np.sqrt(a**2+b**2)
print ("Uppgift 5")
print (f"Längden mellan dom två punkterna är: {length_between:.1f}\n")

#Uppgift 6
point_a = [2, 1, 4]
point_b = [3, 1, 0]

length_between = np.sqrt(np.power((point_a[0] - point_b[0]), 2) + np.power((point_a[1] - point_b[1]), 2) + np.power((point_a[2] - point_b[2]),2))

print ("Uppgift 6")
print (f"Längden mellan punkterna är: {length_between:.2f}\n")

