import json

from base_ontology.node import BaseNode
from base_ontology.relation import BaseRelation


def save_nodes(
    node_dict: dict[str, tuple[BaseNode, bool, str]],
    output_file_name: str = "saved_dict/NODE_DICT.json",
) -> None:
    """
    Save the JSON schemas of dynamically created Pydantic models to a JSON file.
    Each schema includes additional metadata such as multiplicity and description.

    Args:
        node_dict (dict): A dictionary where keys are model names and values are tuples containing:
            - model_class (BaseNode): The Pydantic model class.
            - multiplicity (bool): Indicates if multiple instances of the model are allowed.
            - description (str): A brief description of the model.
        output_file_name (str): The name of the output JSON file (default is "node.json").
    """
    schemas = {}

    for key, (node_class, multiplicity, description) in node_dict.items():
        # Get the model's JSON schema
        schema = node_class.model_json_schema()
        # Add multiplicity information
        schemas[key] = {"schema": schema, "multiplicity": multiplicity, "description": description}

    # Write the schemas to the JSON file
    with open(output_file_name, "w", encoding="utf-8") as f:
        json.dump(schemas, f, indent=2, ensure_ascii=False)

    print(f"Saved schemas for {len(node_dict)} models to {output_file_name}")


def save_relations(relation_dict: dict[str, BaseRelation], output_file_name: str = "saved_dict/RELATION_DICT.json") -> None:
    """
    Save the JSON schemas of dynamically created Pydantic models to a JSON file.
    Each schema includes additional metadata such as multiplicity and description.

    Args:
        node_dict (dict): A dictionary where keys are model names and values are tuples containing:
            - model_class (BaseNode): The Pydantic model class.
            - multiplicity (bool): Indicates if multiple instances of the model are allowed.
            - description (str): A brief description of the model.
        output_file_name (str): The name of the output JSON file (default is "output.json").
    """
    schemas = {}

    for key, relation_class in relation_dict.items():
        # Get the model's JSON schema
        schema = relation_class.model_json_schema()
        # Add multiplicity information
        schemas[key] = {"schema": schema}
    print(schemas)

    # Write the schemas to the JSON file
    with open(output_file_name, "w", encoding="utf-8") as f:
        json.dump(schemas, f, indent=2, ensure_ascii=False)

    print(f"Saved schemas for {len(relation_dict)} models to {output_file_name}")
