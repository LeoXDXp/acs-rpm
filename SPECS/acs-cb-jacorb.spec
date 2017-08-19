Name:		JacORB-ACS
Version:	3.6.1.2017.06
Release:	1%{?dist}
Summary:	JacORB 3.6.1 for ACS
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
#Source1:	buildTclTk-OCT2013
BuildRequires:	gcc, make, tar
#Requires:	expect tk iwidgets tclx tcllib blt tktable
#Requires:	telnet, libX11
#AutoReq:	no

%description
JacORB 3.6.1 with ACS patches

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
export JACORB_HOME="$ALMASW_ROOTDIR/$ALMASW_RELEASE/JacORB"

cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL
curl -o %{_builddir}/%{name}-%{version}/ExtProd/PRODUCTS/jacorb-3.6.1-source.zip http://www.jacorb.org/releases/3.6.1/jacorb-3.6.1-source.zip

sh buildJacORB

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Docs
#mkdir -p %{buildroot}/%{_usr}/local/share/doc/%{name}/
#cp -rf %{_builddir}/%{name}-%{version}/tcltk/doc/tkcon/ %{buildroot}/%{_usr}/local/share/doc/%{name}/

mkdir -p %{buildroot}/home/acs-jacorb/
cd %{_builddir}/home/almamgr/%{name}-%{version}/JacORB/
find lib/ -name *.so | xargs chmod 755 $1
cp -rf %{_builddir}/home/almamgr/%{name}-%{version}/JacORB/ %{buildroot}/home/acs-jacorb/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "JACORB_HOME=/home/acs-jacorb/JacORB/" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export JACORB_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh

#mkdir -p %{buildroot}/%{_usr}/local/%{_lib}/
#cp -f %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/lib/liblog4cpp.a %{buildroot}/%{_usr}/local/%{_lib}/
#chmod 755 %{buildroot}/%{_usr}/local/%{_lib}/liblog4cpp.so.4.0.6

%pre
useradd -U acs-jacorb

%post
# tclCheck symlink to /usr/local/bin
#ln -s /home/almamgr/ACS-%{version}/tcllk/bin/tclCheck %{_usr}/local/bin/
#ln -s /home/almamgr/ACS-%{version}/tcltk/bin/tcl %{_usr}/local/bin/
#ln -s /home/acs-tcltk/bin/tclsh8.5 /home/acs-tcltk/bin/tclsh
#ln -s /home/acs-tcltk/bin/wish8.5 /home/acs-tcltk/bin/wish

#ln -s /home/acs-tcltk/lib/iwidgets4.0.2 /home/acs-tcltk/lib/iwidgets
#ln -s /home/acs-tcltk/lib/libBLT25.a /home/acs-tcltk/lib/libBLT.a
#ln -s /home/acs-tcltk/lib/libBLTlite25.a /home/acs-tcltk/lib/libBLTlite.a
#ln -s /home/acs-tcltk/lib/libBLT25.so /home/acs-tcltk/lib/libBLT.so
#ln -s /home/acs-tcltk/lib/tclx8.4/libtclx8.4.a /home/acs-tcltk/lib/libtclx8.4.a
#ln -s /home/acs-tcltk/lib/tclx8.4/libtclx8.4.so /home/acs-tcltk/lib/libtclx8.4.so

%postun
# Al user processes must be killed before userdel
pkill -u acs-jacorb
userdel -r acs-jacorb

%files
%attr(755,acs-jacorb,acs-jacorb) /home/acs-jacorb/JacORB/
%{_sysconfdir}/profile.d/jacorb-acs.sh

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
