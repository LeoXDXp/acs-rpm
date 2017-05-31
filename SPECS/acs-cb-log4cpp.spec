Name:		log4cpp-ACS
Version:	1.0.2017.02
Release:	1%{?dist}
Summary:	Old version of log4cpp with ACS patches
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-log4cpp
Source2:	MakefileTools-log4cpp

%description
Log for C++ is a library of classes for flexible logging to files, syslog,
and other destinations. It is modeled after the Log for Java library and
stays as close to its API as is reasonable.
This package is patched for ACS. Patch modifies messages and levels.

%package devel
Summary: development tools for Log for C++ with ACS patch
Group: Development/Libraries
#Requires: %name = %version

%description devel
The %{name}-devel package contains the static libraries and header files
needed for development with %{name}.

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile
cp -f %{SOURCE2} %{_builddir}/%{name}-%{version}/LGPL/Tools/Makefile
# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# Env Vars for installing. 
#source %{_sysconfdir}/profile.d/acscb.sh
#source %{_sysconfdir}/profile.d/acscb-gnu.sh

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export OSYSTEM="Linux"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
#mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Docs
mkdir -p %{buildroot}/%{_usr}/local/share/doc/log4cpp-ACS/
cp -f %{_builddir}/%{name}-%{version}/LGPL/Tools/log4cpp/src/log4cpp-1.0/{AUTHORS,COPYING,INSTALL,NEWS,README,THANKS,ChangeLog} %{buildroot}/%{_usr}/local/share/doc/log4cpp-ACS/

# 
mkdir -p %{buildroot}/%{_usr}/local/share/java/
mv %{_builddir}/%{name}-%{version}/LGPL/Tools/log4cpp/lib/log4cpp.jar %{buildroot}/%{_usr}/local/share/java/log4cpp-ACS.jar

# Devel Stuff

%files
%attr(755,root,root) %prefix/lib/lib*.so.*
%doc %{_usr}/local/share/doc/log4cpp-ACS/

%files devel
%defattr(-,root,root,755)
%prefix/include/*
%prefix/man/*
%attr(755,root,root) %prefix/bin/log4cpp-config
%attr(755,root,root) %prefix/lib/lib*.so
%attr(644,root,root) %prefix/lib/*.*a
%attr(644,root,root) %prefix/lib/pkgconfig/log4cpp.pc
#%attr(644,root,root) %prefix/share/aclocal/*.m4

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
