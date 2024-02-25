[Imgur](https://imgur.com/8WLNA2j)

### Why Add Each Element:

* Firewalls: Enhance security by controlling network access and preventing unauthorized attempts.
* SSL Certificate (HTTPS): Encrypts traffic between users and the website, protecting sensitive data from eavesdropping.
* Monitoring Clients: Provide insights into server performance, resource utilization, potential issues, and overall website health.

### Monitoring Explanation:

Monitoring clients collect data like CPU usage, memory consumption, response times, and error logs.
This data is sent to a central monitoring service (like Sumologic) for analysis and visualization.
You can monitor web server QPS (queries per second) by tracking incoming requests and database interactions.

### Issues with the Infrastructure:

* SSL Termination at Load Balancer
* Single Writeable MySQL Server: Creates a Single Point of Failure (SPOF).
* Identical Server Components: Makes scaling specific components (e.g., database) difficult.
