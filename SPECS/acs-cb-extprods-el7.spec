Name:		ACS-ExtProds
Version:	2016.6
Release:	1%{?dist}
Summary:	ACS CB ExtProds for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
# Source0, no need for anything else than ACS/ExtProds folder, with the downloaded sources within
Source0:	%{name}-%{version}.tar.gz
# Ant for EL7 is up to 1.9.2. ACS uses 1.9.3  # Boost for ACS is 1.41. Epel provides 1.48 # ACS uses omniORB 4.1.4. Epel provides 4.2.0, but omniORBpy compilation must be changed: Using ACS's for now
# ACS uses maven 3.2.5. Apache maven repo provides 3.2.5. Installed in pre. ACS's ACE+TAO is 6.3.0, Opensuse repo has 6.4.1

BuildArch: x86_64
# Base tools
BuildRequires: python-virtualenv epel-release git wget unzip tar bzip2 patch, ace-tao == 6.3.0, python-pip
# Packages checked
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ant boost148 omniORB-devel omniORB-doc omniORB-servers omniORB-utils omniORB, apache-maven == 3.2.5
# PyModules With lower or equal version as acs.req. Jinja2 Req: 2.7.3 vs 2.7.2. Pytz . Coverage Req: 3.7.1 vs 3.6. DocUtils Req: 0.12 vs 0.11. Linecache2 1.0.0 exact match- Traceback2 1.4.0 exact match. Scipy 0.12.1 exact match. python-six 1.9.0 exact match. 
# Diference between python-sphinx_rtd_theme 0.1.7 and 0.1.8: 4 features: https://github.com/snide/sphinx_rtd_theme#v0-1-8
# Suds Requires 0.4 vs 0.4.1. unittest2 1.1.0 includes 3 bugfixes 1.0.1 does not.
BuildRequires: python-jinja2 pytz python-coverage python-docutils python-linecache2 python2-traceback2 scipy python-six python-sphinx_rtd_theme python-suds python-unittest2 pexpect
# PyModules with higher versions than those in acs.req
#BuildRequires: python-ipython python-sphinx_rtd_theme python-unittest2
# 2016.6 New requirements. Matplotlib requires 1.2, exact match. Pychecker required 0.8.17, Epel provides 0.8.19. Gnuplot 1.8 required by ACS not found. Base provides 4.6.2
BuildRequires: python-matplotlib pychecker gnuplot
# Built by Tcltk for ACS. Missing on repos: tklib tkimg snack tkman rman tclCheck msqltcl
#Requires: tk iwidgets tclx tcllib blt tktable expect tkcon

%description
RPM Installer of ACS-CB ExtProducts %{version}. It takes the compiled files and installs them on /home/almamgr/ACS-version (symlink to /alma). 

%prep
%setup -q
# builddir = /home/user/rpmbuild/BUILDDIR # setup -q = {builddir}/ACS-ExtProds-2016.6/ExtProds/{PRODUCTS,INSTALL}

#%build

%install
# Declare Global Variables for scripts in ExtProds/INSTALL/
export ALMASW_ROOTDIR="%{buildroot}/alma"
export ALMASW_RELEASE="ACS-%{version}"

export ACE_ROOT="%{buildroot}/alma/ACS-%{version}/TAO/ACE_wrappers/build/linux"
export ACE_ROOT_DIR="%{buildroot}/alma/ACS-%{version}/TAO/ACE_wrappers/build"
export M2_HOME="%{_usr}/share/apache-maven"  # Exported by apache-maven itself, only after re-login
export JACORB_HOME="%{buildroot}/alma/ACS-%{version}/JacORB"
export PYTHON_ROOT="%{buildroot}/alma/ACS-%{version}/Python"
export OMNI_ROOT="%{buildroot}/alma/ACS-%{version}/Python/"

#Create basic folder and symlink
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
# Access and execute scripts. Each script should output the result to %{buildroot}/alma/ACS-%{version}/ 
cd %{_builddir}/%{name}-%{version}/INSTALL/
# Run scripts
./buildEclipse
./buildJacORB # Depends on TAO and Maven, which are rpms
./buildTcltk # TestPending

#install -m 0755 -D -p %{SOURCE1} %{buildroot}/home/almamgr%{name}-%{version}
%clean
cd $ALMASW_INSTDIR
find -name "*.o" | xargs rm -rf

%pre
# Install epel-maven repo
curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo
yum -y install epel-release
# Numpy 1.9.2
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/23/Everything/x86_64/os/Packages/n/numpy-1.9.2-2.fc23.x86_64.rpm
# PyModules
# Babel 1.3
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/23/Everything/x86_64/os/Packages/p/python-babel-1.3-8.fc23.noarch.rpm
# MarkUpSafe 0.23
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/24/Everything/x86_64/os/Packages/p/python-markupsafe-0.23-9.fc24.x86_64.rpm
# Pygments 2.1.3 (Requires 2.0.2). Syntax highlihter
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/updates/24/x86_64/p/python-pygments-2.1.3-1.fc24.noarch.rpm
# Sphinx 1.2.3 (Requires 1.3.1)
# Necesita: tex(upquote.sty)
#yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/22/Everything/x86_64/os/Packages/p/python-sphinx-1.2.3-1.fc22.noarch.rpm
pip install Sphinx==1.3.1 --no-dependencies
# Argparse
pip install argparse==1.3.0 --no-dependencies
# Logilab
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/24/Everything/x86_64/os/Packages/p/python-logilab-common-0.63.2-5.fc24.noarch.rpm
# Astroid 1.3.6. F24 has v1.4.5. Depends on Logilab
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/23/Everything/x86_64/os/Packages/p/python-astroid-1.3.6-5.fc23.noarch.rpm
# Distribute
pip install distribute==0.7.3 --no-dependencies
# iPython OLD 1.2.1
pip install ipython==1.2.1 --no-dependencies
# Logilab astng
pip install logilab-astng==0.24.3 --no-dependencies
# Lxml OLD (Version 2.2 is for EL5)
pip install lxml==2.2.6 --no-dependencies
# mock. EL7 has 1.0.1
pip install mock==0.6.0 --no-dependencies
# Nose. Diference 1.3.6 - 1.3.7 does not apply to linux http://nose.readthedocs.io/en/latest/news.html
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/24/Everything/x86_64/os/Packages/p/python-nose-1.3.7-7.fc24.noarch.rpm
# Pyephem 3.7.5.3 (Req 3.7.5.1) Diference: 5 Bugfixes, 3 feauters. http://rhodesmill.org/pyephem/CHANGELOG.html#version-3-7-5-1-2011-november-24
# F24 and EL7 have 3.7.6.0. Dif: 7 more Bugfixes
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/23/Everything/x86_64/os/Packages/p/pyephem-3.7.5.3-3.fc23.x86_64.rpm
# Pylint 1.4.3. F24 has 1.5.5
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/23/Everything/x86_64/os/Packages/p/pylint-1.4.3-3.fc23.noarch.rpm
# PyOpenSSL. EL7 has 0.13
pip install pyOpenSSL==0.10 --no-dependencies
# Pysnmp. EL7 has 4.2.5
pip install pysnmp==4.1.13a --no-dependencies
# Pysqlite
pip install pysqlite==2.6.0 --no-dependencies
# Python-ldap. EL7 has 2.4.15
pip install python-ldap==2.3.13 --no-dependencies
# pythonscope
pip install pythoscope==0.4.3 --no-dependencies
# snakefood
pip install snakefood==1.4 --no-dependencies
# Snowballstemmer 1.2
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/24/Everything/x86_64/os/Packages/p/python2-snowballstemmer-1.2.0-3.fc24.noarch.rpm
# Twisted. Dependencies: zope, setuptools
pip install Twisted==10.1.0
# Gcovr
pip install gcovr --no-dependencies
# Numeric 24.2
yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/24/Everything/x86_64/os/Packages/p/python-numeric-24.2-25.fc24.x86_64.rpm


# ACE-TAO RPM from OpenSUSE
echo "
[ace-tao_opensuse]
name=Latest ACE micro release (CentOS_7)
type=rpm-md
baseurl=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7/
gpgcheck=1
gpgkey=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7//repodata/repomd.xml.key
enabled=0
" > /etc/yum.repos.d/ace-tao.repo

#Local users
useradd -u 550 -U almamgr

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/

%preun
 
%postun
# Al user processes must be killed before userdel
pkill -u almamgr
userdel -r almamgr

%files
%doc
%attr(0705,almagr,almamgr) /home/almamgr/ 
%attr(0705,almagr,almamgr) /home/almamgr/ACS-%{version}/*

%changelog
* Wed Oct 26 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
