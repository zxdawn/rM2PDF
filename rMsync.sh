#!/bin/bash
# Sync script for the reMarkable reader
# Version: 0.1
# Author: Simon Schilling
# Edit: Xin Zhang
# Licence: MIT

# Remote configuration
RMDIR="/home/root/.local/share/remarkable/xochitl/"
RMUSER="root"
RMIP="10.11.99.1"
SSHPORT="22"

# Local configuration
#---------------------------------------------------------------------#
MAINDIR="/mnt/d/rM"
BACKUPDIR="$MAINDIR/original_pdf/"      # Download all rM contents
OUTPUTDIR="$MAINDIR/noted_pdf/"         # PDFs of everything on the rM
TEMPORARYDIR="$MAINDIR/temporary/"
#---------------------------------------------------------------------#
LOG="sync.log"                          # Log file name in $MAINDIR
LOG="$MAINDIR/$(date +%y%m%d)-$LOG"

echo $'\n' >> $LOG
date >> $LOG

if [ "$RMUSER" ] && [ "$SSHPORT" ]; then
  S="ssh -p $SSHPORT -l $RMUSER";
fi

# check for rM
$S $RMIP -q exit

if [ $? == "0" ]; then

  # Download all files
  echo "BEGIN BACKUP" >> $LOG
  mkdir -p "$BACKUPDIR"
  echo "scp \"$RMUSER@$RMIP:$RMDIR\" $BACKUPDIR"  >> $LOG
  scp -r "$RMUSER@$RMIP:\"$RMDIR\"*" "$BACKUPDIR" >> $LOG 2>&1
  if [ $? -ne 0 ]; then
    ERRORREASON=$ERRORREASON$'\n scp command failed'
    ERROR=1
  fi
  echo "BACKUP END" >> $LOG
  
  mkdir -p "$OUTPUTDIR"
  mkdir -p "$OUTPUTDIR"
fi