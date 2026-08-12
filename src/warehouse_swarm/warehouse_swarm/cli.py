import argparse

from .core import create_square_formation, SwarmController
from .utils import format_robot_status


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog='warehouse_swarm',
        description='Warehouse swarm control and simulation helper.'
    )
    parser.add_argument(
        '--size',
        type=int,
        default=3,
        help='Grid size for the swarm formation.',
    )
    parser.add_argument(
        '--spacing',
        type=float,
        default=1.0,
        help='Distance between robots in the formation.',
    )
    args = parser.parse_args(argv)

    robots = create_square_formation(grid_size=args.size, spacing=args.spacing)
    swarm = SwarmController(robots=robots)

    print(f'Simulating {len(swarm.robots)} robots in a {args.size}x{args.size} swarm formation:')
    for robot in swarm.robots:
        print(format_robot_status(robot))

    centroid = swarm.formation_centroid()
    print(f'Formation centroid: ({centroid[0]:.2f}, {centroid[1]:.2f})')
    return 0
