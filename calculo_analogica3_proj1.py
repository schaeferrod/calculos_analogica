#Rodrigo Schaefer da Silva
#Victor Hugo Dantas Nery
#Eetrônica analógica 3
#Cálculos de polarização direta de transistor
#Configuração divisor de tensão
#Cálculos de capacitores
#Especificações de projeto:
#Ganho = 10; fl = 100 Hz; fh = 1 MHz

#Análise reta de carga
Ic = 40*10**-3
Ib = 150*10**-6
Vcc = 14
Vce = 7
Vbe = 0.7
hfe = 266

#Define R1 e R2
R1 = 10*10**3
R2 = 4*10**3

#Cálculo Rth
Rth = (R1*R2)/(R1+R2)
#Cálculo Eth
Eth = (R2*Vcc)/(R1+R2)
#Cálculo de Re
Re = (Eth-Vbe-Ib*Rth)/(Ib*hfe)
#Cálculo de Rc
Rc = (Vcc-Vce-Ic*Re)/Ic

#print dos resultados da análise DC
print(f"R1 = {R1}")
print(f"R2 = {R2}")
print(f"Rth = {Rth}")
print(f"Eth = {Eth}")
print(f"Re = {Re}")
print(f"Rc = {Rc}")

#Cálculo do ganho
Av = 10

hie = 8700
hoe = 70*10**-6
Rs = 50
pi = 3.141592654
f = 100
f1 = 0.1*f #Adotando Cs como capacitor de corte, os outros dois tem sua frequência reduzida em 10%:


Rl = (Av*hie*Rc)/(-Av*hie-hfe*Rc)

if Rl<0:
    Rl = Rl-2*Rl #Transforma o Rl no seu módulo, caso seja menor que zero

print(f"Rl = {Rl}")

#Cálculo dos capacitores



Cs = 1/(2*pi*f*(Rs+((R1*R2*hie)/(R2*hie+R1*hie+R1*R2))))

fator1_Co = (Rc*Rl)/(Rc+Rl)
fator2_Co = fator1_Co/(1+hoe*fator1_Co)
Co = 1/(2*pi*f1*fator2_Co)

Req1_Ce = ((Rs*R1*R2)/(R1*R2+Rs*R2+Rs*R1))
fator1_Ce = (Req1_Ce+hie)/(1+hfe)
fator2_Ce = (Re*fator1_Ce)/(Re+fator1_Ce)
Ce = 1/(2*pi*f1*fator2_Ce)

print(f"Cs = {Cs}")
print(f"Co = {Co}")
print(f"Ce = {Ce}")

#Cálculo altas frequências
Cbc = 1.5*10**-12
gm = hfe/hie
RlinhaL = (Rc*Rl)/(Rc+Rl)
Cm = Cbc*(1+(gm*RlinhaL))

print(f"Cm = {Cm}")

Cblinhae = 3.5*10**-12
rbblinha = 50
rblinhae = hie
Rb = (R1*R2)/(R1+R2)
Rblinhae = ((rblinhae*(Rb+rbblinha))/(rblinhae+Rb+rbblinha))

print(f"Rblinhae = {Rblinhae}")

fH = 1/(2*pi*Rblinhae*(Cblinhae+Cm))

print(f"fH = {fH}")

#Cálculo capacitor de corte superior

fHf = 1*10**6
Rll = 20

#Cf = Cl
Cl = 1/(2*pi*fHf*Rll)

print(f"Cl = {Cl}")







