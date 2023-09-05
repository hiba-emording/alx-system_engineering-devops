## Scripts:

* 0: A script that prints “Hello, World”, followed by a new line to the standard output
```
#!/bin/bash
echo "Hello, World"
```

* 1: A script that displays a confused smiley
```
#!/bin/bash
echo "\"(Ôo)'"
```

* 2: A script that Display the content of the /etc/passwd file
```
#!/bin/bash
cat /etc/passwd
```

* 3: A script that Display the content of /etc/passwd and /etc/hosts
```
#!/bin/bash
cat /etc/passwd /etc/hosts
```

* 4: A script that Display the last 10 lines of /etc/passwd
```
#!/bin/bash
tail /etc/passwd
```

* 5: A script that Display the first 10 lines of /etc/passwd
```
#!/bin/bash
head /etc/passwd
```

* 6: A script that displays the third line of the file iacta
```
#!/bin/bash
head -n 3 iacta | tail -n 1

* 7:* 7:: A shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line
```
#!/bin/bash
echo "Best School" > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*:\)
```

* 8: A script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it

```
#!/bin/bash
ls -la > ls_cwd_content
```

* 9: A script that duplicates the last line of the file iacta
```
#!/bin/bash
tail -n 1 iacta >> iacta
```

* 10: A script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders
```
#!/bin/bash
find . -name "*.js" -type f -delete
```

* 11: A script that counts the number of directories and sub-directories in the current directory.

The current and parent directories should not be taken into account
Hidden directories should be counted
```
#!/bin/bash
find . -mindepth 1 -type d \( ! -name '.*' \) | wc -l
```

* 12: A script that displays the 10 newest files in the current directory.

Requirements:

One file per line
Sorted from the newest to the oldest
```
#!/bin/bash
ls -t | head -n 10
```

* 13: A script that takes a list of words as input and prints only words that appear exactly once.

Input format: One line, one word
Output format: One line, one word
Words should be sorted
```
#!/bin/bash
sort | uniq -u
```

* 14: A script that Display lines containing the pattern “root” from the file /etc/passwd
```
#!/bin/bash
grep root /etc/passwd
```

* 15: A script that Display the number of lines that contain the pattern “bin” in the file /etc/passwd
```
#!/bin/bash
grep bin /etc/passwd | wc -l
```
* 16: A script that Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd
```
#!/bin/bash
grep -A 3 "root" /etc/passwd
```
* 17: A script that Display all the lines in the file /etc/passwd that do not contain the pattern “bin”
```
#!/bin/bash
grep -v bin /etc/passwd
```
* 18: A script that Display all lines of the file /etc/ssh/sshd_config starting with a letter.

include capital letters as well
```
#!/bin/bash
grep '^[[:upper:]]\|^[[:lower:]]' /etc/ssh/sshd_config
```

* 19: A script that Replace all characters A and c from input to Z and e respectively.
```
#!/bin/bash
tr Ac Ze
```

* 20: A script that removes all letters c and C from input
```
#!/bin/bash
tr -d Cc
```
* 21: A script that reverse its input
```
#!/bin/bash
rev
```

* 22: A script that displays all users and their home directories, sorted by users.

Based on the the /etc/passwd file
```
#!/bin/bash
cut -d ':' -f1,6 /etc/passwd | sort
```
* 23: A command that finds all empty files and directories in the current directory and all sub-directories.

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
```
#!/bin/bash
find . -empty -printf '%f\n'
```
* 24: A script that lists all the files with a .gif extension in the current directory and all its sub-directories.

Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
```
#!/bin/bash
find -type f -name "*.gif" | rev | cut -d '/' -f 1 | cut -d '.' -f 2- | rev | LC_ALL=C sort -f
```

* 25: A  script that decodes acrostics that use the first letter of each line.

The ‘decoded’ message has to end with a new line
```
#!/bin/bash
cut -c 1 | paste -s -d ''
```

* 26: A script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

Order by number of requests, most active host or IP at the top

```
#!/bin/bash
tail -n +2 | cut -f 1 | sort -k 1 | uniq -c | sort -rnk 1 | head -n 11 | rev | cut -d ' ' -f 1 | rev
```
