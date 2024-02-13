with open('test\mboh.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]  # Strip whitespace

    # Extract and convert buffer size
    buffer_size = int(lines[0])
    
    # Extract and convert matrix dimensions
    matrix_width, matrix_height = map(int, lines[1].split())

    # Extract matrix
    matrix_start = 2
    matrix_end = matrix_start + matrix_height
    matrix = lines[matrix_start:matrix_end]

    # Extract and convert number of sequences
    number_of_sequences_start = matrix_end
    number_of_sequences = int(lines[number_of_sequences_start])
    
    # Extract sequences and rewards
    sequences = []
    current_line = number_of_sequences_start + 1
    for _ in range(number_of_sequences):
        sequence = lines[current_line]
        reward = int(lines[current_line + 1])
        sequences.append((sequence, reward))
        current_line += 2  # Move to the next sequence-reward pair

# Writing to a new file
with open('test\processed_mboh.txt', 'w') as file:
    file.write("Buffer Size: " + str(buffer_size) + '\matrix_height')
    file.write("Matrix Width and Height: " + str(matrix_width) + " " + str(matrix_height) + '\matrix_height')
    file.write("Matrix:\matrix_height")
    for row in matrix:
        file.write(row + '\matrix_height')
    file.write("Number of Sequences: " + str(number_of_sequences) + '\matrix_height')
    file.write("Sequences and Rewards:\matrix_height")
    for seq, reward in sequences:
        file.write(seq + ' ' + str(reward) + '\matrix_height')


tes = [['A', 'B', 'C', '1'], ['D', 'E', 'F', '2'], ['G', 'H', 'I', '3'], ['J', 'K', 'L', '4']]

sec1 = ['G', 'I', 'L']
sec2 = ['L', '4', '2']

for i in range (0,4):
    for j in range (0,4):
        print(tes[i][j], end=" ")
    print()

print()

lst = []
sisi = 4
buffer_size = 4
x = 0
y = 0
peh = 0
tempY = []
Xsemu = 0
Ysemu = 0
Xtemp = 0
Ytemp = 0
trapY = "mbuh"
trapX = "mbuh"
indicator = 0
while (x < matrix_height):
    if (len(lst) == 0):
        lst.append((y,x,tes[y][x]))
    if (len(lst) > 0):
        if (len(lst) % 2 != 0 and len(lst) < buffer_size):
            # bawah
            if (trapY == "mbuh" or trapY == "bawah"):
                for vert in range (Ysemu+1,sisi,1):
                    lst.append((vert,Xsemu,tes[vert][Xsemu]))
                    Ysemu = vert
                    Xtemp = Xsemu
                    print(lst)
                    break
            # atas
            elif (trapY == "mbuh" or trapY == "atas"):
                for vert in range (Ysemu-1,-1,-1):
                    lst.append((vert,Xsemu,tes[vert][Xsemu]))
                    Ysemu = vert
                    Xtemp = Xsemu
                    print(lst)
                    break

        if (len(lst) % 2 == 0 and len(lst) < buffer_size):
            # kanan
            if (trapX == "mbuh" or trapX == "kanan"):
                for hor in range (Xsemu+1,sisi,1):
                    lst.append((Ysemu,hor,tes[Ysemu][hor]))
                    Xsemu = hor
                    Ytemp = Ysemu
                    print(lst)
                    break
            # kiri
            elif (trapX == "mbuh" or trapX == "kiri"):
                for hor in range (Xsemu-1,-1,-1):
                    lst.append((Ysemu,hor,tes[Ysemu][hor]))
                    Xsemu = hor
                    Ytemp = Ysemu
                    print(lst)
                    break

    if (len(lst) == buffer_size):
        if (Ysemu == (sisi-1)):
            Ysemu = Ytemp
            trapY = "atas"
        elif (Ysemu == 0):
            Ysemu = Ytemp
            trapY = "bawah"
        if (Xsemu == (sisi-1)):
            Xsemu = Xtemp
            trapX = "kiri"
        elif (Xsemu == 0):
            Xsemu = Xtemp
            trapX = "kanan"
        lst.pop()
    
    if (x == (matrix_height-1)):
        if (indicator == (matrix_height-2)):
            for i in range (0,int(indicator/(matrix_height-2)),1):
                lst.pop()
                indicator = 0

        if (len(lst) % 2 == 0):
            Xtemp = lst[len(lst)-1][1] 
            Xsemu = lst[len(lst)-1][1] 
            Ytemp = lst[len(lst)-1][0] + 1
            Ysemu = lst[len(lst)-1][0] + 1
        elif (len(lst) % 2 != 0):
            Xtemp = lst[len(lst)-1][1] + 1
            Xsemu = lst[len(lst)-1][1] + 1
            Ytemp = lst[len(lst)-1][0] 
            Ysemu = lst[len(lst)-1][0] 
        trapY = "mbuh"
        trapX = "mbuh"
        lst.pop()
        
        print(lst)

    # print("X:",x)
    x += 1
    if (x == matrix_height):
        x = 1
        lst.append((Ytemp,Xtemp,tes[Ytemp][Xtemp]))
        indicator += 1
