import xml.etree.ElementTree as ET
import networkx as nx

try:
    import cPickle as pickle  # Für Python 2
except ImportError:
    import pickle

def read_osm_file(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return root

def create_graph_from_osm(osm_data):
    G = nx.DiGraph()

    # Iteriere über Ways
    for way in osm_data.findall(".//way"):
        nodes = way.findall(".//nd")
        for i in range(len(nodes) - 1):
            source_node = nodes[i].attrib["ref"]
            target_node = nodes[i + 1].attrib["ref"]

            # Füge den Straßennamen als Attribut hinzu, wenn verfügbar
            road_name_tag = way.find(".//tag[@k='name']")
            road_name = road_name_tag.attrib["v"] if road_name_tag is not None else None

            G.add_edge(source_node, target_node, road_name=road_name)

    return G

def save_graph_to_file(graph, file_path):
    with open(file_path, "wb") as file:
        pickle.dump(graph, file, pickle.HIGHEST_PROTOCOL)

if __name__ == "__main__":
    osm_file_path = "muenster-map.osm"
    osm_data = read_osm_file(osm_file_path)
    graph = create_graph_from_osm(osm_data)

    save_graph_to_file(graph, "graph_structure.pkl")
    
    # Beispiel: Finde den kürzesten Weg zwischen zwei Knoten
    #start_node = "start_node_id"
    #end_node = "end_node_id"
    #shortest_path = nx.shortest_path(graph, source=start_node, target=end_node)
    
    #print("Shortest path:", shortest_path)

