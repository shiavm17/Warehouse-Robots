# Warehouse Workspace

This workspace contains ROS 2 packages for warehouse robotics and swarm control.

## Structure

- `src/warehouse_nav/` - navigation package
- `src/warehouse_robot_description/` - robot URDF descriptions
- `src/warehouse_simulation/` - simulation support
- `src/warehouse_swarm/` - warehouse swarm Python package

## Warehouse Swarm Package

The `warehouse_swarm` package provides a simple swarm controller and utility functions.

### Example image usage

Add images to the `images/` folder and reference them in `README.md` like this:

```markdown
![Warehouse Swarm Diagram](images/warehouse_swarm_diagram.png)
```

## Build and Test

From the workspace root:

```bash
colcon build
colcon test
```

## Notes

- Place images in `images/`
- Use `README.md` example links when publishing to GitHub
