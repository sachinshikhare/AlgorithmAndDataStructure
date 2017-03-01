def least_common_subsequence(str1, str2, len_str1, len_str2):
    if len_str1 == 0 or len_str2 == 0:
        return 0
    elif str1[len_str1-1] == str2[len_str2-1]:
        return 1 + least_common_subsequence(str1, str2, len_str1-1, len_str2-1)
    else:
        return max(least_common_subsequence(str1, str2, len_str1-1, len_str2), 
                   least_common_subsequence(str1, str2, len_str1, len_str2-1)) 
        
X = "character"
Y = "retcarahc"
print( "Length of LCS is ", least_common_subsequence(X , Y, len(X), len(Y)))
