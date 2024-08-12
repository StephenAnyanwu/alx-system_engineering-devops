/*Create user named holberton_user with the host name set to localhost and the password projectcorrection280hbtn
on primary/replica */
CREATE USER holberton_user@localhost IDENTIFIED BY "projectcorrection280hbtn";

/*Grant holberton_user permission to check the primary/replica status of your databases*/
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

/*Create a database on the prrimary server (web-01) named tyrell_corp and use it*/
CREATE DATABASE tyrell_corp;
USE tyrell_corp;

/*Create a table nameed nexus6 and insert one entry to it*/
CREATE TABLE nexus6 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);
INSERT INTO nexus6(name) VALUES ("Stephen");

/*Grant holberton_user SELECT permissions on nexus6 table*/
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost;

/* On your primary MySQL server (web-01), create a new user 'replica_user' with the host name set
to % that is any IP,  with whatever password say 'password' for the replica server.*/
CREATE USER replica_user@'%' IDENTIFIED BY "password";

/*On your primary MySQL server (web-01), grant the replica_user appropriate permissions to
replicate your primary MySQL server.*/
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

/*Grant holberton_user SELECT permissions on mysql.user table*/
GRANT SELECT ON mysql.user TO holberton_user@localhost;
