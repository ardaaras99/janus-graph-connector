from pathlib import Path

from base_ontology.node import BaseNode
from base_ontology.relation import BaseRelation

from janus_graph_connector.graph_utils import JanusGraphClient
from janus_graph_connector.utils import save_nodes, save_relations

# 0. Save pydantic object as JSON
NODE_DICT: dict[str, tuple[type[BaseNode], bool, str]] = {}
RELATION_DICT: dict[str, type[BaseRelation]] = {}

ontology_name: str = ""
version: str = ""
node_path: str = ""
relation_path: str = ""
save_nodes(NODE_DICT, node_path)
save_relations(RELATION_DICT, relation_path)

# 1. Write v0 version by reading JSON files (simulating JSON file reading)
testClient = JanusGraphClient()
testClient.cleanup_graph(ontology_name=ontology_name, version=version)
testClient.write_nodes(json_file_path=Path(node_path), ontology_name=ontology_name, version=version)
testClient.write_relations(json_file_path=Path(relation_path), ontology_name=ontology_name, version=version)

# 2. Finally read the graph
READED_NODE_DICT = testClient.read_nodes(ontology_name=ontology_name, version=version)
READED_RELATION_DICT = testClient.read_relations(ontology_name=ontology_name, version=version, node_dict=NODE_DICT)
