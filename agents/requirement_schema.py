from pydantic import BaseModel
from typing import Optional


class SystemRequirements(BaseModel):

    throughput: Optional[str]
    carton_weight: Optional[str]
    pallet_type: Optional[str]
    robot_type: Optional[str]
    gripper_type: Optional[str]
    conveyor_speed: Optional[str]
    control_system: Optional[str]
    integration: Optional[str]
    power_requirement: Optional[str]