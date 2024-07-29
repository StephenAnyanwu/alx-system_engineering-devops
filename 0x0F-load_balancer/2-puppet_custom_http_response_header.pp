#!/usr/bin/env bash
# configuration with puppet

exec { 'http header':
        command => 'sudo apt-get update -y;
        sudo apt-get install nginx -y;
        sudo sed -i "/sever_name _/a add_header X-Served_By HOSTNAME;" /etc/nginx/sites-available/default
        sudo service nginx restart',
        provider => shell,
}