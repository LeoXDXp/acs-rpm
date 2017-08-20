Name:		mico-ACS
Version:	2.3.13.2017.06
Release:	1%{?dist}
Summary:	Mico 2.3.13 for ACS
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	gcc, make, tar, wget
#Requires:	expect tk iwidgets tclx tcllib blt tktable
#Requires:	telnet, libX11
#AutoReq:	no

%description
Mico 2.3.13 with ACS patches

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
export MICO_HOME="$ALMASW_ROOTDIR/$ALMASW_RELEASE/mico"

cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL
wget -c -O %{_builddir}/%{name}-%{version}/ExtProd/PRODUCTS/mico-2.3.13.tar.gz "http://downloads.sourceforge.net/project/mico/mico%202.3.13/mico-2.3.13.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fmico%2F&ts=1405541822&use_mirror=ufpr"

sh buildMico

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
mkdir -p %{buildroot}/%{_usr}/local/share/mico
cd %{_builddir}/home/almamgr/%{name}-%{version}/mico/
find lib/ -name *.so | xargs chmod 755 $1
find lib/ -name *.a | xargs chmod 755 $1
cp -rf %{_builddir}/home/almamgr/%{name}-%{version}/mico/ %{buildroot}/%{_usr}/local/share/mico

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "MICO_HOME=%{_usr}/local/share/mico" >> %{buildroot}%{_sysconfdir}/profile.d/mico-acs.sh
echo "export MICO_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/mico-acs.sh
echo "LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{_usr}/local/share/mico/lib/" >> %{buildroot}%{_sysconfdir}/profile.d/mico-acs.sh
echo "export LD_LIBRARY_PATH" >> %{buildroot}%{_sysconfdir}/profile.d/mico-acs.sh
echo "PATH=$PATH:%{_usr}/local/share/mico/bin/" >> %{buildroot}%{_sysconfdir}/profile.d/mico-acs.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/mico-acs.sh

# No include symlink to local/include, as no packages use tcltk headers to compile
%files
%attr(755,-,-) %{_usr}/local/share/mico
%{_sysconfdir}/profile.d/mico-acs.sh

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 2.3.13.2017.06-1
Initial Packaging
