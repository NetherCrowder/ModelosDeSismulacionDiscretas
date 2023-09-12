R = [0.21, 0.92, 0.25, 0.82, 0.45, 0.31, 0.72, 0.81, 0.45, 0.87]
Pacientes = [4, 6, 8, 10]
Dias = [5, 7, 5, 3]
Suma = float(0)
Px = []
Fx = []
X = []

for I in range(len(Dias)):
    Suma += Dias[I]

for J in range(len(Dias)):
    Px.append((Dias[J]/Suma))

Suma = 0
for K in range(len(Px)):
    Suma += Px[K]
    Fx.append(Suma)

for L in range(len(R)):
    if(R[L] <= Fx[0]):
        X.append(Pacientes[0])
    elif(R[L] <= Fx[1]):
        X.append(Pacientes[1])
    elif(R[L] <= Fx[2]):
        X.append(Pacientes[2])
    else:
        X.append(Pacientes[3])

print("Punto A. La función de masa es:", Px)
print("Punto B. La función de districubión es:", Fx)
print("Punto C. El generador es:",
      "\n \t Si 0 <= R <=",Fx[0],"X = ",Pacientes[0],
      "\n \t Si",Fx[0],"<= R <=",Fx[1],"X = ",Pacientes[1],
      "\n \t Si",Fx[1],"<= R <=",Fx[2],"X = ",Pacientes[2],
      "\n \t Si",Fx[2],"<= R <=",Fx[3],"X = ",Pacientes[3])
print("Punto D. Los valores generados de los 20 Dias:", X)

