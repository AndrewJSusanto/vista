import vista
trace_path = ["/mnt/c/Users/suzan/pacman/pacman-team/vista/vista/resources/vista_traces/20210726-184624_lexus_devens_center/"]
world = vista.World(trace_path,
                    trace_config={'road_width': 4})
car = world.spawn_agent(config={'length': 5.,
                                'width': 2.,
                                'wheel_base': 2.78,
                                'steering_ratio': 14.7,
                                'lookahead_road': True})
display = vista.Display(world)