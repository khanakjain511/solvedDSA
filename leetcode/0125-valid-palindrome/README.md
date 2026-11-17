# 125. Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen) ![Topic](https://img.shields.io/badge/Topic-Two_Pointers-blue) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 8 ms |
| Memory | 19.7 MB |
| Submission Date | 2026-11-17T05:41:06.767Z |
| Platform | leetcode |

## Problem Statement

<p>A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.</p>

<p>Given a string <code>s</code>, return <code>true</code><em> if it is a <strong>palindrome</strong>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p>
```

**Example 2:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p>
```

**Example 3:**

```
</p>

<pre>
<strong>Input:</strong> s = &quot; &quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> s is an empty string &quot;&quot; after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
</pre>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code>
- <code>s</code> consists only of printable ASCII characters.

## Solution

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True

```

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)
