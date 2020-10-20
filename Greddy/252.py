def canAttendMeetings(intervels):
    intervels.sort()                                # O(nlog(n))
    for i in range(1, len(intervels)):
        if intervels[i][0] < intervels[i - 1][1]:
            return False
    return True


print(canAttendMeetings([[0,30], [5,10], [15,20]]))


# Time complexity O(nlog(n)), extra space complexity O(log(n))