Name:		tcltk-ACS
Version:	1.0.2017.02
Release:	1%{?dist}
Summary:	tcltk with ACS patch
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-tcltk
Source2:	MakefileTools-tcltk

%description

#%package devel
#Summary: development tools for Log for C++ with ACS patch
#Group: Development/Libraries
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
#
mkdir -p %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.a %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.la %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.so.4.0.6 %{buildroot}/%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6
chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.la

# Devel Stuff
mkdir -p %{buildroot}/%{_usr}/local/include/log4cpp/threading
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/include/log4cpp/*.h* %{buildroot}/%{_usr}/local/include/log4cpp/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/include/log4cpp/threading/*.h* %{buildroot}/%{_usr}/local/include/log4cpp/threading/

%post

%preun


%files
%attr(755,root,root) %{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6

#%files devel
#%defattr(-,root,root,755)

%changelog
* Sat Aug 04 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 1.0-1
Initial Packaging
