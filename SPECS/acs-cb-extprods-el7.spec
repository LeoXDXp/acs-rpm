%define oldVersion 2016.10

Name:		ACS-ExtProds
Version:	2017.06
Release:	2%{?dist}
Summary:	ACS CB ExtProds for CentOS 7	
License:	LGPL
URL:		http://csrg-utfsm.github.io/
AutoReq:	no
# Source0, no need for anything else than ACS/ExtProds folder, with the downloaded sources within
Source0:	%{name}-%{version}.tar.gz
# Ant for EL7 is up to 1.9.2. ACS uses 1.9.3. Provided in F21  
# Boost for ACS is 1.41. Epel provides 1.48. Changes should not affect ACS: http://www.boost.org/doc/libs/1_53_0/doc/html/hash/changes.html
# ACS uses omniORB 4.2.1, in F24
# ACS uses maven 3.2.5. Apache maven repo provides 3.2.5. Installed in pre. 
# ACS's ACE+TAO is 6.3.0, Opensuse repo has 6.4.1, ACE+TAO source has rpm, and is builded succesfully, ace-tao-6.3.0.2016.6
# Small ifarch hack for x86_64 and aarch64 arch 
#Source4:	searchFile
#Source5:	JacPrep
#Source6:	acsMakeCopySources
#Source7:	acsMakeTclScript
#Source8:	acsMakeJavaClasspath
#Source9:	acserrGenIDL
#Source10:	acserrGenCpp
#Source11:	acserrGenCheckXML
#Source12:	generateTmcdbSchemas
#Source13:	generateXsdPythonBinding
#Source14:	loggingtsGenH
#Source15:	loggingtsGenCheckXML
#Source16:	acsStartJava
#Source17:	acs_python.py
#Source18:	acsMakeCheckUnresolvedSymbols
#Source19:	acsMakeTclLib

#Patch0:		Orbsvcs-TaggedComponentListSeq.patch	
# Base tools
BuildRequires: epel-release git wget unzip tar bzip2 patch gcc
# Java and Others
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo, apache-maven >= 3.2.5, boost148, ant >= 1.9.2
# Built by Tcltk for ACS. Missing on repos: tklib tkimg snack tkman rman tclCheck msqltcl tkcon
BuildRequires: tcltk-ACS JacORB-ACS mico-ACS

# ACE + TAO + ACS  Patches. Only for Requires. JacORB has own rpm
Requires: ace >= 6.3.0.%{oldVersion}, ace-devel >= 6.3.0.%{oldVersion}, ace-xml >= 6.3.0.%{oldVersion}, ace-gperf == 6.3.0.%{oldVersion}, ace-xml-devel >= 6.3.0.%{oldVersion}, ace-kokyu >= 6.3.0.%{oldVersion}, ace-kokyu-devel >= 6.3.0.%{oldVersion}, mpc >= 6.3.0.%{oldVersion}, tao >= 2.3.0.%{oldVersion}, tao-devel >= 2.3.0.%{oldVersion}, tao-utils >= 2.3.0.%{oldVersion}, tao-cosnaming >= 2.3.0.%{oldVersion}, tao-cosevent >= 2.3.0.%{oldVersion}, tao-cosnotification >= 2.3.0.%{oldVersion}, tao-costrading >= 2.3.0.%{oldVersion}, tao-rtevent >= 2.3.0.%{oldVersion}, tao-cosconcurrency >= 2.3.0.%{oldVersion}, ace-tao-debuginfo >= 6.3.0.%{oldVersion}

# OmniORB
Requires: omniORB == 4.2.1, omniORB-devel == 4.2.1, omniORB-utils == 4.2.1, omniORB-debuginfo == 4.2.1, omniORB-servers == 4.2.1, omniORB-doc == 4.2.1 python-omniORB
# Java and Others
Requires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo apache-maven >= 3.2.5, boost148 antlr-tool python-virtualenv epel-release python-pip centos-release-scl maven-local
Requires: ant >= 1.9.2, gcc, time
# PyModules exact version in repos as in acs.req: Linecache2 v1.0.0, Traceback2 v1.4.0, Scipy v0.12.1, python-six v1.9.0, Matplotlib v1.2.0,
Requires: python-coverage == 3.7.1, python-linecache2 == 1.0.0, python2-traceback2 == 1.4.0, scipy == 0.12.1, python-six == 1.9.0, pexpect, python-matplotlib == 1.2.0

# PyModules lower in repo than acs.req: Jinja2 Req: 2.7.3 vs 2.7.2. Pytz 2012d vs 2015.2, Coverage Req: 3.7.1 vs 3.6. DocUtils Req: 0.12 vs 0.11.
Requires: pytz python-jinja2 python-docutils

# PyModules with higher versions in repos than in acs.req. Suds Requires 0.4 vs 0.4.1. unittest2 1.1.0 includes 3 bugfixes 1.0.1 does not.
# Pychecker required 0.8.17, Epel provides 0.8.19. Gnuplot 1.8 required by ACS not found. Base provides 4.6.2. 
# Diference between python-sphinx_rtd_theme 0.1.7 and 0.1.8: 4 features: https://github.com/snide/sphinx_rtd_theme#v0-1-8
# python-ipython could be here: repo 3.2.1 vs acs.req 1.2.1
Requires: python-sphinx_rtd_theme python-unittest2 python-suds pychecker gnuplot man

# PyModules from rpms of F21 to F24 symlinked in acs-cb-extprod repo
# Exact version
# Pylint 1.4.3. F24 has 1.5.5
Requires: python-babel == 1.3, python-markupsafe == 0.23, python-pygments == 2.1.3, python-logilab-common == 0.63.2, python-astroid >= 1.3.6, pylint >= 1.4.3, python2-snowballstemmer == 1.2.0, python-numeric == 24.2, numpy == 1:1.9.2
# Nose. Diference 1.3.6 - 1.3.7 does not apply to linux http://nose.readthedocs.io/en/latest/news.html
# Pyephem 3.7.5.3 (Req 3.7.5.1) Diference: 5 Bugfixes, 3 features. http://rhodesmill.org/pyephem/CHANGELOG.html#version-3-7-5-1-2011-november-24
# F24 and EL7 have 3.7.6.0. Dif: 7 more Bugfixes
Requires: python-nose == 1.3.7, pyephem >= 3.7.5.3

# Devtoolset eclipse-jdt dependency in SCL
#Requires: devtoolset-3-eclipse-jdt
# Other Dependecies for stuff through pip
Requires: libxslt-devel sqlite-devel openldap-devel libxml2-devel

%description
RPM Installer of ACS-CB ExtProducts %{version}. Installs ACE+TAO with ACS Patches, omniORB, Java 1.8 OpenJDK, PyModules needed by ACS, and builds/install Eclipse 4 old libraries. Then, the compiled files are left on /home/almamgr/ACS-version (symlink to /alma). 

%package devel
Summary: ACS CB ExtProd Source files for %{?dist}
License: LGPL

%description devel
Source files to compile ExtProds for ACS CB %{version} for {?dist}

%prep
%setup -q
#%patch0 -p2
# builddir = /home/user/rpmbuild/BUILDDIR
%build
# Uncompress Eclipse4.2.2 gtk-x86_64
cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL/


%install
# Declare Global Variables for scripts in ExtProds/INSTALL/
export ALMASW_ROOTDIR="%{buildroot}/alma"
export ALMASW_RELEASE="ACS-%{version}"

export M2_HOME="%{_usr}/share/apache-maven"  # Exported by apache-maven itself, only after re-login

#Create basic folder and symlink
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/
ln -s %{buildroot}/home/almamgr %{buildroot}/alma

mkdir -p %{buildroot}/%{_usr}/local/share/Eclipse4/SDKandDeltaPack/eclipse/plugins/

# Self export var through etc profile
mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "OMNI_ROOT=/usr/share/idl/omniORB" >> %{buildroot}%{_sysconfdir}/profile.d/mico.sh
echo "export OMNI_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/mico.sh
echo "ANT_HOME=/usr/share/ant" >> %{buildroot}%{_sysconfdir}/profile.d/ant.sh
echo "export ANT_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/ant.sh
echo "SWIG_ROOT=/usr/share/swig/" >> %{buildroot}%{_sysconfdir}/profile.d/swig.sh
echo "export SWIG_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/swig.sh

echo "ALMASW_ROOTDIR=/alma" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ALMASW_ROOTDIR" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "ALMASW_RELEASE=ACS-%{version}" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export ALMASW_RELEASE" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

#echo 'CLASSPATH="/usr/share/java/:/usr/local/share/java/:$JACORB_HOME/lib:$ANT_HOME/lib:$M2_HOME/lib" ' >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

echo "CLASSPATH=$CLASSPATH:/usr/share/java/:/usr/local/share/java/:" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh
echo "export CLASSPATH" >> %{buildroot}%{_sysconfdir}/profile.d/acscb.sh

#CLASSPATH="/alma/ACS-OCT2016/JacORB/lib/jacorb-3.6.1.jar:/alma/ACS-OCT2016/JacORB/lib/jacorb-services-3.6.1.jar:/alma/ACS-OCT2016/JacORB/lib/idl.jar:/alma/ACS-OCT2016/ant/lib/ant.jar"

# Destroy Symlink
/usr/bin/unlink %{buildroot}/alma

# INSTALL and PRODUCTS to buildroot for devel package
mkdir -p %{buildroot}/home/almadevel/ACS-%{version}/ExtProd/
mv %{_builddir}/%{name}-%{version}/ExtProd/INSTALL %{buildroot}/home/almadevel/ACS-%{version}/ExtProd/
mv %{_builddir}/%{name}-%{version}/ExtProd/PRODUCTS %{buildroot}/home/almadevel/ACS-%{version}/ExtProd/
# Delete old Eclipse folder
#rm -rf %{buildroot}/home/almamgr/ACS-%{version}/Eclipse/

%clean

%pre
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

if ! id almamgr >/dev/null 2>&1; then
        useradd -u 550 -U almamgr
	usr/bin/ln -s /home/almamgr/ /alma
fi

%pre devel
if ! id almadevel >/dev/null 2>&1; then
        useradd -U almadevel
fi

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chmod 0705 /home/almamgr/
# Pyxbgen symlink to /usr/local/bin
ln -s /opt/rh/rh-java-common/root/usr/bin/pyxbgen %{_usr}/local/bin/
# ACSnc Build has trouble finding the following files

# Symlink of tao_idl because hardcoded path
mkdir -p %{_usr}/share/tao/TAO_IDL
ln -s %{_usr}/bin/tao_idl %{_usr}/share/tao/TAO_IDL/

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

# Reload Python modules. Avoids the error: from omniORB import CORBA \n omniORB not found
python -c "help('modules')"
# Updating SecurityReplaceable.idl with 2008a Changelog of TAO
sed -i 's/IOP::TaggedComponentList create_ior_components/IOP::TaggedComponentSeq create_ior_components/g' /usr/include/orbsvcs/SecurityReplaceable.idl

# TAO symlinks
mkdir -p /usr/share/ace/TAO/utils/nslist/
mkdir -p /usr/share/ace/TAO/orbsvcs/Notify_Service

ln -s %{_usr}/sbin/tao-cosnaming %{_usr}/sbin/tao_cosnaming
ln -s %{_usr}/sbin/tao-cosnotification %{_usr}/share/ace/TAO/orbsvcs/Notify_Service/tao_cosnotification
ln -s %{_usr}/bin/tao_nsadd %{_usr}/share/ace/TAO/utils/nslist/tao_nsadd
ln -s %{_usr}/bin/tao_ifr %{_usr}/share/ace/bin/tao_ifr

# Eclipse4 symlink
ln -s %{_usr}/local/share/Eclipse4/SDKandDeltaPack/eclipse/plugins/ /home/almamgr/ACS-%{version}/Eclipse4/

%preun
# Remove symlinks 
# Pyxbgen symlink to /usr/local/bin
unlink %{_usr}/local/bin/pyxbgen
# Symlink of tao_idl because hardcoded path
unlink %{_usr}/share/tao/TAO_IDL/tao_idl

unlink %{_usr}/sbin/tao_cosnaming
unlink %{_usr}/share/ace/TAO/orbsvcs/Notify_Service/tao_cosnotification
unlink %{_usr}/share/ace/TAO/utils/nslist/tao_nsadd
unlink %{_usr}/share/ace/bin/tao_ifr

unlink /home/almamgr/ACS-%{version}/Eclipse4/

# remove env vars
export CLASSPATH=$(echo $CLASSPATH | sed 's/\/usr\/share\/java/:\/usr\/local\/share\/java\///g' )
unset OMNI_ROOT
unset ANT_HOME
unset SWIG_ROOT
unset ALMASW_ROOTDIR
unset ALMASW_RELEASE

%postun
# Al user processes must be killed before userdel
pkill -u almamgr
userdel -r almamgr
/usr/bin/unlink /alma

## PyModules in acs.req file
# Sphinx 1.2.3 (Requires 1.3.1)
# Necesita: tex(upquote.sty)
#yum -y install http://ftp.inf.utfsm.cl/fedora/linux/releases/22/Everything/x86_64/os/Packages/p/python-sphinx-1.2.3-1.fc22.noarch.rpm
pip uninstall Sphinx -y
# Argparse
pip uninstall argparse -y
# Distribute
pip uninstall distribute -y
# iPython OLD 1.2.1
pip uninstall ipython -y
# Logilab astng
pip uninstall logilab-astng -y
# Lxml OLD (Version 2.2 is for EL5)
pip uninstall lxml -y
# mock. EL7 has 1.0.1
pip uninstall mock -y
# PyOpenSSL. EL7 has 0.13
pip uninstall pyOpenSSL -y
# Pysnmp. EL7 has 4.2.5
pip uninstall pysnmp -y
# Pysqlite
pip uninstall pysqlite -y
# Python-ldap. EL7 has 2.4.15
pip uninstall python-ldap -y
# pythonscope
pip uninstall pythoscope -y
# snakefood
pip uninstall snakefood -y
# Twisted. Dependencies: zope, setuptools
pip uninstall Twisted -y
# Gcovr
pip uninstall gcovr -y

%postun devel
pkill -u almadevel
userdel -r almadevel

%files
%attr(0705,-,-) %{_usr}/local/share/Eclipse4/SDKandDeltaPack/eclipse/plugins/
%config %{_sysconfdir}/profile.d/

%files devel
%attr(0705,almadevel,almadevel) /home/almadevel/ACS-%{version}/ExtProd/

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 2017.06-1
Updating version. Moving code to respective new rpms
* Sun May 28 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-2
Fixing hardcoded xalan classpath
* Wed Oct 26 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
