Name:		ACS
Version:	2016.6
Release:	1%{?dist}
Summary:	ACS CB for CentOS 7	

#Group:		
License:	LGPL
URL:		http://acs-community.github.io/
Source0:	%{name}-%{version}.tar.gz
#Source1:	ExtProds-%{version}.tar.gz
#Source1:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-3.6.1-delta-pack.zip
#Source2:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-4.2.2-delta-pack.zip	
#Source3:	http://archive.eclipse.org/eclipse/downloads/drops/R-3.6.1-201009090800/eclipse-SDK-3.6.1-linux-gtk-x86_64.tar.gz
#Source4:	http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-4.2.2-201302041200/eclipse-SDK-4.2.2-linux-gtk-x86_64.tar.gz
#Source5:	http://www.jacorb.org/releases/3.6/jacorb-3.6-source.zip

BuildArch: x86_64
# BuildRequires no acepta un grupo: Se agregan paquetes de Development tools por separado al final desde autoconf
# BuildRequires not used , compilation made by JenkinsCI
# Base tools and repos
BuildRequires: epel-release git wget subversion
# Packages
BuildRequires: java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo ksh blas-devel expat-devel vim libX11-devel ncurses-devel readline gdbm gdbm-devel bzip2-devel zlib-devel sqlite-devel openssl-devel openldap-devel freetype-devel libpng-devel libxml2-devel libxslt-devel gsl-devel autoconf213 autoconf util-linux-ng unzip time log4cpp expat cppunit cppunit-devel swig xterm lpr ant centos-release asciidoc xmlto cvs openldap-devel bc ime rsync openssh-server autoconf automake binutils bison flex gcc gcc-c++ gettext gcc-gfortran make byacc patch libtool pkgconfig redhat-rpm-config rpm-build rpm-sign cscope ctags diffstat doxygen elfutils indent intltool patchutils rcs  swig systemtap xz libdb-devel

# In epel: log4cpp xemacs xemacs-packages-extra sqlite2-devel
# No existen en centos 7
# perl-ExtUtils MakeMaker libncurses-devel ime libpng10-devel expat21 castor* shunit2

# Desglose de paquetes de X Window System desde glx-utils hasta xorg-x11-drv-mouse
Requires:  python procmail lockfile-progs gnome-classic-session gnome-terminal nautilus-open-terminal control-center liberation-mono-fonts setroubleshoot-server glx-utils gdm openbox mesa-dri-drivers plymouth-system-theme spice-vdagent xorg-x11-drivers xorg-x11-server-Xorg xorg-x11-utils xorg-x11-xauth xorg-x11-xinit xvattr xorg-x11-drv-keyboard xorg-x11-drv-mouse gcc-c++ java-1.8.0-openjdk java-1.8.0-openjdk-devel java-1.8.0-openjdk-demo man xterm epel-release 

%description
RPM Installer of ACS-CB %{version}. It takes the compiled files and installs it on /home/almamgr/ (symlink to /alma). 

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
#%make_install
mkdir -p  %{buildroot}/home/almamgr
# /usr/local
mkdir -p %{buildroot}%{_usr}/local/bin/
mkdir -p %{buildroot}%{_usr}/local/lib64/
mkdir -p %{buildroot}%{_usr}/local/include/
mkdir -p %{buildroot}%{_usr}/local/share/
# /var/run/
mkdir -
Initial Packaging
