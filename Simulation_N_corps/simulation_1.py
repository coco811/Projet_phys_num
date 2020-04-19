import math
import random
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
class point:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

class body:
    def __init__(self, location, mass, velocity, name = ""):
        self.location = location
        self.mass = mass
        self.velocity = velocity
        self.name = name

def calculate_single_body_acceleration(bodies, body_index):
    G_const = 6.67408e-11 #m3 kg-1 s-2
    acceleration = point(0,0,0)
    target_body = bodies[body_index]
    for index, external_body in enumerate(bodies):
        if index != body_index:
            r = (target_body.location.x - external_body.location.x)**2 + (target_body.location.y - external_body.location.y)**2 + (target_body.location.z - external_body.location.z)**2
            r = math.sqrt(r)
            tmp = G_const * external_body.mass / r**3
            acceleration.x += tmp * (external_body.location.x - target_body.location.x)
            acceleration.y += tmp * (external_body.location.y - target_body.location.y)
            acceleration.z += tmp * (external_body.location.z - target_body.location.z)

    return acceleration

def compute_velocity(bodies, time_step = 1):
    for body_index, target_body in enumerate(bodies):
        acceleration = calculate_single_body_acceleration(bodies, body_index)
        target_body.velocity.x += acceleration.x * time_step
        target_body.velocity.y += acceleration.y * time_step
        target_body.velocity.z += acceleration.z * time_step

def update_location(bodies, time_step = 1):
    for target_body in bodies:
        target_body.location.x += target_body.velocity.x * time_step
        target_body.location.y += target_body.velocity.y * time_step
        target_body.location.z += target_body.velocity.z * time_step

def compute_gravity_step(bodies, time_step = 1):
    compute_velocity(bodies, time_step = time_step)
    update_location(bodies, time_step = time_step)


def run_simulation(bodies, names=None, time_step=1, number_of_steps=10000, report_freq=100):
    # create output container for each body
    body_locations_hist = []
    for current_body in bodies:
        body_locations_hist.append({"x": [], "y": [], "z": [], "name": current_body.name})

    for i in range(1, number_of_steps):
        compute_gravity_step(bodies, time_step=1000)

        if i % report_freq == 0:
            for index, body_location in enumerate(body_locations_hist):
                body_location["x"].append(bodies[index].location.x)
                body_location["y"].append(bodies[index].location.y)
                body_location["z"].append(bodies[index].location.z)
    print(body_locations_hist)
    return body_locations_hist


def plot_output(bodies, outfile=None):
    fig = plot.figure()
    colours = ['r', 'b', 'g', 'y', 'm', 'c']
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0
    for current_body in bodies:
        max_dim = max(max(current_body["x"]), max(current_body["y"]), max(current_body["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(current_body["x"], current_body["y"], current_body["z"], c=random.choice(colours),
                label=current_body["name"])

    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend()

    if outfile:
        plot.savefig(outfile)
    else:
        plot.show()


def animation3d(bodies, titre):

    fig = plot.figure()
    colours = ['r', 'b', 'g', 'y', 'm', 'c']
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0
    for current_body in bodies:
        max_dim = max(max(current_body["x"]), max(current_body["y"]), max(current_body["z"]))
        if max_dim > max_range:
            max_range = max_dim
    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])

    lines = [ax.plot([], [], [])[0] for _ in range(bodies)]
    planete = [ax.plot([], [],[],marker='o')[0] for _ in range(bodies)]

    def animate(i):
        for j in range(bodies):
            lines[j].set_data(bodies[j]['x'][:i+1], bodies[j]['y'][:i+1])
            lines[j].set_3d_properties(bodies[j]['z'][:i+1])
            planete[j].set_data(bodies[j]['x'][:i], bodies[j]['y'][:i])
            planete[j].set_3d_properties(bodies[j]['z'][:i + 1])
        return lines,planete


    anim = animation.FuncAnimation(fig, animate, interval=2, repeat=False)
    fig.title(titre)
    fig.xlabel('position en x')
    fig.ylabel('position en y')
    fig.legend()
    fig.show()