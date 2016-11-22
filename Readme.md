ACS and ACS ExtProd RPM in branch master
ACE+TAO 6.3.0-ACS_VERSION RPM in ace-tao branch. It has ACS patches applied to the source.
All has been thought for CentOS 7 and above.

# Repository
A repo (and the .repo file for /etc/yum.repos.d/) can be found in http://repo.csrg.cl.
It contains the exact version packages required in ACS and ExtProd in the form of rpms, which have been colected
from Fedora 21 to 24, OpenSuse and JPP6 (JPackage Project), among other rpm sources.

#Issues
Some issues in ACS ExtProd with Rpaths due to Eclipse libs and TcTlk build. Both leave libs on "non-system" folders.
https://fedoraproject.org/wiki/RPath_Packaging_Draft

A temp fix done for the moment was to comment out the section %__arch_install_post (last 4 lines) 
in the .rpmmacro file in /home/<user used to build-rebuild rpm>

#Pending:
- Sign the RPMs: http://giovannitorres.me/how-to-setup-an-rpm-signing-key.html
- Complete the SysV daemons of acs commands (used in a Pacemaker PoC) and migrate them to SystemD
