import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

#Establish constants 
c = 0.01
k = 0.1
initial_concs = [0.1, 0.1, 0.1]

#Calculate concentrations

def get_concs(C, t):
    G, T, P = C
    dGdt = 0
    dTdt = c*G
    dPdt = k*T
    return [dGdt, dTdt, dPdt]

times = np.linspace(0., 100., 101)
ans = odeint(func=get_concs, y0=initial_concs, t=times)
Gs = ans[:, 0]
Ts = ans[:, 1]
Ps = ans[:, 2]


fig, ax = plt.subplots()
ax.plot(times, Gs, label='DNA')
ax.plot(times, Ts, label='RNA')
ax.plot(times, Ps, label='Protein')
ax.legend()
ax.set_xlabel('time, hrs')
ax.set_ylabel('Concentration, M')
plt.grid()
