
with open('/Users/cturner/workspace/advent-of-code-23/05/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [int(x) for x in lines[0][7:].split(' ')]
seed_to_soil_i = lines.index('seed-to-soil map:')
soil_to_fertilizer_i = lines.index('soil-to-fertilizer map:')
fertilizer_to_water_i = lines.index('fertilizer-to-water map:')
water_to_light_i = lines.index('water-to-light map:')
light_to_temperature_i = lines.index('light-to-temperature map:')
temperature_to_humidity_i = lines.index('temperature-to-humidity map:')
humidity_to_location_i = lines.index('humidity-to-location map:')

def get_mapping(min_i, max_i):
    return [[int(x) for x in y.split(' ')] for y in lines[min_i:max_i]]

seed_to_soil = get_mapping(seed_to_soil_i+1,soil_to_fertilizer_i-1)
soil_to_fertilizer = get_mapping(soil_to_fertilizer_i+1, fertilizer_to_water_i-1 )
fertilizer_to_water = get_mapping(fertilizer_to_water_i+1, water_to_light_i-1)
water_to_light = get_mapping(water_to_light_i+1, light_to_temperature_i-1)
light_to_temperature = get_mapping(light_to_temperature_i+1,temperature_to_humidity_i-1)
temperature_to_humidity = get_mapping(temperature_to_humidity_i+1,humidity_to_location_i-1)
humidity_to_location = get_mapping(humidity_to_location_i+1,len(lines))

steps = [seed_to_soil,
        soil_to_fertilizer,
        fertilizer_to_water,
        water_to_light,
        light_to_temperature,
        temperature_to_humidity,
        humidity_to_location]

def find_min_location(seeds):
    min_location = None
    count = 0
    for seed in seeds:
        current = seed
        for step in steps:
            for [dest_start, source_start, range_] in step:
                offset = (current - source_start)
                if offset >= 0 and offset < range_:
                    current = dest_start + offset
                    break
        if min_location is None:
            min_location = current
        elif min_location > current:
            min_location = current
        count+= 1

        if count % 10000 == 0:
            print(f'{count/len(seeds)*100}')

    print(f'min_location: {min_location}')

def find_seed_from_location(seeds):
    found = False
    location = 0
    while not found:
        if (location % 100 == 0):
            print(f'l: {location}')
        current = location
        for step in reversed(steps):
            for [dest_start, source_start, range_] in step:
                offset = (current - dest_start)
                if offset >= 0 and offset < range_:
                    current = source_start + offset
                    break
        for i in range(0, len(seeds), 2):
            if current >= seeds[i] and current <seeds[i]+seeds[i+1]:
                found = True
                print(f'found! {location}')
        location += 1

# Part 1
# find_min_location(seeds)

# Part 2
find_seed_from_location(seeds)

