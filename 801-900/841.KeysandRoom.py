class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        all_keys = set()
        all_keys.add(0)
        keys = rooms[0]


        while keys:
            temp = []
            for key in keys:
                if key not in all_keys:
                    temp += rooms[key]
                    all_keys.add(key)

            keys = temp

        
        return False if len(all_keys) < len(rooms) else True
