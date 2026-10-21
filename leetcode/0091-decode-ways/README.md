# 91. Decode Ways

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow) ![Topic](https://img.shields.io/badge/Topic-String-blue) ![Topic](https://img.shields.io/badge/Topic-Dynamic_Programming-blue) ![Language](https://img.shields.io/badge/Language-python3-orange)

## Metadata

| Field | Value |
| --- | --- |
| Runtime | 1 ms |
| Memory | 19.4 MB |
| Submission Date | 2026-10-21T03:51:16.308Z |
| Platform | leetcode |

## Problem Statement

<p>You have intercepted a secret message encoded as a string of numbers. The message is <strong>decoded</strong> via the following mapping:</p>

<p><code>&quot;1&quot; -&gt; &#39;A&#39;<br />
&quot;2&quot; -&gt; &#39;B&#39;<br />
...<br />
&quot;25&quot; -&gt; &#39;Y&#39;<br />
&quot;26&quot; -&gt; &#39;Z&#39;</code></p>

<p>However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (<code>&quot;2&quot;</code> and <code>&quot;5&quot;</code> vs <code>&quot;25&quot;</code>).</p>

<p>For example, <code>&quot;11106&quot;</code> can be decoded into:</p>

<ul>
	<li><code>&quot;AAJF&quot;</code> with the grouping <code>(1, 1, 10, 6)</code></li>
	<li><code>&quot;KJF&quot;</code> with the grouping <code>(11, 10, 6)</code></li>
	<li>The grouping <code>(1, 11, 06)</code> is invalid because <code>&quot;06&quot;</code> is not a valid code (only <code>&quot;6&quot;</code> is valid).</li>
</ul>

<p>Note: there may be strings that are impossible to decode.<br />
<br />
Given a string s containing only digits, return the <strong>number of ways</strong> to <strong>decode</strong> it. If the entire string cannot be decoded in any valid way, return <code>0</code>.</p>

<p>The test cases are generated so that the answer fits in a <strong>32-bit</strong> integer.</p>

<p>&nbsp;</p>
<p>

## Examples

**Example 1:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;12&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>&quot;12&quot; could be decoded as &quot;AB&quot; (1 2) or &quot;L&quot; (12).</p>
</div>

<p>
```

**Example 2:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;226&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>&quot;226&quot; could be decoded as &quot;BZ&quot; (2 26), &quot;VF&quot; (22 6), or &quot;BBF&quot; (2 2 6).</p>
</div>

<p>
```

**Example 3:**

```
</p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;06&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>&quot;06&quot; cannot be mapped to &quot;F&quot; because of the leading zero (&quot;6&quot; is different from &quot;06&quot;). In this case, the string is not a valid encoding, so return 0.</p>
</div>

<p>&nbsp;</p>
```

## Constraints

- <code>1 &lt;= s.length &lt;= 100</code>
- <code>s</code> contains only digits and may contain leading zero(s).

## Solution

```py
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        
        prev2, prev1 = 1, 1

        for i in range(1, len(s)):
            curr = 0
            if s[i] != '0':
                curr+=prev1
            two = int(s[i-1:i+1])
            if 10<=two<=26:
                curr+=prev2
            
            prev2, prev1 = prev1, curr
        return prev1
```

[View on LeetCode](https://leetcode.com/problems/decode-ways/)
