Toolbox
=======

These are assorted tools that can assist in developing solutions

Installing the Project
======================

The steps are as follows: 

    1. Download and install git for your platform if you don't already have it installed.
       It can be downloaded from https://git-scm.com/downloads
    
    2. Open a new shell/command prompt. It must be new since only a new shell will include the new python 
       path that was created in step 1. Cd to the folder where you want to install the scripts.
    
    3. Clone this repo using the following command. This would create a new drectory
    
    4. Change into the folder. Type the following to install all the package dependencies 
       (this may take a while as this will download all of the libraries that it uses):

        pipenv install
        
Dependencies
============

This should be minimal, if there are requirements outside of the scripts, they will be listed as a 
file to include and drive installs from.

Script Names and Purposes
=========================

    1. cidrcat.py - cheerful and easy way to enumerate a network block based on base IP and netmask
                   
To Do List:
===========

* Add extra scripts

License
=======

Copyright 2019 Wayne Kirk Schmidt

Licensed under the GNU GPL License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    license-name   GNU GPL
    license-url    http://www.gnu.org/licenses/gpl.html

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Support
=======

Feel free to e-mail me with issues to: wschmidt@sumologic.com
I will provide "best effort" fixes and extend the scripts.
