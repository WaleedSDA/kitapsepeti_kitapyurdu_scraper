from dataclasses_serialization.bson import BSONSerializer


def serialize_dataclass(obj):
    return BSONSerializer.serialize(obj)
