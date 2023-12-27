import math


def generate_wave_pattern(width, height):
    art = []
    for i in range(height):
        line = ''
        for j in range(width):
            # Using sine wave formula for the pattern
            wave = int(10 * math.sin(j / 3.0) + 10)
            if wave == i:
                line += '*'
            else:
                line += ' '
        art.append(line)
    return '\n'.join(art)


# Define the size of the wave pattern
width, height = 60, 20
print(generate_wave_pattern(width, height))
