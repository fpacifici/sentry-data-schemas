from importlib.resources import read_binary, path
from jsonschema_typed import JSONSchema

with path("schemas", "event.schema.json") as schema_path:
    EventData = JSONSchema["var:schemas:schema_path"]

