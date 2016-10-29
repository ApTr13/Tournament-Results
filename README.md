# Tournament-Results
A project for keeping the track of a Swiss-style tournament.... By creating a Python Module using PostgreSQL.....

###Contents
1. **tournament.py** - A py module comprising all the functions to track a Swiss tournament
2. **tournament.sql** - A file having all sql commands for creating required Database, Tables & Views
3. **tournament_test.py** - A sample test prepared to check the tournament.py module
4. **tournament.pyc** - Pre-compiled version of tournament.py

In order to run a database, the following things need to be set up:

1. [Virtual Box](https://www.virtualbox.org/)
2. [Vagrant](https://www.vagrantup.com/downloads.html) Virtual Machine
3. [Git](https://git-scm.com/downloads) on Windows(Terminal on Linux/Mac)

Now fork and clone [fullstack-nanodegree-vm repository]() so that you get the directory fullstack in your current User.

### Running The Python module for tournament results  
1. Clone this repository [Tournament-Results](https://github.com/ApTr13/Tournament-Results)

2. Go to **fullstack->vagrant->tournament**

3. Extract the files of **Tournamet-Results** here and replace the incomplete project files

4. Now open your Terminal/Cmd/GitBash and give following commands from home folder:
> cd fullstack\vagrant

5. Boot the virtual machine into Virtual box.
> vagrant up

6. Virtual machine gets booted. Now start vagrant with the command:
> vagrant ssh

7. cd to the tournament folder from home as
> cd vagrant\tournament

8. First we need to set up sql so give command for **PostgreSQL** as
> psql

9. Setup the **tournament database** from **tournament.sql** as
> \i tournament.sql

10. Required database, tables and views get created. Exit Postgresql as
> \q

11. Complie the **tournament.py** module as
> python tournament.py

12. Now test it against given **tournament-test.py** or against your own test file 
> python tournament-test.py

Remember that you can see or edit the py module outside the virtual box... The job of Vagrant is to help set up the database in Psql..
Install [Python 2.7](https://www.python.org/download/releases/2.7/) to compile the module....
Read about the PostgreSQL [here](https://www.postgresql.org/docs/)...

For furthur queries, contact apurvatripathi13@gmail.com..... :D
