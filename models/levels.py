import random

class Dungeon:
    def __init__(self):
        self.level = 1
        self.map, self.start_pos = self.generate_map()
        self.next_map, self.next_start_pos = self.generate_map()
        self.current_floor = 1

    def generate_map(self):
        map_width, map_height = 200, 180
        dungeon_map = [['#' for _ in range(map_width)] for _ in range(map_height)]
        rooms = []

        # 部屋の生成
        for _ in range(10):
            room_size = random.choice(['small', 'medium', 'large'])
            x, y = random.randint(1, map_width - 20), random.randint(1, map_height - 15)
            room = self.create_room(dungeon_map, x, y, room_size)
            if room:
                rooms.append(room)

        # 通路の生成
        for i in range(len(rooms) - 1):
            self.connect_rooms(dungeon_map, rooms[i], rooms[i + 1])

        # 階段の生成
        stairs_room = random.choice(rooms)
        self.create_stairs(dungeon_map, stairs_room)

        # Player spawn point
        start_room = random.choice(rooms)
        start_pos = (start_room['x'] + start_room['width'] // 2, start_room['y'] + start_room['height'] // 2)

        return dungeon_map, start_pos

    def create_room(self, dungeon_map, x, y, size):
        # width, height = {'small': (5, 4), 'medium': (10, 8), 'large': (15, 12)}[size]
        # for i in range(y, min(y + height, len(dungeon_map))):
        #     for j in range(x, min(x + width, len(dungeon_map[0]))):
        #         dungeon_map[i][j] = '.'
        width, height = {'small': (5, 4), 'medium': (10, 8), 'large': (15, 12)}[size]
        # 部屋がマップの外に出ないか確認
        if x + width >= len(dungeon_map[0]) or y + height >= len(dungeon_map):
            return None

        for i in range(y, y + height):
            for j in range(x, x + width):
                dungeon_map[i][j] = '.'

        return {'x': x, 'y': y, 'width': width, 'height': height}

    def connect_rooms(self, dungeon_map, room1, room2):
        x1, y1 = room1['x'] + room1['width'] // 2, room1['y'] + room1['height'] // 2
        x2, y2 = room2['x'] + room2['width'] // 2, room2['y'] + room2['height'] // 2

        # 水平通路
        for x in range(min(x1, x2), max(x1, x2) + 1):
            dungeon_map[y1][x] = '.'

        # 垂直通路
        for y in range(min(y1, y2), max(y1, y2) + 1):
            dungeon_map[y][x2] = '.'

    def create_stairs(self, dungeon_map, room):
        # stairs_x, stairs_y = random.randint(1, len(dungeon_map[0]) - 2), random.randint(1, len(dungeon_map) - 2)
        # dungeon_map[stairs_y][stairs_x] = '>'
        stairs_x, stairs_y = room['x'] + room['width'] // 2, room['y'] + room['height'] // 2
        dungeon_map[stairs_y][stairs_x] = '>'

    def next_level(self):
        self.level += 1
        self.current_floor += 1
        self.map = self.generate_map()
        self.map, self.start_pos = self.next_map, self.next_start_pos # 次の階層に移動
        self.next_map, self.next_start_pos = self.generate_map() # 新しい次の階層を生成

    def get_tile(self, x, y):
        if y < 0 or y >= len(self.map) or x < 0 or x >= len(self.map[0]):
            return None # 範囲外の座標に対してNoneを返す
        return self.map[y][x]

    def is_stairs(self, x, y):
        tile = self.get_tile(x, y)
        return tile == '>' if tile else False
    
    def is_wall(self, x, y):
        if x < 0 or y < 0 or x >= len(self.map[0]) or y >= len(self.map):
            print(f"Warning: Attempted to access out-of-bounds index ({x}, {y})")
            return False
        return self.map[y][x] == '#'
