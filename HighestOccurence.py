from collections import Counter

def highestOccurringElement(nums):
    # Count the frequency of each number
    counts = Counter(nums)
    
    max_freq = 0
    best_element = None
    
    # Find the element with the highest frequency. 
    # If there's a tie, keep the smaller element.
    for num, freq in counts.items():
        if freq > max_freq:
            max_freq = freq
            best_element = num
        elif freq == max_freq:
            if best_element is None or num < best_element:
                best_element = num
                
    return best_element