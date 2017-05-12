Name:		ACS-xmljbind
Version:	2017.02
Release:	1%{?dist}
Summary:	Java ACS util
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-xmljbind
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} ACS-jacsutil >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version} ACS-jacsutil >= %{version}

%description
ACS Community Branch Java interface for XML

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
source %{_sysconfdir}/profile.d/ant.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export CLASSPATH="/usr/share/java/ant.jar:/usr/share/java/castor/castor-xml.jar:/usr/share/java/castor/castor-xml-schema.jar:/usr/share/java/castor/castor-codegen.jar:/home/almamgr/ACS-2017.02/ACSSW/lib/jACSUtil.jar:"

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

mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/lib
mv %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/*.jar %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/lib/

# Clean symlink in builddir
unlink %{_builddir}/alma

%files
#/home/almamgr/ACS-%{version}/ACSSW/lib/jhall-2.0_05.jar

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
