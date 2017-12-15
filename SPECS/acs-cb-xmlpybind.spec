Name:		ACS-xmlpybind
Version:	2017.06
Release:	1%{?dist}
Summary:	ACS XML Python Interface
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-xmlpybind
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}
Obsoletes:	xmlpybind

%description
ACS Community Branch Python interface for XML

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Env Vars for installing. 
source %{_sysconfdir}/profile.d/acscb.sh
source %{_sysconfdir}/profile.d/acscb-toolsKit.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/acscb-python.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
#export CLASSPATH=":/usr/share/java/ant.jar:/usr/share/java/castor/castor-xml.jar:/usr/share/java/castor/castor-xml-schema.jar:/usr/share/java/castor/castor-codegen.jar:/usr/share/java/castor/castor-core.jar:/home/almamgr/ACS-2017.02/ACSSW/lib/jACSUtil.jar:"
export PATH="$PATH:%{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/"

# Remove acsMakeJavaClasspath
echo '#!/usr/bin/env perl' > %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
echo 'print $ENV{CLASSPATH}' >> %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath
chmod +x %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/src/acsMakeJavaClasspath

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# TAT Stuff. Symlink to libtatlib.tcl/ folder
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/lib/
ln -s /home/almamgr/ACS-%{version}/ACSSW/lib/libtatlib.tcl/ %{_builddir}/%{name}-%{version}/LGPL/acsBUILD/lib/
export HOST="$HOSTNAME"
export VLTDATA=""
export OSYSTEM="Linux"
export CYGWIN_VER=""
#Needed to find nosetests, which is in /usr/bin/nosetests
export PYTHON_ROOT="/usr"
#Extending PythonPath to find own products. Can be expanded to <acs-core-component>/src or <acs-core-component>/lib/python/site-packages/
export PYTHONPATH="$PYTHONPATH:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/lib/python/site-packages/"
make test

%install

#mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/xmlpybind/
mkdir -p %{buildroot}%{_usr}/local/bin
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
# Copy EntitybuilderSettings.py and __init__
cp -r %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/lib/python/site-packages/xmlpybind/ %{buildroot}%{_usr}/local/lib/python/site-packages/
# generateXsdPythonBinding
cp %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/bin/generateXsdPythonBinding %{buildroot}%{_usr}/local/bin/

# Remove objects
cd 
find -name "*.pyo" | xargs rm -rf

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
%{_usr}/local/lib/python/site-packages/xmlpybind/xmlpybind-build.log
%{_usr}/local/lib/python/site-packages/xmlpybind/EntitybuilderSettings.py*
%{_usr}/local/lib/python/site-packages/xmlpybind/__init__.py*
%{_usr}/local/bin/generateXsdPythonBinding

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
