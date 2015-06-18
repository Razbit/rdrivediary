#!/bin/bash

# This script is used to update the RDriveDiary system.
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
upd_ver=0.01
configfile="rdd.conf"

# ==== CODE ==== #
if [ "$(id -u)" != "0" ]; then
    echo "This script is intended to be run as the web-server user, e.g. root." 
    read -p "Continue (Y/n)? " yn
    case $yn in
        [Nn]* ) exit;;
    esac
fi

# Parse the config file
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


echo "RDriveDiary updater, v$upd_ver"
echo 'Eetu "Razbit" Pesonen, 2015'
echo ""

echo "Updating the RDriveDiary system to version $version"
read -p "Please type the path of the install: " configpath

echo "Fetching the original configuration.."
if [[ `ls $configpath | grep rdd.conf` == "rdd.conf" ]]; then
    echo "Found configuration from $configpath"
else
    echo "No previous configuration found in the given location."
fi

cp $configpath/rdd.conf ./rdd.conf.orig

echo "The configuration files have the following differences:"
diff ./rdd.conf.orig ./rdd.conf -iwB

echo "Make sure rdd.conf is correct, then run deploy.sh"
