from simulation.simple_sim import Simulation
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from numpy import linspace, exp

def run_sim(sim):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x_theory = linspace(0, sim.fixing_constant, sim.fixing_constant)
    y_theory = [sim.fixing_constant*exp(-a/sim.temperature) for a in x_theory]


    def update(stuff):
        y = [a.money for a in sim.agents]
        ax.clear()
        ax.set_xlabel('money')
        ax.set_ylabel('frequency')
        ax.hist(y,bins=int(len(sim.agents)/50),range=(0,sim.fixing_constant),histtype='step')
        ax.plot(x_theory,y_theory)
        sim.update(100)
        #print(sim.temperature)

    a = anim.FuncAnimation(fig, update, frames=10000, repeat=False)
    plt.show()


sim = Simulation(1000, 50)
run_sim(sim)