from collections import Counter

def freq_cal(str1):
    freqs = Counter(str1)
    # print(freqs)
    freq_counts = Counter(freqs.values())
    # print(freq_counts)

    if len(freq_counts) == 1 :
        return "yes"

    if len(freq_counts) > 2 :
        return "no"  


    min, max = sorted(freq_counts.keys())

    if (( freq_counts[min] == 1 and max - min == 1) or (freq_counts[max] == 1 and max - min == 1) ):
        return "yes"
    

print(freq_cal("abcc"))