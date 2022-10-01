class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index_dict = dict()
        zigzag_index = 0
        down = 1  # Down flag
        up = -1  # Up flag
        move = 0
        for character in s:
            if zigzag_index == 0:  # Down
                move = down
            elif zigzag_index == numRows - 1:  # Up
                move = up

            index_dict[zigzag_index] = index_dict.get(zigzag_index, '') + character
            zigzag_index +=move  # Move index

        return ''.join(index_dict.values())