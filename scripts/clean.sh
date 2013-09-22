#!/bin/bash 
# Brandon Thomas <bt@brand.io>

# Sets the directory of the current script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJ_DIR="$DIR/.."

# Password is not set! Use `ssh-copy-id` to prevent fumbling around with it.
export USER='laser'
export HOST='169.254.10.49'
export DIR_ROOT='/home/laser/dev/gamejam-demo'

#
# Functions and Aliases
# _____________________

# XXX: May need to `sudo visudo` and comment out `Defaults requiretty`
shopt -s expand_aliases
alias rsync="rsync -zrpvuL -e ssh --exclude-from=$DIR/exclude.txt --progress" 

function print_status() {
	status=$1
	length=${#1}
	echo ''
	echo $status
	for i in $(seq $length); do echo -n '='; done
	echo ''
}

print_status 'Clean everything'
ssh -o "StrictHostKeyChecking no" $USER@$HOST << ENDHERE
  cd $DIR_ROOT &&	rm -rf *
ENDHERE
