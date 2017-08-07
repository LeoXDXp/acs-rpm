Name:		tcltk-ACS
Version:	8.5.15.2017.02
Release:	1%{?dist}
Summary:	Tcl with 1 ACS patch, and other packages
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
#Source1:	buildTclTk-OCT2013
BuildRequires:	ksh, libX11-devel, gcc, make, tar
#Requires:	expect tk iwidgets tclx tcllib blt tktable

%description
Tcl, mini SQL, tklib, tclCheck, tkman, tkimg,  itcl, rman, snack, tkcon

%prep
%setup -q

%build
# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=%{name}-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export OSYSTEM="Linux"
export TCLTK_ROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/tcltk"

cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL

sh buildTcltk

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Docs
#mkdir -p %{buildroot}/%{_usr}/local/share/doc/%{name}/
#cp -rf %{_builddir}/%{name}-%{version}/tcltk/doc/tkcon/ %{buildroot}/%{_usr}/local/share/doc/%{name}/

mkdir -p %{buildroot}/home/acs-tcltk/
cp -rf %{_builddir}/home/almamgr/%{name}-%{version}/tcltk/ %{buildroot}/home/acs-tcltk/

echo "TCLTK_ROOT=/home/acs-tcltk/tcltk/" >> %{_sysconfdir}/profile.d/tcltk-acs.sh
echo "export TCLTK_ROOT" >> %{_sysconfdir}/profile.d/tcltk-acs.sh
chmod bin
chmod so

#mkdir -p %{buildroot}/%{_usr}/local/%{_lib}/
#cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.a %{buildroot}/%{_usr}/local/%{_lib}/
#chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6

%pre
useradd -U acs-tcltk

%post
# tclCheck symlink to /usr/local/bin
#ln -s /home/almamgr/ACS-%{version}/tcllk/bin/tclCheck %{_usr}/local/bin/
#ln -s /home/almamgr/ACS-%{version}/tcltk/bin/tcl %{_usr}/local/bin/

%postun
# Al user processes must be killed before userdel
pkill -u acs-tcltk
userdel -r acs-tcltk

%files
%attr(755,acs-tcltk,acs-tcltk) /home/acs-tcltk/tcltk/
%{_sysconfdir}/profile.d/tcltk-acs.sh

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 1.0-1
Initial Packaging
