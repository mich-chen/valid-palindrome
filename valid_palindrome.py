from typing import List

def isPalindrome(s: str) -> bool:

    if not s:
        return True

    string = list(filter(str.isalnum, s.lower()))

    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return False

    return True


if __name__ == '__main__':

    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
