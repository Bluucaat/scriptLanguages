def escape_from_alcatraz():
    doors = [0] * 600

    for step in range(1, 601):
        for cell in range(step - 1, 600, step):
            # Flip the lock (0 to 1 or 1 to 0)
            if doors[cell] == 0:
                doors[cell] = 1
            else:
                doors[cell] = 0

    # Find the indices of open doors
    open_doors = []
    for i in range(len(doors)):
        if doors[i] == 1:
            open_doors.append(str(i + 1) + " ")

    return ''.join(open_doors)


print(escape_from_alcatraz())
