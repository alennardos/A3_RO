from pulp import *

AB = LpVariable("AB", 0, 1, const.LpBinary)
AC = LpVariable("AC", 0, 1, const.LpBinary)
AD = LpVariable("AD", 0, 1, const.LpBinary)
AE = LpVariable("AE", 0, 1, const.LpBinary)

BC = LpVariable("BC", 0, 1, const.LpBinary)
BD = LpVariable("BD", 0, 1, const.LpBinary)
BE = LpVariable("BE", 0, 1, const.LpBinary)

CD = LpVariable("CD", 0, 1, const.LpBinary)
CE = LpVariable("CE", 0, 1, const.LpBinary)

DE = LpVariable("DE", 0, 1, const.LpBinary)

# probleme
prob = LpProblem("choix", LpMinimize)

# objectif
prob += AB + AC + AD + AE == 2
prob += AB + BC + BD + BE == 2
prob += AC + BC + CD + CE == 2
prob += AE + BE + CE + DE == 2
prob += AD + BD + CD + DE == 2

# contrainte
prob += 10*AB + 2*AC + 3*AD + 4*AE + 1*BC + 5*BD + 30*BE + 5*CD + 8*CE + 9*DE

prob.solve()
print("a")
print(LpStatus[prob.status])
print("Min=", value(prob.objective))

# variables resultat
for v in prob.variables():
    print("%s=%.2f"%(v.name,v.varValue), end=', ')