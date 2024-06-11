# `0x1B-web_stack_debugging_4`


### Task 0: Fixing Nginx Under Load

**Problem:**
Nginx is receiving a huge amount of failed requests when tested under load using ApacheBench.

**Solution:**
To solve this problem, we need to increase the limit on the number of file descriptors that Nginx can open simultaneously. This will allow Nginx to handle more concurrent connections and reduce the number of failed requests. Specifically, we will modify the Nginx configuration to set a higher limit and then restart the Nginx service to apply the changes.

### Task 1: Fixing User Login and File Opening Errors

**Problem:**
The user `holberton` encounters "Too many open files" errors when logging in and opening files.

**Solution:**
To resolve this issue, we need to increase the system-wide limit on the number of open files for all users. This involves editing the system's limits configuration file to set higher soft and hard limits for the number of open files. This change ensures that the user can open more files simultaneously without encountering errors.
