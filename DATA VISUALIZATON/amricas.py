import pygal

wm = pygal.maps.world.World()
wm.title = 'North, Central, and South Amrica'

wm.add('North Amrica', ['ca', 'mx', 'us'])
wm.add('Central Amrica', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South Amrica', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('amricas.svg')