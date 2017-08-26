%define oldVersion 2016.10

Name:		JacORB-ACS
Version:	3.6.1.2017.06
Release:	1%{?dist}
Summary:	JacORB 3.6.1 for ACS
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
#Source1:	buildTclTk-OCT2013
BuildRequires:	gcc, make, tar, wget, apache-maven >= 3.2.5, ace >= 6.3.0.%{oldVersion}, ace-devel >= 6.3.0.%{oldVersion}, ace-xml >= 6.3.0.%{oldVersion}, ace-gperf == 6.3.0.%{oldVersion}, ace-xml-devel >= 6.3.0.%{oldVersion}, ace-kokyu >= 6.3.0.%{oldVersion}, ace-kokyu-devel >= 6.3.0.%{oldVersion}, mpc >= 6.3.0.%{oldVersion}, tao >= 2.3.0.%{oldVersion}, tao-devel >= 2.3.0.%{oldVersion}, tao-utils >= 2.3.0.%{oldVersion}, tao-cosnaming >= 2.3.0.%{oldVersion}, tao-cosevent >= 2.3.0.%{oldVersion}, tao-cosnotification >= 2.3.0.%{oldVersion}, tao-costrading >= 2.3.0.%{oldVersion}, tao-rtevent >= 2.3.0.%{oldVersion}, tao-cosconcurrency >= 2.3.0.%{oldVersion}, ace-tao-debuginfo >= 6.3.0.%{oldVersion}
BuildRequires:  plexus-classworlds java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo apache-maven >= 3.2.5
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
export CLASSPATH="$CLASSPATH:%{_usr}/share/java/plexus/classworlds.jar"
export PATH=$PATH:%{_builddir}/%{name}-%{version}/ExtProd/INSTALL/
export JAVA_HOME="/usr/lib/jvm/java-1.8.0-openjdk"
export M2_HOME="%{_usr}/share/apache-maven"

#Modify harcoded paths
sed -i 's/$ACE_ROOT\/TAO\/orbsvcs\/orbsvcs\/CosProperty.idl/\/usr\/share\/tao\/orbsvcs\/orbsvcs\/CosProperty.idl/g' %{_builddir}/%{name}-%{version}/ExtProd/INSTALL/buildJacORB

sed -i 's/$ACE_ROOT\/TAO\/orbsvcs\/orbsvcs\/DsLogAdmin.idl/\/usr\/share\/tao\/orbsvcs\/orbsvcs\/DsLogAdmin.idl/g' %{_builddir}/%{name}-%{version}/ExtProd/INSTALL/buildJacORB

sed -i 's/$ACE_ROOT\/TAO\/orbsvcs\/orbsvcs\/AVStreams.idl/\/usr\/share\/tao\/orbsvcs\/orbsvcs\/AVStreams.idl/g' %{_builddir}/%{name}-%{version}/ExtProd/INSTALL/buildJacORB

sed -i 's/$ACE_ROOT\/TAO\/tao\/TimeBase.pidl/\/usr\/include\/tao\/TimeBase.pidl/g' %{_builddir}/%{name}-%{version}/ExtProd/INSTALL/buildJacORB

cd %{_builddir}/%{name}-%{version}/ExtProd/INSTALL
#wget -c -O %{_builddir}/%{name}-%{version}/ExtProd/PRODUCTS/jacorb-3.6.1-source.zip http://www.jacorb.org/releases/3.6.1/jacorb-3.6.1-source.zip
wget -c -O %{_builddir}/%{name}-%{version}/ExtProd/PRODUCTS/jacorb-3.6.1-source.zip http://repo.csrg.cl/Sources/jacorb-3.6.1-source.zip
rm -rf %{_builddir}/alma/%{name}-%{version}/JacORB
mkdir -p %{_builddir}/alma/%{name}-%{version}/JacORB

sh buildJacORB

cd $JACORB_HOME
mvn clean install -e -X -DskipTests=true -DskipPDFGeneration=true -DskipJavadoc=true -Dmaven.clean.failOnError=false -Dmaven.javadoc.failOnError=false
mkdir -p $JACORB_HOME/lib/endorsed
mv $JACORB_HOME/lib/jacorb-omgapi-3.6.1.jar $JACORB_HOME/lib/endorsed


# Clean symlink in builddir
unlink %{_builddir}/alma

%install
mkdir -p %{buildroot}/%{_usr}/local/share/
#cd %{_builddir}/home/almamgr/%{name}-%{version}/JacORB/
#find lib/ -name *.so | xargs chmod 755 $1
cp -rf %{_builddir}/home/almamgr/%{name}-%{version}/JacORB/ %{buildroot}/%{_usr}/local/share/

mkdir -p %{buildroot}%{_sysconfdir}/profile.d/
echo "JACORB_HOME=%{_usr}/local/share/JacORB/" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export JACORB_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "CLASSPATH=$CLASSPATH:%{_usr}/local/share/JacORB/lib/" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export CLASSPATH" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "PATH=$PATH:%{_usr}/local/share/JacORB/bin/" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export PATH" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh
echo "export JAVA_HOME" >> %{buildroot}%{_sysconfdir}/profile.d/jacorb-acs.sh


%files
%attr(755,-,-) %{_usr}/local/share/JacORB/
%{_sysconfdir}/profile.d/jacorb-acs.sh

%changelog
* Sat Aug 19 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 3.6.1.2017.06-1
Initial Packaging
