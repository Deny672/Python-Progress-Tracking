"""
Your task, is to calculate the minimal number of moves to win the game
"Towers of Hanoi", with given number of disks.
"""
def search_count_move(count_disk):
    return (2 ** count_disk) - 1

a = 10
print(search_count_move(a))