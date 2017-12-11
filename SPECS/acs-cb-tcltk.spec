Name:		tcltk-ACS
Version:	8.5.15.2017.06
Release:	2%{?dist}
Summary:	Tcl with 1 ACS patch, and other packages
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
#Source1:	buildTclTk-OCT2013
BuildRequires:	ksh, libX11-devel, gcc, make, tar
#Requires:	expect tk iwidgets tclx tcllib blt tktable
Requires:	telnet, libX11
AutoReq:	no

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

mkdir -p %{buildroot}/%{_usr}/local/share/tcltk
cd %{_builddir}/home/almamgr/%{name}-%{version}/tcltk/
find lib/ -name *.so | xargs chmod 755 $1
cp -rf %{_builddir}/home/almamgr/%{name}-%{version}/tcltk/ %{buildroot}/%{_usr}/local/share/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "TCLTK_ROOT=%{_usr}/local/share/tcltk/" >> %{buildroot}%{_sysconfdir}/profile.d/tcltk-acs.sh
echo "export TCLTK_ROOT" >> %{buildroot}%{_sysconfdir}/profile.d/tcltk-acs.sh
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{_usr}/local/share/tcltk/lib/" >> %{buildroot}%{_sysconfdir}/profile.d/tcltk-acs.sh
echo "export LD_LIBRARY_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/tcltk-acs.sh
echo "PATH=$PATH:%{_usr}/bin/:%{_usr}/local/bin:%{_usr}/local/share/tcltk/bin/" >> %{buildroot}%{_sysconfdir}/profile.d/tcltk-acs.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/tcltk-acs.sh

%post
# /include to usr/local/include. Not yet, as no packages use tcltk headers to compile
ln -s /usr/local/share/tcltk/bin/tcl /usr/local/bin/seqSh
ln -s /usr/bin/wish /usr/local/bin/seqWish

%preun
export LD_LIBRARY_PATH=$(echo $LD_LIBRARY_PATH | sed 's/\%{_usr}\/local\/share\/tcltk\/lib\///g' )
export PATH=$( echo $PATH | sed 's/\%{_usr}\/local\/share\/tcltk\/bin\///g' )
unset TCLTK_ROOT
unlink /usr/local/bin/seqSh
unlink /usr/local/bin/seqWish

%files
%attr(755,-,-) %{_usr}/local/share/tcltk/
%{_sysconfdir}/profile.d/tcltk-acs.sh

%changelog
* Thu Sep 28 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 8.5.15.2017.06-2
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 8.5.15.2017.06-1
Updating version
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 1.0-1
Initial Packaging
