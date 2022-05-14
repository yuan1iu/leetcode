class Solution:
    def duplicateZeros(self, arr) -> None:
        zero = 0
        i = 0
        j = len(arr) - 1
        while i + zero < len(arr):
            if arr[i] == 0:
                zero += 1
            i += 1
        i -= 1
        if i + zero == len(arr):
            # the last zero should not be copied twice
            # hence, copy it directly to the last item of array
            # then zero--
            arr[j] = arr[i]
            i -= 1
            j -= 1
            zero -= 1

        while zero > 0:
            if arr[i] != 0:
                arr[j] = arr[i]
                j -= 1

            else:
                arr[j] = 0
                arr[j - 1] = 0
                j -= 2
                zero -= 1
            i -= 1
