from pyvis.network import Network
import webbrowser

net = Network(height="1500px", width="100%", bgcolor="#b3b3cc", font_color="white")


# Adding character family nodes
stark_nodes = [
    (1, "Ned Stark", "House Stark", 35),
    (2, "Catelyn Stark", "House Stark", 35),
    (3, "Robb Stark", "House Stark", 30),
    (4, "Sansa Stark", "House Stark", 25),
    (5, "Arya Stark", "House Stark", 25),
    (6, "Bran Stark", "House Stark", 25),
    (7, "Rickon Stark", "House Stark", 25)
]

lannister_nodes = [
    (8, "Jaime Lannister", "House Lannister", 35),
    (9, "Cersei Lannister", "House Lannister", 35),
    (10, "Tyrion Lannister", "House Lannister", 35)
]

robert_node = (11, "Robert Baratheon", "House Baratheon", 35)
shared_children_nodes = [
    (12, "Joffrey Baratheon", "House Baratheon", 25),
    (13, "Myrcella Baratheon", "House Baratheon", 25),
    (14, "Tommen Baratheon", "House Baratheon", 25)
]

# Jon Snow, separate from Stark family
jon_snow_node = (15, "Jon Snow", "The Night's Watch", 30)


# Add Stark, Lannister, Robert Baratheon, shared children, and Jon Snow nodes
for node_id, label, title, size in stark_nodes + lannister_nodes + [robert_node] + shared_children_nodes + [jon_snow_node]:
    if title == "House Stark" or label == "Jon Snow":
        color = "#708090"  # Light blue for Starks
    elif title == "House Lannister":
        color = "#FFD700"  # Gold for Lannisters
    elif title == "House Baratheon":
        color = "green"  # Green for Baratheons
    net.add_node(node_id, label=label, title=title, size=size, color=color)

# Connect families
for i, stark in enumerate(stark_nodes[:-1]):
    for next_stark in stark_nodes[i+1:]:
        net.add_edge(stark[0], next_stark[0])

for i, lannister in enumerate(lannister_nodes[:-1]):
    for next_lannister in lannister_nodes[i+1:]:
        net.add_edge(lannister[0], next_lannister[0])

# Connect Robert Baratheon to Ned Stark, Cersei Lannister, and shared children
net.add_edge(robert_node[0], 1)  
net.add_edge(robert_node[0], 9)  
for child in shared_children_nodes:
    net.add_edge(robert_node[0], child[0])
    net.add_edge(9, child[0])  

# Connect Jon Snow to Ned Stark only
net.add_edge(1, jon_snow_node[0])  


filename = "network_visualization.html"
net.save_graph(filename)

# Open the saved HTML file in the default web browser
webbrowser.open(filename, new=2)

