`0x17-web_stack_debugging_3`

# Apache 500 Internal Server Error - Troubleshooting and Fix

## Error Description
The Apache web server was returning a 500 Internal Server Error when accessing a WordPress site. The server logs were not providing clear reasons for the error.

## Troubleshooting and Fix

1. **Initial Diagnosis:**
   - Reviewed Apache error and access logs:
     ```sh
     sudo cat /var/log/apache2/error.log
     sudo cat /var/log/apache2/access.log
     ```
   - Identified 500 status codes in the logs.

2. **Using `strace`:**
   - Attached `strace` to the Apache process to trace system calls and signals:
     ```sh
     ps aux | grep apache2
     sudo strace -p <apache_pid> -o /tmp/strace_apache.log
     ```
   - Observed repeated `select` and `wait4` system calls, which indicated the process was waiting for some event or input.

3. **Error Identification:**
   - Investigated the WordPress configuration files for potential errors.
   - Discovered a typo in `wp-settings.php` where `.phpp` was written instead of `.php`.

4. **Fix Applied:**
   - Used a Puppet script to correct the typo in `wp-settings.php`:
     ```sh
     sudo puppet apply -e "exec { 'Typo Fix': command => 'sudo sed -i \"s/.phpp/.php/\" /var/www/html/wp-settings.php', provider => shell }"
     ```
   - Restarted Apache to apply the changes:
     ```sh
     sudo service apache2 restart
     ```

The typo in the `wp-settings.php` file was causing the PHP script to fail, leading to the 500 Internal Server Error. Fixing this typo resolved the error, and the server resumed normal operations.
