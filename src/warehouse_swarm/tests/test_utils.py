from warehouse_swarm import Robot
from warehouse_swarm.utils import format_robot_status, validate_robot_id


def test_validate_robot_id():
    assert validate_robot_id('robot_1')
    assert not validate_robot_id('')
    assert not validate_robot_id('   ')


def test_format_robot_status():
    robot = Robot(robot_id='robot_1', x=1.25, y=2.75, active=False)
    assert format_robot_status(robot) == 'Robot robot_1: position=(1.25, 2.75), status=inactive'
