
def seats_are_empty(seats, seat_group):
    """
    Check whether a given group of seats are empty, that is
    not found in the collection of reserved seats.
    """
    for seat in seat_group:
        if seat in seats:
            return False
            
    return True


def solution(N, S):
    """
    Given a number of rows and a space separated string of
    reserved seats, return the number of 4-person families
    can sit together on the flight. Transform the string of
    reservations into a set for easy lookup. Going row by row,
    check each viable group of seats (that is, starting with
    seat B, D, or F) and check whether all four seats in the
    group are available.
    """    
    families = 0
    seats = S.split(' ')
    seats = set(seats)
   
    for row in range(1, N+1):
        group_1 = [f'{row}B', f'{row}C', f'{row}D', f'{row}E']
        group_2 = [f'{row}F', f'{row}G', f'{row}H', f'{row}J']
        group_3 = [f'{row}D', f'{row}E', f'{row}F', f'{row}G']

        if seats_are_empty(seats, group_1):
            families += 1
            if seats_are_empty(seats, group_2):
                families += 1
               
        elif seats_are_empty(seats, group_3):
            families += 1
            
        elif seats_are_empty(seats, group_2):
            families += 1
            
    return families
