
MAX_TALLY = 1000000000

def calculate(n):
    """
    Get the number of sub-periods for a given length of time (n). Happens to be equal
    to the nth number in a list where each item is equal to the previous item
    plus the current index.
    """
    if n == 0:
        return 0
    else:
        return calculate(n-1) + n


def count_sub_periods(start_index, end_index):
    """
    Get the number of sub-periods inside of a given start and end index, excluding
    sub-periods that are only three items long or less. The former have already
    been added to the tally, while the latter are invalid.
    """
    sub_periods = calculate(end_index - start_index - 3)
    return sub_periods


def solution(A):
    """
    Given a list of particle positions (A), calculate the number of time periods
    longer than three where the particle's velocity was stable. Track a running
    queue of three positions and compare the differences between the two pairs
    of consecutive positions. If they are equal, increment the tally that tracks
    periods of stability. Every time we find a period of stability, set the
    period_start_index, so that when the period ends, we can figure out how many
    internal periods of stability longer than three moments exist inside of the
    containing period and increment the tally accordingly.
    """
    max_index = len(A) - 1
    tally = 0
    
    if max_index < 2:
        return tally
    
    subsection = [A[0], A[1], A[2]]
    differences = [A[0] - A[1], A[1] - A[2]]
    
    # track the start index of a period of stability
    period_start_index = None
    
    i = 2
    
    while len(subsection) > 2:
        if differences[0] == differences[1]:
            tally += 1
            if period_start_index is None:
                period_start_index = i-2
        else:
            # accounting for enclosing time periods of stability when entering a period
            # of instability - increment tally for enclosing period and reset start index
            if period_start_index is not None:
                tally += count_sub_periods(period_start_index, i)
            period_start_index = None

        subsection.pop(0)
        differences.pop(0)
            
        if i + 1 <= max_index:
            i += 1
            new_num = A[i]
            subsection.append(new_num)
            differences.append(subsection[1] - new_num)
            
        if tally > MAX_TALLY:
            return -1
            
    if period_start_index is not None:
        tally += count_sub_periods(period_start_index, i+1)

    return tally
