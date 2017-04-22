Name:		ACS-jacsutil
Version:	2017.02
Release:	1%{?dist}
Summary:	Java ACS util
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-jacsutil
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
ACS Community Branch Java interface for ACS util

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile
# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Env Vars for installing. Assume rest of env vars ready by Tools-Kit-Benchmark package 
source %{_sysconfdir}/profile.d/acscb.sh
export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export CLASSPATH="/usr/share/java/:/usr/share/local/java/:/usr/share/java/ant.jar:/alma/ACS-%{version}/ACSSW/lib/"

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

mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/ACSSW/
mv %{_builddir}/home/almamgr/ACS-%{version}/ACSSW %{buildroot}/home/almamgr/ACS-%{version}/ACSSW

%files
%attr(645,-,-) /home/almamgr/ACS-%{version}/ACSSW/lib/


%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
