## Scripts used:

* 0: a script that switches the current user to the user betty
**su betty**

* 1: a script that prints the effective username of the current user
**whoami**

* 2: a script that prints all the groups the current user is part of
**groups**

* 3: a script that changes the owner of the file hello to the user betty
**chown betty hello**

* 4: a script that creates an empty file called hello
**touch hello**

* 5: a script that adds execute permission to the owner of the file hello
**chmod u+x hello**

* 6: a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello
**chmod u+x,g+x,o+r hello**

* 7: a script that adds execution permission to the owner, the group owner and the other users, to the file hello
**chmod a+x hello**

* 8: a script that sets the permission to the file hello as follows:

Owner: no permission at all
Group: no permission at all
Other users: all the permissions

**chmod 007 hello**

* 9: a script that sets the mode of the file hello to this:

-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

**chmod 753 hello**

* 10: a script that sets the mode of the file hello the same as olleh’s mode
**chmod --reference=olleh hello**

* 11: a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users.

Regular files should not be changed.

**chmod -R a+x '*'/**

* 12: a script that creates a directory called my'_'dir with permissions 751 in the working directory
mkdir -m 751 my'_'dir

* 13: a script that changes the group owner to school for the file hello
**chgrp school hello**

* 14: a script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory
**chown vincent:staff '*'**

* 15: a script that changes the owner and the group owner of _hello to vincent and staff respectively
chown -h vincent:staff _hello

* 16: a script that changes the owner of the file hello to betty only if it is owned by the user guillaume
**chown --from=guillaume betty hello**

* 17: a script that will play the StarWars IV episode in the terminal
**talnet towel.blinkenlights.nl**

