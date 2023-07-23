from dataclasses_serialization.bson import BSONSerializer


def serialize_dataclass(obj):
    """
    Serializes a dataclass object into BSON (Binary JSON) format.

    Args:
        obj (dataclass): Dataclass object to be serialized.

    Returns:
        bytes: BSON serialized representation of the dataclass object.
    """
    return BSONSerializer.serialize(obj)
