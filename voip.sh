#!/bin/bash
dir="/backup/voip"
y=`date +%Y -d "-1 day"`
ym=`date +%Y-%m -d "-1 day"`
ymd=`date +%Y-%m-%d -d "-1 day"`
echo $y
echo $ym
echo $ymd
echo $dir/$y/$ym/$ymd/
mkdir -p $dir/$y/$ym/$ymd/
mv $dir/*$ymd* $dir/$y/$ym/$ymd/
