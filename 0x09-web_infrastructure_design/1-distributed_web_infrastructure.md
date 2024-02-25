[Imgur](https://imgur.com/VYs8oKB)

a three server web infrastructure that hosts the website www.foobar.com

Issues:

###SPOFs:
Load balancer: If it fails, all traffic is blocked. Consider redundant load balancers.
Database primary node: Data loss or unavailability if it fails. Implement high availability solutions like clustering.

### Security:
No firewall: Exposes servers to potential attacks. Implement firewalls for each server.
No HTTPS: Communication is unencrypted, making it vulnerable to eavesdropping. Implement SSL/TLS certificates for secure communication.
Monitoring: No insights into server performance or potential issues. Implement monitoring tools for servers, applications, and databases.

This design demonstrates a more robust and scalable infrastructure compared to the single server setup. However, it still has limitations and requires careful security considerations and monitoring practices.
