

def relative_pressure(absolute_pressure, temperature, height):
    h = 8000 * (1 + 0.004 * temperature) / absolute_pressure
    p = absolute_pressure + height / h
    p_mean = (absolute_pressure + p) / 2
    t = temperature + (0.6 * height) / 100
    t_mean = (temperature + t) / 2

    h = 8000 * (1 + 0.004 * t_mean) / p_mean
    return absolute_pressure +  height / h

