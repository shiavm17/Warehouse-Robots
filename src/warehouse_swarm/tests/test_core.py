import pytest

from warehouse_swarm import Robot, SwarmController, create_square_formation


def test_robot_creation():
    robot = Robot(robot_id='robot_1', x=1.0, y=2.0)
    assert robot.robot_id == 'robot_1'
    assert robot.as_tuple() == (1.0, 2.0)
    assert robot.active


def test_swarm_centroid():
    robots = [
        Robot(robot_id='robot_1', x=0.0, y=0.0),
        Robot(robot_id='robot_2', x=2.0, y=2.0),
    ]
    swarm = SwarmController(robots=robots)
    assert swarm.formation_centroid() == (1.0, 1.0)


def test_move_robot():
    swarm = SwarmController(robots=[Robot(robot_id='robot_1', x=0.0, y=0.0)])
    swarm.move_robot('robot_1', 3.0, 4.0)
    assert swarm.robots[0].as_tuple() == (3.0, 4.0)


def test_create_square_formation():
    robots = create_square_formation(grid_size=2, spacing=1.5)
    assert len(robots) == 4
    assert robots[0].robot_id == 'robot_1'
    assert robots[3].as_tuple() == (1.5, 1.5)
