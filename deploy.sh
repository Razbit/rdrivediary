#!/bin/bash

# This script is used to deploy the RDriveDiary system, according to
# rules set in the configuration file rdd.conf
#
# Copyright Eetu "Razbit" Pesonen, 2015
#
# This file is part of RDriveDiary.
# 
# RDriveDiary is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# RDriveDiary is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with RDriveDiary.  If not, see <http://www.gnu.org/licenses/>.
#
# Code for parsing the config file inspired by code from Stackoverflow 
# user Antonio
#

# ==== VARS ==== #
depl_ver=0.01
configfile="rdd.conf"

# ==== CODE ==== #
if [ "$(id -u)" != "0" ]; then
    echo "This script is intended to be run as the web-server user, e.g. root." 
    read -p "Continue (Y/n)? " yn
    case $yn in
        [Nn]* ) exit;;
    esac
fi

shopt -s extglob

tr -d '\r' < $configfile > $configfile.unix

while IFS='= ' read lhs rhs
do
    if [[ ! $lhs =~ ^\ *# && -n $lhs ]]; then
        rhs="${rhs%%\#*}"    # Del in line right comments
        rhs="${rhs%%*( )}"   # Del trailing spaces
        rhs="${rhs%\"*}"     # Del opening string quotes 
        rhs="${rhs#\"*}"     # Del closing string quotes 
        declare $lhs="$rhs"
    fi
done < $configfile.unix
rm $configfile.unix

echo "RDriveDiary deployer, v$depl_ver"
echo 'Eetu "Razbit" Pesonen, 2015'
echo ""

echo "Deploying RDriveDiary v$version to $server_path"
mkdir -pv $server_path

# Copy the relevant files to appropriate locations.
mkdir -pv $server_path/cgi-bin/log
cp -v index.html $server_path/index.html
cp -v rdd.conf $server_path/rdd.conf
cp -v cgi-bin/main.py $server_path/cgi-bin/main.py


echo "Done"
