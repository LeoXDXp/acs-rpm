%define oldVersion 2016.10

Name:		JacORB-ACS
Version:	3.6.1.2017.06
Release:	1%{?dist}
Summary:	JacORB 3.6.1 for ACS
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
#Source1:	buildTclTk-OCT2013
BuildRequires:	gcc, make, tar, apache-maven >= 3.2.5, ace >= 6.3.0.%{oldVersion}, ace-devel >= 6.3.0.%{oldVersion}, ace-xml >= 6.3.0.%{oldVersion}, ace-gperf == 6.3.0.%{oldVersion}, ace-xml-devel >= 6.3.0.%{oldVersion}, ace-kokyu >= 6.3.0.%{oldVersion}, ace-kokyu-devel >= 6.3.0.%{oldVersion}, mpc >= 6.3.0.%{oldVersion}, tao >= 2.3.0.%{oldVersion}, tao-devel >= 2.3.0.%{oldVersion}, tao-utils >= 2.3.0.%{oldVersion}, tao-cosnaming >= 2.3.0.%{oldVersion}, tao-cosevent >= 2.3.0.%{oldVersion}, tao-cosnotification >= 2.3.0.%{oldVersion}, tao-costrading >= 2.3.0.%{oldVersion}, tao-rtevent >= 2.3.0.%{oldVersion}, tao-cosconcurrency >= 2.3.0.%{oldVersion}, ace-tao-debuginfo >= 6.3.0.%{oldVersion}
# Depends on TAO and Maven
Requires:	apache-maven >= 3.2.5, maven-local
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
#export JACORB_HOME=%{_usr}/local/share/JacORB

export M2_HOME="%{_usr}/share/apache-maven"

cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL
curl -o %{_builddir}/%{name}-%{version}/ExtProd/PRODUCTS/jacorb-3.6.1-source.zip http://www.jacorb.org/releases/3.6.1/jacorb-3.6.1-source.zip

sh buildJacORB

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
mkdir -p %{buildroot}/%{_usr}/local/share/JacORB
cd %{_builddir}/home/almamgr/%{name}-%{version}/JacORB/
find lib/ -name *.so | xargs chmod 755 $1
cp -rf %{_builddir}/home/almamgr/%{name}-%{version}/JacORB/ %{buildroot}/%{_usr}/local/share/JacORB

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "JACORB_HOME=%{_usr}/local/share/JacORB/" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export JACORB_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "CLASSPATH=$CLASSPATH:%{_usr}/local/share/JacORB/lib/" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export CLASSPATH" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh

%files
%attr(755,-,-) %{_usr}/local/share/JacORB/
%{_sysconfdir}/profile.d/jacorb-acs.sh

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
