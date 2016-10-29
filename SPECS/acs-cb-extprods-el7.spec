Name:		ACS-ExtProds
Version:	2016.6
Release:	1%{?dist}
Summary:	ACS CB ExtProds for CentOS 7	
License:	LGPL
URL:		http://acs-community.github.io/
# Source0, no need for anything else than ACS/ExtProds folder, with the downloaded sources within
Source0:	%{name}-%{version}.tar.gz
# Ant for EL7 is up to 1.9.2. ACS uses 1.9.3  # Boost for ACS is 1.41. Epel provides 1.48 # ACS uses omniORB 4.1.4. Epel provides 4.2.0, but omniORBpy compilation must be changed: Using ACS's for now
# ACS uses maven 3.2.5. Apache maven repo provides 3.2.5. Installed in pre. ACS's ACE+TAO is 6.3.0, Opensuse repo has 6.4.1

BuildArch: x86_64
# Base tools
BuildRequires: python-virtualenv epel-release git wget unzip tar bzip2 patch
# Packages checked
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ant boost148 omniORB-devel omniORB-doc omniORB-servers omniORB-utils omniORB gcc-c++, apache-maven == 3.2.5
# PyModules With lower or equal version as acs.req
BuildRequires: pytz python-pbr python-linecache2 python-jinja2 python-babel python-markupsafe python-pygments python-sphinx python2-sphinx-theme-alabaster python-astroid python-coverage python-docutils python-logilab-common python2-mock python-nose numpy pylint python-six python2-traceback2 
# PyModules with higher versions than those in acs.req
# BuildRequires: python-ipython python-sphinx_rtd_theme python-unittest2
# Built by Tcltk for ACS. Missing on repos: tklib tkimg snack tkman rman tclCheck msqltcl
#Requires: tk iwidgets tclx tcllib blt tktable expect tkcon

%description
RPM Installer of ACS-CB ExtProducts %{version}. It takes the compiled files and installs them on /home/almamgr/ACS-version (symlink to /alma). 

%prep
%setup -q
# builddir = /home/user/rpmbuild/BUILDDIR # setup -q = {builddir}/ACS-ExtProds-2016.6/ExtProds/{PRODUCTS,INSTALL}

#%build

%install
# Declare Global Variables for scripts in ExtProds/INSTALL/
export ALMASW_ROOTDIR="%{buildroot}/alma"
export ALMASW_RELEASE="ACS-%{version}"

export ACE_ROOT="%{buildroot}/alma/ACS-%{version}/TAO/ACE_wrappers/build/linux"
export ACE_ROOT_DIR="%{buildroot}/alma/ACS-%{version}/TAO/ACE_wrappers/build"
export M2_HOME="%{_usr}/share/apache-maven"  # Exported by apache-maven itself, only after re-login
export JACORB_HOME="%{buildroot}/alma/ACS-%{version}/JacORB"
export PYTHON_ROOT="%{buildroot}/alma/ACS-%{version}/Python"
export OMNI_ROOT="%{buildroot}/alma/ACS-%{version}/Python/"

#Create basic folder and symlink
mkdir -p %{buildroot}/home/almamgr/ACS-%{version}/
ln -s %{buildroot}/home/almamgr %{buildroot}/alma
# Access and execute scripts. Each script should output the result to %{buildroot}/alma/ACS-%{version}/ 
cd %{_builddir}/%{name}-%{version}/INSTALL/
# Run scripts
./buildEclipse
./buildTAO # Needs c++
./buildJacORB # Depends on TAO and Maven
./buildPython # Python and PyModules source PYTHON_ROOT/bin/activate file
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
