from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(''))

template = env.get_template('ltl_temp.tl')


layer_loc = {0:['A'], 1:['B'], 2:['C','D'], 3:['E']}

rlayers = ['First', 'Second', 'Third', 'Forth']

n_layers = 4
n_locations = 5
n_uavs = 4
locations = []
points = [chr(i + 97).upper() for i in range(n_locations)]
locations += ["None"]
layers = []
layers += "First"

tmpinput = {}

tmpinput["controller_name"] = "Controller_4"

for i in range(n_locations):
    locations += [' | ']
    locations += [points[i]]

for i in range(1,n_layers):
    layers += [' | ']
    layers += [rlayers[i]]

tmpinput["types"] = "enum Pos = {} \nenum Layer = {}".format("".join(locations),
                                                     ''.join(layers))
input_string = []
for i in range(n_uavs):
    for j in range(i,n_uavs):
        if i != j:
            input_string += ["input uav{}_{}_collide : Bool = \
 False\n".format(i,j)]

tmpinput["inputs"] = "".join(input_string)

output_string = []

for i in range(n_uavs):
    output_string += ["output uav{}_layer : Layer\n".format(i)]
    output_string += ["output uav{}_goto : Pos = None\n".format(i)]
    output_string += ["output uav{}_intent : Pos = None\n".format(i)]

tmpinput["outputs"] = "".join(output_string)

spec = '  !('
for i in range(n_uavs):
    for j in range(i, n_uavs):
        if i != j:
            spec += 'uav{}_{}_collide'.format(i,j)
            if i != n_uavs - 2 or j != n_uavs -1:
                spec += ' /\ '
            else:
                spec += ')'

tmpinput["env_trans"] = [spec]

specs = []
spec = ''
for i in range(n_uavs):
    for l in range(n_layers):
        lh = "  uav{}_layer == {} -> (".format(i, rlayers[l])
        rh = ""
        for j in range(len(layer_loc[l])):
            rh += 'uav{}_goto == {}'.format(i, layer_loc[l][j])
            if j == len(layer_loc[l]) - 1:
                rh += ' \/ uav{}_goto == None)'.format(i)
            else:
                rh += ' \/ '
        spec = lh + rh
        specs += [spec]

for i in range(n_uavs):
    for j in range(j,n_uavs):
        if i != j:
            spec = '  uav{i}_{j}_collide -> uav{i}_layer != uav{j}_layer'.format(i=i,j=j)
            specs += [spec]

for i in range(n_uavs):
    for j in range(n_locations):
        spec = "  uav{i}_goto' == {j} -> uav{i}_intent == {j}".format(i=i,
                                                                    j=points[j])
        specs += [spec]


sys_trans_strings = specs
tmpinput["sys_trans"] = sys_trans_strings

specs = []
for i in range(n_uavs):
    for j in range(n_locations):
        spec = "  uav{i}_goto' == {j}".format(i=i,j=points[j])
        specs += [spec]

sys_liveness_strings = specs
tmpinput["sys_liveness"] = sys_liveness_strings

with open("ctrl.salt",'w+') as f:
    f.write(template.render(**tmpinput))
