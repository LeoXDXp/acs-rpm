Name:		ACS-acserr
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS Error Core
License:	LGPL
URL:		http://csrg-utfsm.github.io
Source0:	%{name}-%{version}.tar.gz
Source1:	Makefile-acserr
BuildRequires:	ACS-Tools-Kit-Benchmark-devel >= %{version} castor-ACS ACS-acserridl >= %{version} ACS-xmljbind >= %{version} ACS-jacsutil >= %{version}
Requires:	ACS-Tools-Kit-Benchmark >= %{version}

%description
ACS Error Core

%package devel
Summary: ACS Error Objects
License: LGPL

%description devel
Object output: *.h,*.cpp

%prep
%setup -q

%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma
# As acserr looks for internal acserrGen, fix them as they are fixed in Extprods
sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenIDL

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCpp

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava

sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenPython

sed -i 's/`searchFile \/idl\/ACSError\.xsd`/\.\./g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML
sed -i 's/$ACSROOT\/lib/\/usr\/local\/share\/java/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCheckXML

# Hack to look inside the same folder. acserr cant be in a system path if its not yet installed
sed -i 's/&lt;acserr.idl&gt/"acserr.idl"/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/config/AES2IDL.xslt
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/commontypes.xml %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/
# Changing and extending classpath
sed -i 's/$(ACSROOT)\/lib\/xalan\.jar$(PATH_SEP)$(ACSROOT)\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/alma/ACS-%{version}/ACSSW/include/acsMakefileCore.mk 
# acserr.jar
mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
ln -s %{_usr}/local/share/java/acserr.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/lib/
# Not nice stuff in acsMakefileDefinitions.mk
sed -i 's/`acsMakeJavaClasspath`:$(ACSROOT)\/lib\/endorsed\/xercesImpl.jar/\/usr\/share\/java\/xerces-j2.jar:\/usr\/local\/share\/java\/castor-ACS.jar:\/usr\/local\/share\/java\/xmljbind.jar:\/usr\/local\/share\/java\/jACSUtil.jar /g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileDefinitions.mk



export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
# Somehow, classpath breaks things, and still gets ignored

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/

make

# Clean symlink in builddir
unlink %{_builddir}/alma

%install
# Instalation on usr local, if python, then python/site-packages, if C/C++, then include, if Java, then share/java 
# ACSErr and ACSErr__POA folders, and acserr_idl.py
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/acscommon/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/acscommon__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/acscommon_idl.py %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/log_audience/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/log_audience__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/ACS/ %{buildroot}%{_usr}/local/lib/python/site-packages/
cp -rf %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/python/site-packages/ACS__POA/ %{buildroot}%{_usr}/local/lib/python/site-packages/

# The result of using pyxbgen is bindings.py, which is renamed to commontypes.py for ACS.
mkdir -p %{buildroot}%{_usr}/local/lib/python/site-packages/commontypes/
cp -f %{_builddir}/%{name}-%{version}/binding.py %{buildroot}%{_usr}/local/lib/python/site-packages/commontypes/commontypes.py

mkdir -p %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/commontypes.jar %{buildroot}%{_usr}/local/share/java/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/acscommon.jar %{buildroot}%{_usr}/local/share/java/

mkdir -p %{buildroot}%{_usr}/local/%{_lib}/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/lib/libacscommonStubs.so %{buildroot}%{_usr}/local/%{_lib}/
chmod 755 %{buildroot}%{_usr}/local/%{_lib}/libacscommonStubs.so

# Devel Stuff
mkdir -p %{buildroot}%{_usr}/local/include/
# unlink acserrC.h
unlink %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/acserrC.h
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/*.h %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/*.cpp %{buildroot}%{_usr}/local/include/
cp -f %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/object/*.inl %{buildroot}%{_usr}/local/include/

%files
%{_usr}/local/lib/python/site-packages/acscommon/
%{_usr}/local/lib/python/site-packages/acscommon__POA/
%{_usr}/local/lib/python/site-packages/acscommon_idl.py*
%{_usr}/local/lib/python/site-packages/log_audience/
%{_usr}/local/lib/python/site-packages/log_audience__POA/
%{_usr}/local/lib/python/site-packages/ACS/
%{_usr}/local/lib/python/site-packages/ACS__POA/
%{_usr}/local/lib/python/site-packages/commontypes/commontypes.py*

%{_usr}/local/share/java/commontypes.jar
%{_usr}/local/share/java/acscommon.jar
%{_usr}/local/%{_lib}/libacscommonStubs.so

%files devel
%{_usr}/local/include/acscommonC.cpp
%{_usr}/local/include/acscommonC.h
%{_usr}/local/include/acscommonC.inl
%{_usr}/local/include/acscommonS.cpp
%{_usr}/local/include/acscommonS.h
%{_usr}/local/include/acscommonS_T.cpp
%{_usr}/local/include/acscommonS_T.h

%changelog
* Sat Apr 22 2017 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
