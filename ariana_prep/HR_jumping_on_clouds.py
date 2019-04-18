#!/usr/bin/env python


def jumpingOnClouds(c):
    jumps = 0
    emmas_location = -1
    num_clouds = len(c)
    print('num_clouds', num_clouds)
    while emmas_location < num_clouds - 2:
        if c[emmas_location + 2] == 0:
            emmas_location += 2
        else:
            emmas_location += 1
        print('emmas_location', emmas_location)
        jumps += 1

    return jumps + num_clouds - emmas_location - 1


def main():
    c = [0, 0, 1, 0, 0, 1, 0]
    print(jumpingOnClouds(c))
    print('should be 4')
    c2 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
    print(jumpingOnClouds(c2))
    print('should be 6')
    c3 = [0, 0, 0, 1, 0, 0]
    print(jumpingOnClouds(c3))
    print('should be 3')

if __name__ == '__main__':
    main()
