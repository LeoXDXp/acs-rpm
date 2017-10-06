Name:       ACS-acsqos
Version:    2017.06
Release:    1%{?dist}
Summary:    ACS QOS Declarations
License:    LGPL
URL:        http://csrg-utfsm.github.io
Source0:    %{name}-%{version}.tar.gz
Source1:    Makefile-acsqos
#BuildRequires: ACS-ExtProds >= %{version} ACS-ExtJars >= %{version}
BuildRequires:  ACS-Tools-Kit-Benchmark-devel >= %{version} ACS-acserr >= %{version} ACS-acserridl >= %{version}
#Requires:       ACS-Tools-Kit-Benchmark >= %{version}


%description
ACS QOS.

%prep
%setup -q

#cambiar el makefile solo para el modulo
%build
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/Makefile

# Basic path
mkdir -p  %{_builddir}/home/almamgr
# Symlink for build log
ln -s %{_builddir}/home/almamgr %{_builddir}/alma

# Env Vars for installing. 
source %{_sysconfdir}/profile.d/acscb.sh
source %{_sysconfdir}/profile.d/acscb-toolsKit.sh
source %{_sysconfdir}/profile.d/acscb-gnu.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/acscb-python.sh
#### custom ####
### end custom ###

#general Compilation
export ALMASW_ROOTDIR=%{_builddir}/alma
export ALMASW_RELEASE=ACS-%{version}
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ALMASW_ROOTDIR/$ALMASW_RELEASE/config/defaultCDB"
export IDL_PATH="$IDL_PATH:%{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/idl/"

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

#xsd files needed by acsqos
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/ACSError.xsd %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserridl/ws/idl/acserr.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acscomponentidl/ws/idl/acscomponent.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/idl/
ln -s %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/acscommon.idl %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/idl/
sed -i 's/\$(ACE\_ROOT)\/TAO\/orbsvcs\/orbsvcs\// ..\/idl\/ /g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/src/Makefile


#sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenIDL
#sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenCpp
#sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava
#sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenPython
#sed -i 's/$ACSROOT\/lib\/xalan\.jar${PATH_SEP}$ACSROOT\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/src/acserrGenJava
#sed -i 's/$(ACSROOT)\/lib\/xalan\.jar$(PATH_SEP)$(ACSROOT)\/lib\/xalan_serializer\.jar/\/usr\/share\/java\/xalan-j2\.jar:\/usr\/share\/java\/xalan-j2-serializer\.jar:\/usr\/local\/share\/java\/castor-ACS\.jar/g' %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefileCore.mk 


#ln -s %{_builddir}/%{altname}-%{version}/LGPL/CommonSoftware/acsidlcommon/ws/idl/commontypes.xsd %{_builddir}/%{altname}-%{version}/LGPL/CommonSoftware/acserr/ws/idl/

cd %{_builddir}/%{name}-%{version}/
mkdir -p %{_builddir}/home/almamgr/ACS-%{version}/ACSSW/
#sed -i 's/@echo "ERROR: ----> $@  does not exist."; exit 1/@echo "ERROR: ----> $@  does not exist.";/g'  %{_builddir}/%{name}-%{version}/LGPL/Kit/acs/include/acsMakefile

mkdir -p %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/
ln -s %{_usr}/local/share/java/acserr.jar %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacserr.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/
ln -s %{_usr}/local/%{_lib}/libacserrStubs.so %{_builddir}/%{name}-%{version}/LGPL/CommonSoftware/acsQoS/ws/lib/

make 
%install

#unlink
unlink %{_builddir}/alma

%files

%changelog
* Sat May 20 2017 Maximiliano Osorio <mosorio@inf.utfsm.cl> - 0.1-1
Initial Packaging
