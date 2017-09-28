%define ALTVER FEB2017

Name:		ACS
Version:	2017.02
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz 
Source1:	https://raw.githubusercontent.com/tmbdev/pylinda/master/linda/doc/pythfilter.py
Source2:	tao_ifr_service
# Modified Makefile to compile only ACS core Modules
Source3:	Makefile-Core
Source4:	acscbdaemon-systemd
Source5:	acscbRemotedaemon-systemd

BuildArch: x86_64 aarch64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
BuildRequires: ACS-Tools-Kit-Benchmark >= %{version}

%description
RPM Installer of ACS-CB %{version}. Installs ACS CB in /home/almamgr/, leaving env vars in profile.d and commands symlinked to /usr/local/bin avoiding sourcing of .bash_profile.acs file. 

%prep
%setup -q
%build
# Replace LGPL/Tools/extpy/src/Pythfilter  with SOURCE1 pythfilter.
cp -f %{SOURCE1} %{_builddir}/%{name}-%{version}/LGPL/Tools/extpy/src/
cp -f %{SOURCE3} %{_builddir}/%{name}-%{version}/Makefile

%install
# Basic paths and symlinks
mkdir -p  %{buildroot}/home/almamgr
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
ln -s %{buildroot}/home/almamgr/%{name}-%{version} %{buildroot}/home/almamgr/%{name}-current

# Source 4,5 SystemD daemons
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/
cp -f %{SOURCE4} %{buildroot}%{_sysconfdir}/systemd/system/acscb.service
cp -f %{SOURCE5} %{buildroot}%{_sysconfdir}/systemd/system/acscbremote.service

# Env Vars for installing. 
export ALMASW_ROOTDIR=%{buildroot}/alma
export ALMASW_RELEASE=%{name}-%{version}
export ACSDATA="$ALMASW_ROOTDIR/$ALMASW_RELEASE/acsdata"
export ACSROOT="$ALMASW_ROOTDIR/$ALMASW_RELEASE/ACSSW"
export ACS_CDB="$ACSDATA/config/defaultCDB"
export ACS_INSTANCE="0"
export ACS_STARTUP_TIMEOUT_MULTIPLIER="2"
# hostname has to be short, or can be fqdn
export ACS_TMP="$ACSDATA/tmp/$HOSTNAME"
export IDL_PATH="-I$ACSROOT/idl -I/usr/src/debug/ACE_wrappers/TAO/orbsvcs/orbsvcs -I$TAO_ROOT/orbsvcs -I$TAO_ROOT -I/usr/include/orbsvcs -I/usr/include/tao"
export LD_LIBRARY_PATH="$ACSROOT/idl:/usr/lib64/:$ACSROOT/tcltk/lib:/usr/local/lib64:/usr/local/lib"
export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk
export PATH="$PATH:/alma/%{name}-%{version}/tctlk/bin:/alma/%{name}-%{version}/JacORB/bin:$GNU_ROOT/bin:/alma/%{name}-%{version}/ACSSW/bin"
# Calling Mico, JacORB, ACE+TAO , MPC, Maven env vars PENDING OmniORB 2 paths, Extend PATH, python_root path, manpath , gnu_root maybe?
source %{_sysconfdir}/profile.d/mico.sh
source %{_sysconfdir}/profile.d/jacorb.sh
source %{_sysconfdir}/profile.d/ant.sh
source %{_sysconfdir}/profile.d/ace-devel.sh # overrides ACE_ROOT
source %{_sysconfdir}/profile.d/apache-maven.sh
source %{_sysconfdir}/profile.d/mpc.sh
source %{_sysconfdir}/profile.d/tao-devel.sh
source %{_sysconfdir}/profile.d/tcltk-acs.sh
source %{_sysconfdir}/profile.d/acscb-python.sh # PythonPath, PythonInc, PythonRoot
source %{_sysconfdir}/profile.d/acscb-gnu.sh

# Compilation specific env vars
export MAKE_NOSTATIC=yes
export MAKE_NOIFR_CHECK=on
export MAKE_PARS=" -j 2 -l 2 "

cd %{_builddir}/%{name}-%{version}/
# mkdir of ACSSW
mkdir -p %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/

make

# To allow the extraction of debug info
chmod +w %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/lib/libacserrStubs.so
chmod +w %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/lib/libACSIRSentinelStubs.so
chmod +w %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/lib/libacscomponentStubs.so

# /usr/local/bin. Source2 here
mkdir -p %{buildroot}%{_usr}/local/bin/
cp -f %{SOURCE2} %{buildroot}%{_usr}/local/bin/
#ln -s %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/bin/* %{buildroot}%{_usr}/local/bin/

#Symlink Libs in include. Very useful when building, because it's in gcc's default path
mkdir -p %{buildroot}%{_usr}/local/include/
#ln -s %{buildroot}/home/almamgr%{name}-%{version}/ACSSW/include/* %{buildroot}%{_usr}/local/include/

# Move ACS Mans to here
mkdir -p %{buildroot}%{_usr}/local/share/
#mv %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/share/man/man1/ %{buildroot}%{_usr}/local/share/man/
#mv %{buildroot}/home/almamgr/%{name}-%{version}/ACSSW/share/man/man3/ %{buildroot}%{_usr}/local/share/man/
# Documentation
mkdir -p %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/README* %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/LICENSE* %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/ACS_* %{buildroot}%{_usr}/local/acscb/
mv %{_builddir}/%{name}-%{version}/Documents/ %{buildroot}%{_usr}/local/acscb/
# /etc. Hoping to have acsdata only on etc in the future
mkdir -p %{buildroot}%{_sysconfdir}/acscb/
cp -r %{buildroot}/home/almamgr/%{name}-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
# Introot for development
mkdir -p  %{buildroot}/home/almaproc/introot

# Remove objects
cd %{buildroot}/alma/ACS-%{version}/ACSSW/
find -name "*.o" | xargs rm -rf

# Destroy Symlink in buildroot
%{_usr}/bin/unlink %{buildroot}/alma
%{_usr}/bin/unlink %{buildroot}/home/almamgr/%{name}-current

%clean

%pre
# almaproc user created in ACS-Tools-Kit-Benchmark
%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almaproc:almaproc /home/almaproc/introot/
mkdir -p /home/almamgr/%{name}-%{version}/Python/lib/python2.7/
ln -s /home/almamgr/%{name}-%{version}/ /home/almamgr/%{ALTVER}
ln -s /home/almamgr/%{name}-%{version}/ /home/almamgr/%{name}-latest
# Fixing chmod done for debug info extraction
chmod -w /home/almamgr/%{name}-%{version}/ACSSW/lib/libacserrStubs.so
chmod -w /home/almamgr/%{name}-%{version}/ACSSW/lib/libACSIRSentinelStubs.so
chmod -w /home/almamgr/%{name}-%{version}/ACSSW/lib/libacscomponentStubs.so

# Enable systemd services
systemctl enable acscb.service
systemctl enable acscbremote.service
systemctl daemon-reload

# Reload Python modules. Avoids the error: from omniORB import CORBA \n omniORB not found
python -c "help('modules')"

%preun
systemctl stop acscb.service
systemctl disable acscb.service
 
%postun
systemctl daemon-reload
# Al user processes must be killed before userdel
pkill -u almamgr
#userdel -r almamgr # Dependecy issue with ExtProds

%files
# ACSSW, acsdata, READMEs, LICENSE, ACS_VERSION, ACS_PATCH_LEVEL
%config %{_sysconfdir}/systemd/system/acscb.service
%config %{_sysconfdir}/systemd/system/acscbremote.service
%config %{_sysconfdir}/acscb/
%attr(0705,almamgr,almamgr) /home/almamgr/%{name}-%{version}/ACSSW/
%attr(0705,almamgr,almamgr) /home/almamgr/%{name}-%{version}/ACSSW/bin/
%attr(0705,almamgr,almamgr) /home/almamgr/%{name}-%{version}/acsdata/
%attr(-,almaproc,almaproc)/home/almaproc/introot/
%{_usr}/local/bin
%{_usr}/local/lib
%license /home/almamgr/%{name}-%{version}/LICENSE.md
%docdir %{_usr}/local/share/man/
%{_usr}/local/share/man/
%docdir %{_usr}/local/acscb/
%{_usr}/local/acscb/

%changelog
* Fri Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
