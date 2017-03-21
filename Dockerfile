# DockerFile to build ACS 2017.02 RPM
FROM centos:centos7

MAINTAINER CSRG <leonardo.pizarro@usm.cl>

#Installing dependencies
RUN yum update -y
RUN curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo
RUN curl http://repo.csrg.cl/acs-cb.repo -o /etc/yum.repos.d/acs-cb.repo
RUN yum -y install epel-release centos-release-scl
RUN yum install -y ACS-ExtProds ACS-ExtJars
RUN yum install -y rpm-build tar
RUN yum install -y gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib log4cpp shunit2 castor hibernate3 xerces-c xerces-c-devel xerces-j2 time ksh rh-java-common-PyXB python-pmw-1.3.2 pexpect PyXML pychecker apache-commons-lang junit javassist geronimo-jta mockito mysql-connector-java objenesis xmlunit procmail tkinter

# Might need to source new files in profile.d if source within

#Creating rpm user
RUN adduser -U rpm
#Changing to rpm user
USER rpm

#Download rpm repo
RUN git clone -b master --depth 1 https://github.com/LeoXDXp/acs-rpm.git ~/rpmbuild
# Create Source0
RUN cd ~/rpmbuild/SOURCES/ && git clone -b master --depth 1 https://github.com/csrg-utfsm/acscb.git
RUN tar czvf ACS-2017.02.tar.gz ACS* Benchmark Documents L* Makefile R*

ENV MAKE_VERBOSE=on
RUN cd ~/rpmbuild && rpmbuild -ba SPECS/acs-cb-el7-full.spec

#ENV MAKE_NOSTATIC=yes
