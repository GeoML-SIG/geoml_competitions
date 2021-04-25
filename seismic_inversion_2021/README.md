# 2021 Seismic Inversion Challenge

Please visit the website for competition details: https://www.geoscienceml.org/

# Scoreboard - April 25 - 6:00PM

| **Team Name**        | **Score Type**        | **Date**                 | **Score (R<sup>2</sup>)** |
|:---------------------|:---------------------:|:------------------------:|:-------------------------:|
|TeamCowboy|	Intermediate11b|	4/25/2021|	0.777481|
|TeamCowboy|	Intermediate11a|	4/25/2021|	0.771603|
|TeamCowboy|	Intermediate10|	4/24/2021|	0.770885|
|TeamCowboy|	Intermediate09|	4/24/2021|	0.766452|
|TeamCowboy|	Intermediate08|	4/24/2021|	0.750102|
|TeamCowboy|	Intermediate03|	4/23/2021|	0.749855|
|Team3ctsu|	Intermediate01|	4/25/2021|	0.744328|
|TeamCowboy|	Intermediate05|	4/23/2021|	0.744141|
|TeamCowboy|	Intermediate07|	4/23/2021|	0.74095|
|TeamKT|	Intermediate|	4/24/2021|	0.723424|
|TeamKT|	Intermediate04|	4/25/2021|	0.714812|
|TeamGeoCloud|	Intermediate03|	4/24/2021|	0.710123|
|TeamKT|	Intermediate05|	4/25/2021|	0.709756|
|TeamKT|	Intermediate02|	4/24/2021|	0.707046|
|TeamKT|	Intermediateb|	4/24/2021|	0.706418|
|TeamGeoCloud|	Intermediate04|	4/25/2021|	0.693235|
|TeamGeoCloud|	Intermediate|	4/24/2021|	0.690093|
|TeamGeoCloud|	Intermediate02|	4/24/2021|	0.690093|
|TeamKT|	Intermediate03|	4/24/2021|	0.685018|
|TeamQI|	Intermediate|	4/22/2021|	0.682238|
|TeamQI|	Intermediate|	4/21/2021|	0.68014|
|TeamQI|	Intermediate04|	4/25/2021|	0.678346|
|TeamQI|	Intermediate|	4/24/2021|	0.677533|
|TeamQI|	Intermediate03|	4/25/2021|	0.674276|
|TeamQI|	Intermediate|	4/23/2021|	0.67424|
|TeamQI|	Intermediate05|	4/25/2021|	0.671527|
|TeamQI|	Intermediate02|	4/25/2021|	0.666454|
|SLBIF|	Intermediate03|	4/25/2021|	0.657024|
|TeamQI|	Intermediate06|	4/25/2021|	0.649368|
|7seas|	Intermediate02|	4/22/2021|	0.614438|
|SLBIF|	Intermediate|	4/25/2021|	0.596641|
|SLBIF|	Intermediate01|	4/25/2021|	0.596641|
|seismicboosters|	Intermediate|	4/23/2021|	0.574381|
|7seas|	Intermediate03|	4/25/2021|	0.500655|
|TeamQI|	Intermediate01|	4/25/2021|	0.494481|
|7seas|	Intermediate01|	4/25/2021|	0.484969|
|7seas|	Intermediate02|	4/25/2021|	0.473945|
|SLBIF|	Intermediate|	4/25/2021|	0.463192|
|SLBIF|	Intermediate02|	4/25/2021|	0.463192|
|GeoGeeks|	Intermediate|	4/26/2021|	0.277521|
|7seas|	Intermediate01|	4/23/2021|	0.263788|
|Maquina|	Intermediate02|	4/23/2021|	-0.33303|
|Maquina|	Intermediate01|	4/23/2021|	-0.582522|
|Mictlan|	Intermediate01|	4/25/2021|	-1.051279|
|Mictlan|	Intermediate02|	4/25/2021|	-1.093139|
|Tongseng|	Intermediate02|	4/25/2021|	-1.58004|
|Tongseng|	Intermediate|	4/25/2021|	-1.58004|



# Installation Guide

This is the installation guide for the serverless data available through 
the GSH Geophysics on the cloud challenge. SEGY, rss and OpenVDS data is available:

`s3://sagemaker-gitc2021/poseidon/seismic/`

SEGY can be read directly using boto3 or s3fs, rss and OpenVDS+ require additional 
python libraries to access.

Well and horizon data are located here:

`s3://sagemaker-gitc2021/poseidon/horizons`

`s3://sagemaker-gitc2021/poseidon/wells`

# RSS - Python Installation

## Windows, OSX, Ubuntu, ....  Python 3.6, 3.8, 3.9

pip install real-simple-seismic

# OpenVDS - Python Installation

[Download] https://bluware.com/downloads/download-openvds/

## Windows - Working Conda + Python 3.8

Download the Windows OpenVDS+ wheel file and unzip it. 

From the power shell (inside VsCode for example) run:
pip install .\openvds+-2.0.2\openvds-2.0.2-cp38-cp38-win_amd64.whl

This has been tested by multiple users and appears to work.

## Redhat/Centos 7 -  Untested Requires Python 3.6

## Ubuntu - Issues Conda + Python 3.8

Download the Ubuntu OpenVDS+ wheel file and untar it

tar -zxvf openvds+-2.0.2-ubuntu-20.04.tar.gz\
pip install openvds+-2.0.2/openvds-2.0.2-cp38-cp38-linux-x86_64.whl

## Issues:
import openvds\
throws some errors around missing libraries, which can be fixed by installing 
the libraries with apt or conda, for the apt examples:

sudo apt upgrade apt\
sudo apt-get install -y libgomp1\
sudo apt-get install -y libboost1.71-all-dev

or,\
conda install -c anaconda libgomp\
conda install -c conda-forge boost

The final issues comes from the version of libssl.

### Warning this may screw up your conda install

import openvds\
libssl.so.1.1: undefined symbol EVP_idea_cba, version OPENSSL_1_1_0

A work around here is to copy system libssl.a, libssl.so, libssl.1.1 into:\
~/miniconda3/lib\
Assuming conda is installed in the default location.

This seems to work, but it's unclear how stable this solution is going to be.



