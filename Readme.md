# Regular expression syntax cheatsheet
###### Regular Expression Syntax Cheat Sheet

<table style="width: 100%">
<tbody>
<tr>
<th>Element</th>
<th>Short Description</th>
</tr>
<tr>
<td>\</td>
<td>Forces special characters to be treated as ordinary characters</td>
</tr>
<tr>
<td>^</td>
<td>Indicates the beginning of the pattern (i.e., forces checking from the first character)</td>
</tr>
<tr>
<td>$</td>
<td>Indicates the end of the pattern (i.e., forces checking until the last character)</td>
</tr>
<tr>
<td>*</td>
<td>Used when the preceding character or group may occur zero or more times</td>
</tr>
<tr>
<td>+</td>
<td>Used when the preceding character or group may occur one or more times</td>
</tr>
<tr>
<td>?</td>
<td>Used when the preceding character or group may occur zero or one time</td>
</tr>
<tr>
<td>.</td>
<td>Represents any single character</td>
</tr>
<tr>
<td>[abc]</td>
<td>Represents any single character within the brackets</td>
</tr>
<tr>
<td>[^abc]</td>
<td>Represents any single character not within the brackets</td>
</tr>
<tr>
<td>[a-z]</td>
<td>Represents any single character within the specified range</td>
</tr>
<tr>
<td>[^a-z]</td>
<td>Represents any single character not within the specified range</td>
</tr>
<tr>
<td>x|y</td>
<td>Represents either "x" or "y"</td>
</tr>
<tr>
<td>(pattern)</td>
<td>Represents a group</td>
</tr>
<tr>
<td>(?&lt;name&gt;pattern)</td>
<td>Creates a named group</td>
</tr>
<tr>
<td>{n}</td>
<td>Represents when the preceding character or group occurs exactly "n" times</td>
</tr>
<tr>
<td>{n,}</td>
<td>Represents when the preceding character or group occurs "n" or more times</td>
</tr>
<tr>
<td>{n,m}</td>
<td>Represents when the preceding character or group occurs at least "n" and at most "m" times</td>
</tr>
<tr>
<td>(?=…)</td>
<td>Positive lookahead (requires a specific character or text to be present in the search context)</td>
</tr>
<tr>
<td>(?!…)</td>
<td>Negative lookahead (requires a specific character or text to be absent in the search context)</td>
</tr>
<tr>
<td>(?&lt;!-)\d</td>
<td>Negative lookahead (Represents a digit not preceded by a negative sign)</td>
</tr>
<tr>
<td>(?&lt;=-)\d</td>
<td>Positive lookahead (Represents a digit preceded by a negative sign)</td>
</tr>
<tr>
<td>\b</td>
<td>Represents the boundary between a word character and a non-word character</td>
</tr>
<tr>
<td>\B</td>
<td>Represents a position that is not a word boundary</td>
</tr>
<tr>
<td>\d</td>
<td>Represents a digit</td>
</tr>
<tr>
<td>\D</td>
<td>Represents a non-digit character</td>
</tr>
<tr>
<td>\n  or \r\n</td>
<td>Represents a new line</td>
</tr>
<tr>
<td>\s</td>
<td>Represents a whitespace character</td>
</tr>
<tr>
<td>\S</td>
<td>Represents a non-whitespace character</td>
</tr>
<tr>
<td>\t</td>
<td>Represents a tab</td>
</tr>
<tr>
<td>\w</td>
<td>Represents a word character, including "_" but excluding other symbols</td>
</tr>
<tr>
<td>\W</td>
<td>Represents a non-word character, excluding "_" but including other symbols</td>
</tr>
</tbody>
</table>

<h2>Top 5 Regular Expressions</h2>
<table style="width: 100%">
    <tbody>
        <tr><th>Email</th></tr>
        <tr><td>^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$</td></tr>
        <tr><th>Web Address</th></tr>
        <tr><td>^(http(s):\/\/.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$</td></tr>
        <tr><th>Phone Number</th></tr>
        <tr><td>^(\+994|0)(50|51|55|70|77|99|10)-(\d{3}-\d{2}-\d{2})$</td></tr>
        <tr><th>Name</th></tr>
        <tr><td>^[A-ZƏ]{1}[a-zə]{2,}$</td></tr>
        <tr><th>Password</th></tr>
        <tr><td>^((?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#])).{8,}$</td></tr>
    </tbody>
</table>
