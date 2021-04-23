# 2021 Seismic Inversion Challenge

Please visit the website for competition details: https://www.geoscienceml.org/

# Scoreboard - April 23

| **Team Name**        | **Score Type**        | **Date**                 | **Score (R<sup>2</sup>)** |
|:---------------------|:---------------------:|:------------------------:|:-------------------------:|
| TeamCowboy           | Intermediate03        | 2021-04-23               | 0.749855                  |
| TeamCowboy           | Intermediate05        | 2021-04-23               | 0.744141                  |
| TeamQI               | Intermediate          | 2021-04-22               | 0.682238                  |
| TeamQI               | Intermediate          | 2021-04-21               | 0.680140                  |
| TeamQI               | Intermediate          | 2021-04-23               | 0.674240                  |
| 7seas                | Intermediate02        | 2021-04-22               | 0.614438                  |
| seismicboosters      | Intermediate          | 2021-04-23               | 0.574381                  |
| Maquina              | Intermediate02        | 2021-04-23               | -0.333030                  |

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



