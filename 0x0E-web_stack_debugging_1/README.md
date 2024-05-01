`0x0E-web_stack_debugging_1`

Issue:
Nginx was not listening on port 80, preventing it from serving web traffic as expected.

Solution:
Wrote a Bash script to automate the fix by removing conflicting configurations, creating a symlink to the default configuration file, and restarting Nginx.
