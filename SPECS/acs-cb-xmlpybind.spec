Name:		ACS-xmlpybind
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS XML Python Interface
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-xmlpybind
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

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
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/acscb-tcltk.sh
#source %{_sysconfdir}/profile.d/ant.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
#export CLASSPATH=":/usr/share/java/ant.jar:/usr/share/java/castor/castor-xml.jar:/usr/share/java/castor/castor-xml-schema.jar:/usr/share/java/castor/castor-codegen.jar:/usr/share/java/castor/castor-core.jar:/home/almamgr/ACS-2017.02/ACSSW/lib/jACSUtil.jar:"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# Remove objects
cd %{_builddir}/alma/ACS-%{version}/ACSSW/
find -name "*.o" | xargs rm -rf

%install

mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/xmlpybind/
# Copy Build log as evidence
mv %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/NORM-BUILD-OUTPUT  %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/
# Copy EntitybuilderSettings.py
mv %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/xmlpybind/  %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/NORM-BUILD-OUTPUT
/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/xmlpybind/EntitybuilderSettings.py
/home/almamgr/ACS-%{version}/ACSSW/Sources/xmlpybind/src/xmlpybind/__init__.py

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
