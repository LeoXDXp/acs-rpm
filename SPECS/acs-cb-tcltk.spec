Name:		tcltk-ACS
Version:	8.5.15.2017.02
Release:	1%{?dist}
Summary:	Tcl with 1 ACS patch, and other packages
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	ksh
Requires:	expect

%description
Tcl, tk, mini SQL, tklib, tclCheck, tclx, iwidgets, tkman, TKtable, tkimg, tcllib, blt, itcl, rman, snack

%prep
%setup -q

%build
# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export OSYSTEM="Linux"
export TCLTK_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/tcltk"

cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL

sh buildTcltk

#sh checkTcltk

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Docs
#mkdir -p %{buildroot}/%{_usr}/local/share/doc/log4cpp-ACS/
#cp -f %{_builddir}/%{name}-%{version}/LGPL/Tools/log4cpp/src/log4cpp-1.0/{AUTHORS,COPYING,INSTALL,NEWS,README,THANKS,ChangeLog} %{buildroot}/%{_usr}/local/share/doc/log4cpp-ACS/

#
mkdir -p %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.a %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.la %{buildroot}/%{_usr}/local/%{_lib}/
cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.so.4.0.6 %{buildroot}/%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6
chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.la

%post

%preun

%files
%attr(755,root,root) %{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 1.0-1
Initial Packaging
