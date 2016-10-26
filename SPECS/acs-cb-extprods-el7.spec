Name:		ACS-ExtProds
Version:	2016.6
Release:	1%{?dist}
Summary:	ACS CB ExtProds for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
# Source0, no need for anything else than ACS/ExtProds folder, with the downloaded sources within
Source0:	%{name}-%{version}.tar.gz
# Ant for EL7 is up to 1.9.2. ACS uses 1.9.3  # Boost for ACS is 1.41. Epel provides 1.48 # ACS uses omniORB 4.1.4. Epel provides 4.2.0
# ACS uses maven 3.2.5. Apache maven repo provides 3.2.5. Installed in pre

BuildArch: x86_64
# Base tools
BuildRequires: python-virtualenv epel-release git wget unzip tar bzip2 patch
# Packages checked
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ant boost148 omniORB-devel omniORB-doc omniORB-servers omniORB-utils omniORB apache-maven-3.2.5-1.el7.noarch gcc-c++
# PyModules
BuildRequires: pytz python-pbr python-linecache2 python-jinja2 python-babel python-markupsafe 


# Packages in Testing
#BuildRequires: ksh blas-devel expat-devel vim libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel openssl-devel openldap-devel freetype-devel libpng-devel libxml2-devel libxslt-devel gsl-devel autoconf213 autoconf util-linux-ng unzip time log4cpp expat cppunit cppunit-devel swig xterm lpr ant centos-release asciidoc xmlto cvs openldap-devel bc ime rsync openssh-server autoconf automake binutils bison flex gcc gcc-c++ gettext gcc-gfortran make byacc patch libtool pkgconfig redhat-rpm-config rpm-build rpm-sign cscope ctags diffstat doxygen elfutils indent intltool patchutils rcs  swig systemtap xz libdb-devel
# In epel: log4cpp xemacs xemacs-packages-extra sqlite2-devel
# No existen en centos 7: perl-ExtUtils MakeMaker libncurses-devel ime libpng10-devel expat21 castor* shunit2

%description
RPM Installer of ACS-CB ExtProducts %{version}. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q
# builddir = /home/user/rpmbuild/BUILDDIR # setup -q = {builddir}/ACS-ExtProds-2016.6/ExtProds/{PRODUCTS,INSTALL}

%build
# Declare Global Variables for scripts in ExtProds/INSTALL/
export ALMASW_ROOTDIR="%{buildroot}/alma"
export ALMASW_RELEASE="ACS-%{version}"

export ACE_ROOT="%{buildroot}/alma/ACS-%{version}/TAO/ACE_wrappers/build/linux"
export ACE_ROOT_DIR="%{buildroot}/alma/ACS-%{version}/TAO/ACE_wrappers/build"
export M2_HOME="%{_usr}/share/apache-maven"  # Exported by apache-maven itself, only after re-login
export JACORB_HOME="%{buildroot}/alma/ACS-%{version}/JacORB"
export PYTHON_ROOT="%{buildroot}/alma/ACS-%{version}/Python"
export OMNI_ROOT="%{buildroot}/alma/ACS-%{version}/Python/"

%install
#Create basic folder and symlink
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
# Access and execute scripts. Each script should output the result to %{buildroot}/alma/ACS-%{version}/ 
cd %{_builddir}/ACS/ExtProds/INSTALL/
# Run scripts
./buildEclipse
./buildTAO # Needs c++
./buildJacORB # Depends on TAO and Maven
./buildPython 
./buildPyModules # PyModules could be installed directly as requires. Depends on buildPython
./buildOmniORBpy 
./buildTcltk # TestPending


#install -m 0755 -D -p %{SOURCE1} %{buildroot}/home/almamgr%{name}-%{version}
%clean
cd $ALMASW_INSTDIR
find -name "*.o" | xargs rm -rf

%pre
# Install epel-maven repo
curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo
yum -y install epel-release

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

%post
# Permissions
chown -R almamgr:almamgr /home/almamgr/

%preun
 
%postun
# Al user processes must be killed before userdel
pkill -u almamgr
userdel -r almamgr

%files
%doc
%attr(0705,almagr,almamgr) /home/almamgr/ 
%attr(0705,almagr,almamgr) /home/almamgr/ACS-%{version}/*

%changelog
* Wed Oct 26 2016 Leonardo Pizarro <lepizarr@inf.utfsm.cl> - 0.1-1
Initial Packaging
