Name:		ACS
Version:	2015.4
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	

Group:		
License:	
URL:		
#Source0:	http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz
#Source1:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-3.6.1-delta-pack.zip
#Source2:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-4.2.2-delta-pack.zip	
#Source3:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-linux-gtk-x86_64.tar.gz
#Source4:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz
#Source5:	http://www.jacorb.org/releases/3.6/jacorb-3.6-source.zip

BuildArch: %{?dist}
BuildRequires:	java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ksh blas-devel gcc expat-devel gcc gcc-c++ gcc-gfortran make byacc patch vim subversion libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel sqlite2-devel openssl-devel openldap-devel freetype-devel libpng-devel libpng10-devel libxml2-devel libxslt-devel gsl-devel flex xemacs xemacs-packages-extra doxygen autoconf213 autoconf util-linux-ng unzip time log4cpp expat expat21 cppunit cppunit-devel swig castor castor-xml castor-demo shunit2 lockfile-progs xterm lpr ant centos-release
Requires: procmail lockfile-progs "X Window System" gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server 

%description
RPM Installer of ACS-CB 2015.4. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
#%make_install
mkdir -p  %{buildroot}/home/almamgr
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
cp -r %{_builddir}/%{name}-%{version}/    %{buildroot}/home/almamgr/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/ %{buildroot}/home/almamgr/%{name}-current/
#Binaries ln
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscommandcenter/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftwareacscourse/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemon/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acsEclipseUtils/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acssampGUI/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmPanel/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmSourcePanel/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/cdbBrowser/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/errorBrowser/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/eventGUI/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/jlog/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logLevelGUI/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logTools/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/objexp/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/alarm-clients/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acslog/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncdds/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspy/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspyexmpl/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssim/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutilpy/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbChecker/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb_rdb/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/codegen/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcont/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jmanager/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingts/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/nsStatisticsService/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/acs/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/acstempl/bin/* /usr/local/bin/
ln -s %{buildroot}/home/almamgr/%{name}-%{version}/LGPL/Kit/doc/bin/* /usr/local/bin/
mkdir -p  %{buildroot}/home/almaproc/introot
%clean


%pre
# Install epel-maven repo
curl -O https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo

# ACE-TAO RPM from OpenSUSE
echo "
[ace-tao_opensuse]
name=Latest ACE micro release (CentOS_7)
type=rpm-md
baseurl=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7/
gpgcheck=1
gpgkey=http://download.opensuse.org/repositories/devel:/libraries:/ACE:/micro/CentOS_7//repodata/repomd.xml.key
enabled=0
" > /etc/yum.repos.d/ace-tao.repo

#Local users
useradd -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/
chown almaproc:almaproc /home/almaproc/introot/

# Create systemd service
echo "
[Unit]
Description=Alma Common Software CB Service
Documentation=man:sshd(8) man:sshd_config(5)
After=multi-user.target

[Service]
Type=oneshoot
Environment=INTROOT='/home/almaproc/introot/'
EnvironmentFile=-/home/almamgr/ACS-current/LGPL/acsBUILD/config/.acs/.bash_profile.acs
User=almamgr
ExecStart=acsStart
ExecStop=acsStop && acsdataClean --all
ExecReload=cdbjDALClearCache
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target

" > %{_sysconfdir}/systemd/system/acscb.service
systemctl enable acscb.service
systemctl daemon-reload

# Set SELinux PERMISSIVE (Audit mode)
sed -i 's/SELINUX=disabled/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
setenforce 0

# /etc/hosts
#echo "" >> /etc/hosts

%preun
systemctl stop acscb.service
systemctl disable acscb.service
 
%postun
systemctl daemon-reload
# Al user processes must be killed before userdel
pkill -u almaproc
pkill -u almamgr
userdel -r almamgr
userdel -r almaproc

%files
%doc
%config %{_sysconfdir}/systemd/system/acscb.service
%attr(0705,almagr,almamgr) /home/almamgr/ 
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsalarmidl/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acscommandcenter/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftwareacscourse/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsdaemon/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acserr/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsexmpl/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acsEclipseUtils/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/acssampGUI/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmPanel/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/alarmSourcePanel/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/cdbBrowser/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/errorBrowser/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/eventGUI/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/jlog/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logLevelGUI/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/logTools/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsGUIs/objexp/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/ACSLaser/alarm-clients/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acslog/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsncdds/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspy/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acspyexmpl/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acssim/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsstartup/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutil/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/acsutilpy/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdbChecker/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/cdb_rdb/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/codegen/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/containerTests/contNcTest/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jacsutil/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jcont/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/jmanager/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/logging/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/loggingts/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/maci/ws/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/nsStatisticsService/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/task/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/CommonSoftware/xmlpybind/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/Kit/acs/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/Kit/acstempl/bin/*
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/LGPL/Kit/doc/bin/*
%attr(-,almaproc,almaproc)/home/almaproc/introot/
%config %{_usr}/local/bin/*

%changelog
* Mon Aug 19 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
