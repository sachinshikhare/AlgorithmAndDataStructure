""" LONGEST PALINDROME SUBSEQUENCE : use same implementation as LCS, just pass 2nd string as reverse of 1st string """

""" Dynamic programming by memoization """
def lcs_by_memoization(str1, str2, len_str1, len_str2, arr):
    if arr[len_str1][len_str2] != -1:
        return arr[len_str1][len_str2]
    else:
        if len_str1 == 0 or len_str2 == 0:
            arr[len_str1][len_str2] = 0
        elif str1[len_str1-1] == str2[len_str2-1]:
            arr[len_str1][len_str2] = 1 + lcs_by_memoization(str1, str2, len_str1-1, len_str2-1, arr)
        else:
            arr[len_str1][len_str2] = max(lcs_by_memoization(str1, str2, len_str1-1, len_str2, arr), 
                       lcs_by_memoization(str1, str2, len_str1, len_str2-1, arr)) 
        return arr[len_str1][len_str2]

""" Dynamic programming by bottom up """
def lcs_bottom_up_approach(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    arr = [[None]*(len2+1) for _ in range(len1+1)]
    
    for cntr1 in range(len1+1):
        for cntr2 in range(len2+1):
            if cntr1 == 0 or cntr2 == 0:
                arr[cntr1][cntr2] = 0
            elif str1[cntr1-1] == str2[cntr2-1]:
                arr[cntr1][cntr2] = 1 + arr[cntr1-1][cntr2-1]
            else:
                arr[cntr1][cntr2] = max(arr[cntr1-1][cntr2],arr[cntr1][cntr2-1])
    return arr[len1][len2]

str = "MyNameIsSachinShikhare"

arr = [[-1 for y in range(len(str)+1)] for x in range(len(str)+1)]
print( "lcs_by_memoization: ", lcs_by_memoization(str , str[::-1], len(str), len(str), arr))
print( "lcs_by_memoization: ", lcs_bottom_up_approach(str , str[::-1]))
