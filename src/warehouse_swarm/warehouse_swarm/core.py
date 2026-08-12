from dataclasses import dataclass
from typing import List, Optional, Tuple


@dataclass
class Robot:
    """A warehouse robot with an identifier, position and active state."""
    robot_id: str
    x: float
    y: float
    active: bool = True

    def as_tuple(self) -> Tuple[float, float]:
        return self.x, self.y


class SwarmController:
    """Manage a collection of warehouse robots."""

    def __init__(self, robots: Optional[List[Robot]] = None) -> None:
        self.robots: List[Robot] = robots or []

    def add_robot(self, robot: Robot) -> None:
        if any(existing.robot_id == robot.robot_id for existing in self.robots):
            raise ValueError(f'Robot with id {robot.robot_id} already exists')
        self.robots.append(robot)

    def move_robot(self, robot_id: str, x: float, y: float) -> None:
        robot = self._find_robot(robot_id)
        if robot is None:
            raise ValueError(f'No robot found with id {robot_id}')
        robot.x = x
        robot.y = y

    def _find_robot(self, robot_id: str) -> Optional[Robot]:
        return next((robot for robot in self.robots if robot.robot_id == robot_id), None)

    def active_robots(self) -> List[Robot]:
        return [robot for robot in self.robots if robot.active]

    def formation_centroid(self) -> Tuple[float, float]:
        active = self.active_robots() or self.robots
        if not active:
            return 0.0, 0.0
        x_sum = sum(robot.x for robot in active)
        y_sum = sum(robot.y for robot in active)
        count = len(active)
        return x_sum / count, y_sum / count

    def report(self) -> List[str]:
        return [f'{robot.robot_id}: ({robot.x:.2f}, {robot.y:.2f}) active={robot.active}' for robot in self.robots]


def create_square_formation(grid_size: int = 3, spacing: float = 1.0) -> List[Robot]:
    """Create a square grid formation of robots."""
    if grid_size < 1:
        raise ValueError('grid_size must be at least 1')
    robots: List[Robot] = []
    index = 1
    for row in range(grid_size):
        for column in range(grid_size):
            robots.append(Robot(
                robot_id=f'robot_{index}',
                x=column * spacing,
                y=row * spacing,
            ))
            index += 1
    return robots
