# 0x10. HTTPS SSL
`DevOps,SysAdmin,Security`

**Task 1: Configuring Domain Zone and Writing a Bash Script**

Configured the domain zone to point the subdomains `www`, `lb-01`, `web-01`, and `web-02` to their respective IP addresses. Additionally, wrote a Bash script that displays information about these subdomains. The script accepts a domain name and an optional specific subdomain as arguments, providing information about the specified subdomain or default subdomains (`www`, `lb-01`, `web-01`, `web-02`) if only the domain is provided. Utilized Bash functions, `awk`, and `dig`, while ignoring the ShellCheck case SC2086.

**Task 2: Terminating SSL on HAProxy**

Configured HAProxy to terminate SSL, meaning it handles encrypted traffic, decrypts it, and forwards it to its destination. Created a certificate using certbot and configured HAProxy to accept encrypted traffic for the `www` subdomain. HAProxy was set to listen on TCP port 443, accepting SSL traffic, and serving encrypted traffic that returned the root of the web server containing "Hello World!".

**Task 3: Enforcing HTTPS Traffic with HAProxy**

Enforced HTTPS traffic by configuring HAProxy to automatically redirect HTTP traffic to HTTPS. This redirection was transparent to the user, returning a 301 status code. The HAProxy configuration file was modified to achieve this redirection.


### Tip: Concatenating SSL Certificate Files

If you're configuring SSL termination with HAProxy, you'll need to provide the SSL certificate and private key files. Typically, these files are `fullchain.pem` (containing the full certificate chain) and `privkey.pem` (containing the private key).

To use these files with HAProxy, you'll often need to concatenate them into a single file. You can do this using the `cat` command in your terminal:

```bash
cat fullchain.pem privkey.pem > combined_cert.pem
```
