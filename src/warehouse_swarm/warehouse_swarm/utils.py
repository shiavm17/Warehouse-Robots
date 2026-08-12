from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .core import Robot


def validate_robot_id(robot_id: str) -> bool:
    """Validate that a robot identifier is a non-empty string."""
    return bool(robot_id and robot_id.strip())


def format_robot_status(robot: 'Robot') -> str:
    """Return a formatted status string for a robot."""
    status = 'active' if robot.active else 'inactive'
    return f'Robot {robot.robot_id}: position=({robot.x:.2f}, {robot.y:.2f}), status={status}'
