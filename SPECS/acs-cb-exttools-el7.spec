Name:		ACS-ExtProds
Version:	2016.6
Release:	1%{?dist}
Summary:	ACS CB ExtProds for CentOS 7	

#Group:		
License:	LGPL
URL:		http://acs-community.github.io/
# Source0, no need for anything else than ACS/ExtProds folder
Source0:	%{name}-%{version}.tar.gz
Source1:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-3.6.1-delta-pack.zip
Source2:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-4.2.2-delta-pack.zip	
Source3:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-linux-gtk-x86_64.tar.gz
Source4:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz
Source5:	http://www.jacorb.org/releases/3.6/jacorb-3.6-source.zip
# Ant for EL7 is up to 1.9.2. ACS uses 1.9.3 
#Source6:	http://archive.apache.org/dist/ant/source/apache-ant-1.9.3-src.tar.gz
# Boost for ACS is 1.41. Epel provides 1.48
#Source7:	http://downloads.sourceforge.net/project/boost/boost/1.41.0/boost_1_41_0.tar.bz2?r=http%3A%2F%2Fwww.boost.org%2Fusers%2Fhistory%2Fversion_1_41_0.html&ts=1405539262&use_mirror=ufpr
# ACS uses omniORB 4.1.4. Epel provides 4.2.0
#Source8:	http://downloads.sourceforge.net/project/omniorb/omniORB/omniORB-4.1.4/omniORB-4.1.4.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fomniorb%2Ffiles%2FomniORB%2FomniORB-4.1.4%2F&ts=1405542245&use_mirror=ufpr
# omniORBpy not found on repos
Source9:	http://downloads.sourceforge.net/project/omniorb/omniORBpy/omniORBpy-3.4/omniORBpy-3.4.tar.gz?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fomniorb%2Ffiles%2FomniORBpy%2FomniORBpy-3.4%2F&ts=1405542362&use_mirror=ufpr
# ACS uses maven 3.2.5. Apache maven repo provides 3.2.5. Installed in pre
#Source10:	http://mirrors.advancedhosters.com/apache/maven/maven-3/3.2.5/binaries/apache-maven-3.2.5-bin.tar.gz
Source11:	http://download.dre.vanderbilt.edu/previous_versions/ACE+TAO-6.3.0.tar.gz


BuildArch: x86_64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
# Base tools and repos
BuildRequires: python-virtualenv epel-release git wget 
# Packages checked
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ant boost148 omniORB-devel omniORB-doc omniORB-servers omniORB-utils omniORB apache-maven-3.2.5-1.el7.noarch
# Packages in Testing
#BuildRequires: ksh blas-devel expat-devel vim libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel openssl-devel openldap-devel freetype-devel libpng-devel libxml2-devel libxslt-devel gsl-devel autoconf213 autoconf util-linux-ng unzip time log4cpp expat cppunit cppunit-devel swig xterm lpr ant centos-release asciidoc xmlto cvs openldap-devel bc ime rsync openssh-server autoconf automake binutils bison flex gcc gcc-c++ gettext gcc-gfortran make byacc patch libtool pkgconfig redhat-rpm-config rpm-build rpm-sign cscope ctags diffstat doxygen elfutils indent intltool patchutils rcs  swig systemtap xz libdb-devel
# In epel: log4cpp xemacs xemacs-packages-extra sqlite2-devel
# No existen en centos 7: perl-ExtUtils MakeMaker libncurses-devel ime libpng10-devel expat21 castor* shunit2

%description
RPM Installer of ACS-CB ExtProducts %{version}. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q
# builddir = /home/user/rpmbuild/BUILDDIR
# setup -q = {builddir}/ACS/ExtProds/{PRODUCTS,INSTALL}

#%build
#%configure
#make %{?_smp_mflags}



%install
# Moves {builddir}/ACS/ExtProds/{PRODUCTS,INSTALL} to {buildroot}/ACS/ExtProds/{PRODUCTS,INSTALL}
#%make_install
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
# Move Sources 1 - N to %{builddir}/ACS/ExtProds/PRODUCTS/


cp -r %{_builddir}%{name}-%{version}/    %{buildroot}/home/almamgr/
ln -s %{buildroot}/home/almamgr%{name}-%{version}/ %{buildroot}/home/almamgr%{name}-current/
cp %{buildroot}/home/almamgr%{name}-%{version}/LGPL/acsBUILD/config/.acs/.bash_profile.acs %{buildroot}%{_sysconfdir}/acs/bash_profile.acs.old
cp -r %{buildroot}/home/almamgr%{name}-%{version}/acsdata/config/ %{buildroot}%{_sysconfdir}/acscb/
#Source1 ExtProds
install -m 0755 -D -p %{SOURCE1} %{buildroot}/home/almamgr%{name}-%{version}
%clean

%pre
# Install epel-maven repo
curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo

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
useradd -u 550 -U almamgr
useradd -U almaproc
echo new2me | echo new2me | passwd --stdin almaproc

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/

# Set SELinux PERMISSIVE (Audit mode)
sed -i 's/SELINUX=disabled/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' %{_sysconfdir}/sysconfig/selinux
setenforce 0

# /etc/hosts
#echo "" >> /etc/hosts

%preun
 
%postun
# Al user processes must be killed before userdel
pkill -u almamgr
userdel -r almamgr

%files
%doc
%attr(0705,almagr,almamgr) /home/almamgr/ 
%attr(0705,almagr,almamgr) /home/almamgr/%{name}-%{version}/*
#%{_usr}/local/bin/*
#%{_usr}/local/lib/*

%changelog
* Wed Oct 26 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
