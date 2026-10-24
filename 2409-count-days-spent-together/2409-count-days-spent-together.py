class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def getDay(date):
            month = int(date[:2])
            day = int(date[3:])

            total = day

            for i in range(month - 1):
                total += days[i]

            return total

        alice_start = getDay(arriveAlice)
        alice_end = getDay(leaveAlice)

        bob_start = getDay(arriveBob)
        bob_end = getDay(leaveBob)

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        if start > end:
            return 0

        return end - start + 1