from typing import List

def reverseString(s: List[str]) -> None:
   

    if len(s) == 1:
        return s
    
    elif len(s) == 2:
        temp = s[1]
        s[1] = s[0]
        s[0] = temp
    
    else: 
        max_range = int(len(s)/2)

        for i in range(max_range):
            left = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = left
    
    return s


if __name__ == "__main__":
    s = ["a", "p", "p", "l", "e"]
    print(s)
    print(reverseString(s))

    s = ["a"]
    print(s)
    print(reverseString(s))

    s = ["a", "p"]
    print(s)
    print(reverseString(s))