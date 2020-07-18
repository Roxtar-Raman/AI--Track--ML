from scipy.optimize import linprog
obj=[-50,-120]
lhs_ieq = [[100,200],[10,30],[1,1]]
rhs_ieq = [[10000,1200,110]]
boundaries = [(0,float('inf')),(0,float('inf'))]
opt= linprog(c = obj, A_ub =lhs_ieq, b_ub=rhs_ieq,bounds=boundaries,method='Simplex')
opt
