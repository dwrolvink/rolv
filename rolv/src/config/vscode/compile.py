import json, sys

# arguments
if len(sys.argv) != 2:
    print("Usage: python compile.py <deployment>")
    exit(1)

deployment = sys.argv[1]
valid_deployments = ["home", "work"]
if deployment not in valid_deployments:
    print(f'Error: deployment not valid. Valid deployments: {valid_deployments}')
    exit(1)

# input
if deployment == "home":
    negative_keybindings_file = "/home/dorus/git/rolv/rolv/src/config/vscode/keybindings.linux.negative.json"
    keybindings_file = "/home/dorus/git/rolv/rolv/src/config/vscode/keybindings.json"
    extra_keybindings_file = "/home/dorus/.config/rolv/vscode/keybindings.json"
    keybindings_output_file = "/home/dorus/.config/Code - Insiders/User/keybindings.json"
else:
    negative_keybindings_file = "/u/rolvinkd/git/rolv/rolv/src/config/vscode/keybindings.windows.negative.json"
    keybindings_file = "/u/rolvinkd/git/rolv/rolv/src/config/vscode/keybindings.json"
    extra_keybindings_file = "/u/rolvinkd/.config/rolv/vscode/keybindings.json"
    keybindings_output_file = "/tmp/keybindings.json"


# get input
with open(negative_keybindings_file, 'r') as f:
    negative_keybindings = json.loads(f.read())

with open(keybindings_file, 'r') as f:
    added_keybindings = json.loads(f.read())

with open(extra_keybindings_file, 'r') as f:
    extra_keybindings = json.loads(f.read())

# merge
keybindings = negative_keybindings

for group in added_keybindings.keys():
    keybindings += added_keybindings[group]["bindings"]

keybindings += extra_keybindings

# remove description, as this is not native
for keybinding in keybindings:
    if "description" in keybinding.keys():
        del(keybinding["description"])

# output
with open(keybindings_output_file, "w") as f:
    f.write(json.dumps(keybindings, indent=2))

if deployment == "work":
    print(f'Wrote compiled keybindings to {keybindings_output_file} copy them manually to the keybindings file!')