import json
import hashlib
from enum import Enum
from pydantic import BaseModel, validator
from typing import List, Optional
from speckle.resources.objects import SpeckleObject
from speckle.base.resource import ResourceBaseSchema


class SpeckleObjectBase(ResourceBaseSchema):
    type: Optional[str]
    name: Optional[str]
    geometryHash: Optional[str]  # Is immediately replaced anyways
    hash: Optional[str]  # Is immediately replaced anyways
    applicationId: Optional[str]
    properties: dict = {}
    partOf: Optional[List[str]]
    parent: Optional[List[str]]
    children: Optional[List[str]]
    ancestors: Optional[List[str]]

    def dict(self):
        json_string = json.dumps(
            super(SpeckleObjectBase, self).dict()['properties'])

        self.geometryHash = hashlib.md5(
            json_string.encode('utf-8')).hexdigest()

        self.hash = hashlib.md5('{}.{}'.format(
            self.type, json_string).encode('utf-8')).hexdigest()

        return super(SpeckleObjectBase, self).dict()
