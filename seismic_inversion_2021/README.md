# 2021 Seismic Inversion Challenge

Please visit the website for competition details: https://www.geoscienceml.org/

# Scoreboard - April 26 - 3:30PM

| **Team Name**        | **Score Type**        | **Date**                 | **Score (R<sup>2</sup>)** |
|:---------------------|:---------------------:|:------------------------:|:-------------------------:|
| Team3ctsu | Intermediate07 | 4/26/2021 | 0.789302 |
| TeamCowboy | Intermediate13b | 4/26/2021 | 0.781131 |
| TeamKT | Intermediate06 | 4/25/2021 | 0.737037 |
| FYY | Intermediate02 | 4/26/2021 | 0.714284 |
| TeamGeoCloud | Intermediate06 | 4/26/2021 | 0.714178 |
| Tongseng | Intermediate01 | 4/26/2021 | 0.706852 |
| TeamQI | Intermediate04 | 4/26/2021 | 0.704526 |
| 7seas | Intermediate03 | 4/26/2021 | 0.683267 |
| SLBIF | Intermediate04 | 4/25/2021 | 0.681461 |
| TAMUSEG | Intermediate05 | 4/26/2021 | 0.647979 |
| seismicboosters | Intermediate | 4/23/2021 | 0.574381 |
| UsefulModel | Intermediate03 | 4/26/2021 | 0.482949 |
| GeoGeeks | Intermediate02 | 4/26/2021 | 0.192619 |
| CREWES | Intermediate03 | 4/25/2021 | 0.161849 |
| Maquina | Intermediate06 | 4/23/2021 | 0.014714 |
| NeverStop | Intermediate1 | 4/25/2021 | -0.026146 |
| Mictlan | Intermediate01 | 4/25/2021 | -1.051279 |



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



