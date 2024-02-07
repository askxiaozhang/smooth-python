l = [10, 20, 30, 40, 50, 60]

print(l[:2]) # 在下标2的地方分割

print(l[2:])
print(l[2:5])
print(l[:3]) # 在下标3的地方分割

print(l[3:])

invoice = """
0.....6................................40........52...55........
1909 Pimoroni PiBrella
$17.50
3
$52.50
1489 6mm Tactile Switch x20
$4.95
2
$9.90
1510 Panavise Jr. - PV-201
$28.00
1
$28.00
1601 PiTFT Mini Kit 320x240
$34.95
1
$34.95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

demo = "123"
print(demo[0:2] == demo[slice(0,2)])

row=['_'] * 3
board = []
for i in range(3):
    board.append(row)
board[0][1] = "NB"
print(board)

board = []
for i in range(3):
    row=['_'] * 3 # ➊
    board.append(row)
board[0][1] = "NB"
print(board)

board = [['_'] * 3 for i in range(3)]
print(board)

board[0][1] = 'NB'
print(board)
