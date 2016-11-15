%define ALTVER 2016.10

Name:		ACS-ExtProds
Version:	OCT2016
Release:	1%{?dist}
Summary:	ACS CB ExtProds for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
# Source0, no need for anything else than ACS/ExtProds folder, with the downloaded sources within
Source0:	%{name}-%{version}.tar.gz
# Ant for EL7 is up to 1.9.2. ACS uses 1.9.3. Provided in F21  
# Boost for ACS is 1.41. Epel provides 1.48. Changes should not affect ACS: http://www.boost.org/doc/libs/1_53_0/doc/html/hash/changes.html
# ACS uses omniORB 4.2.1, in F24
# ACS uses maven 3.2.5. Apache maven repo provides 3.2.5. Installed in pre. 
# ACS's ACE+TAO is 6.3.0, Opensuse repo has 6.4.1, ACE+TAO source has rpm, and is builded succesfully, ace-tao-6.3.0.2016.6

BuildArch: x86_64
# Base tools
BuildRequires: epel-release git wget unzip tar bzip2 patch
# ACE + TAO + ACS  Patches
BuildRequires: ace == 6.3.0.%{ALTVER}, ace-devel == 6.3.0.%{ALTVER}, ace-xml == 6.3.0.%{ALTVER}, ace-gperf == 6.3.0.%{ALTVER}, ace-xml-devel == 6.3.0.%{ALTVER}, ace-kokyu == 6.3.0.%{ALTVER}, ace-kokyu-devel == 6.3.0.%{ALTVER}, mpc == 6.3.0.%{ALTVER}, tao == 2.3.0.%{ALTVER}, tao-devel == 2.3.0.%{ALTVER}, tao-utils == 2.3.0.%{ALTVER}, tao-cosnaming == 2.3.0.%{ALTVER}, tao-cosevent == 2.3.0.%{ALTVER}, tao-cosnotification == 2.3.0.%{ALTVER}, tao-costrading == 2.3.0.%{ALTVER}, tao-rtevent == 2.3.0.%{ALTVER}, tao-cosconcurrency == 2.3.0.%{ALTVER}, ace-tao-debuginfo == 6.3.0.%{ALTVER} 
# Java and Others
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo, apache-maven == 3.2.5, boost148, ant == 1.9.3

# Built by Tcltk for ACS. Missing on repos: tklib tkimg snack tkman rman tclCheck msqltcl
#BuildRequires: tk iwidgets tclx tcllib blt tktable expect tkcon

# ACE + TAO + ACS  Patches
Requires: ace == 6.3.0.%{ALTVER}, ace-devel == 6.3.0.%{ALTVER}, ace-xml == 6.3.0.%{ALTVER}, ace-gperf == 6.3.0.%{ALTVER}, ace-xml-devel == 6.3.0.%{ALTVER}, ace-kokyu == 6.3.0.%{ALTVER}, ace-kokyu-devel == 6.3.0.%{ALTVER}, mpc == 6.3.0.%{ALTVER}, tao == 2.3.0.%{ALTVER}, tao-devel == 2.3.0.%{ALTVER}, tao-utils == 2.3.0.%{ALTVER}, tao-cosnaming == 2.3.0.%{ALTVER}, tao-cosevent == 2.3.0.%{ALTVER}, tao-cosnotification == 2.3.0.%{ALTVER}, tao-costrading == 2.3.0.%{ALTVER}, tao-rtevent == 2.3.0.%{ALTVER}, tao-cosconcurrency == 2.3.0.%{ALTVER}, ace-tao-debuginfo == 6.3.0.%{ALTVER}

# OmniORB
Requires: omniORB == 4.2.1, omniORB-devel == 4.2.1, omniORB-utils == 4.2.1, omniORB-debuginfo == 4.2.1, omniORB-servers == 4.2.1, omniORB-doc == 4.2.1
# Java and Others
Requires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo, apache-maven == 3.2.5, boost148, ant == 1.9.3, python-virtualenv epel-release python-pip centos-release-scl

# PyModules exact version in repos as in acs.req: Linecache2 v1.0.0, Traceback2 v1.4.0, Scipy v0.12.1, python-six v1.9.0, Matplotlib v1.2.0,
Requires: python-coverage == 3.7.1, python-linecache2 == 1.0.0, python2-traceback2 == 1.4.0, scipy == 0.12.1, python-six == 1.9.0, pexpect, python-matplotlib == 1.2.0

# PyModules lower in repo than acs.req: Jinja2 Req: 2.7.3 vs 2.7.2. Pytz 2012d vs 2015.2, Coverage Req: 3.7.1 vs 3.6. DocUtils Req: 0.12 vs 0.11.
Requires: pytz python-jinja2 python-docutils

# PyModules with higher versions in repos than in acs.req. Suds Requires 0.4 vs 0.4.1. unittest2 1.1.0 includes 3 bugfixes 1.0.1 does not.
# Pychecker required 0.8.17, Epel provides 0.8.19. Gnuplot 1.8 required by ACS not found. Base provides 4.6.2. 
# Diference between python-sphinx_rtd_theme 0.1.7 and 0.1.8: 4 features: https://github.com/snide/sphinx_rtd_theme#v0-1-8
# python-ipython could be here: repo 3.2.1 vs acs.req 1.2.1
Requires: python-sphinx_rtd_theme python-unittest2 python-suds pychecker gnuplot

# PyModules from rpms of F21 to F24 symlinked in acs-cb-extprod repo
# Exact version
# Pylint 1.4.3. F24 has 1.5.5
Requires: numpy == 1.9.2, python-babel == 1.3, python-markupsafe == 0.23, python-pygments == 2.1.3, python-logilab-common == 0.63.2, python-astroid == 1.3.6, pylint == 1.4.3, python2-snowballstemmer == 1.2.0, python-numeric == 24.2
# Nose. Diference 1.3.6 - 1.3.7 does not apply to linux http://nose.readthedocs.io/en/latest/news.html
# Pyephem 3.7.5.3 (Req 3.7.5.1) Diference: 5 Bugfixes, 3 features. http://rhodesmill.org/pyephem/CHANGELOG.html#version-3-7-5-1-2011-november-24
# F24 and EL7 have 3.7.6.0. Dif: 7 more Bugfixes
Requires: python-nose == 1.3.7, pyephem == 3.7.5.3

%description
RPM Installer of ACS-CB ExtProducts %{version}. It installs ACE+TAO with ACS Patches, omniORB, Java 1.8 OpenJDK, PyModules needed by ACS, and builds/install Eclipse 3 and 4 old libraries, JacORB, Tctlk and MicoORB. Then, the compiled files are left on /home/almamgr/ACS-version (symlink to /alma). 

%prep
%setup -q
# builddir = /home/user/rpmbuild/BUILDDIR # setup -q = {builddir}/ACS-ExtProds-2016.6/ExtProds/{PRODUCTS,INSTALL}
#%build

%install
# Declare Global Variables for scripts in ExtProds/INSTALL/
export ALMASW_ROOTDIR="%{buildroot}/alma"
export ALMASW_RELEASE="ACS-%{version}"

export M2_HOME="%{_usr}/share/apache-maven"  # Exported by apache-maven itself, only after re-login
export JACORB_HOME="%{buildroot}/alma/ACS-%{version}/JacORB"

#Create basic folder and symlink
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
# Access and execute scripts. Each script should output the result to %{buildroot}/alma/ACS-%{version}/ 
cd %{_builddir}/%{name}-%{version}/INSTALL/
# Run scripts
./buildEclipse
./buildJacORB # Depends on TAO and Maven, which are rpms
./buildTcltk # TestPending. Uses gcc, make, tar
./buildMico # TestPending. Uses gcc, make , tar

# Self export var through etc profile
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "JACORB_HOME=/home/almamgr/ACS-%{version}/JacORB" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb.sh
echo "export JACORB_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb.sh
echo "MICO_HOME=/home/almamgr/ACS-%{version}/mico" >> %{buildroot}%{_sysconfdir}/profile.d/mico.sh
echo "export MICO_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/mico.sh


#install -m 0755 -D -p %{SOURCE1} %{buildroot}/home/almamgr%{name}-%{version}
%clean
cd $ALMASW_INSTDIR
find -name "*.o" | xargs rm -rf

%pre
# Install epel-maven repo
curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo
yum -y install epel-release
# Install acs-cb and acs-cb extprod repo #
echo -n"
[acs-cb]
name=Alma Common Software for Enterprise Linux 7 - $basearch
baseurl=http://repo.csrg.cl/$basearch/acscb/
enabled=0
gpgcheck=0
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ACS-CB-EL7

[acs-cb-extprod]
name=Alma Common Software Compiling/Base Packages for Enterprise Linux 7 - $basearch
baseurl=http://repo.csrg.cl/$basearch/extprod/
enabled=1
gpgcheck=0
#gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-ACS-CB-EL7
" > /etc/yum.repos.d/acs-cb.repo

## PyModules in acs.req file
# Sphinx 1.2.3 (Requires 1.3.1)
# Necesita: tex(upquote.sty)
#yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/22/Everything/x86_64/os/Packages/p/python-sphinx-1.2.3-1.fc22.noarch.rpm
pip install Sphinx==1.3.1 --no-dependencies
# Argparse
pip install argparse==1.3.0 --no-dependencies
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
# Twisted. Dependencies: zope, setuptools
pip install Twisted==10.1.0
# Gcovr
pip install gcovr --no-dependencies

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
%config %{_sysconfdir}/profile.d/jacorb.sh

%changelog
* Wed Oct 26 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
