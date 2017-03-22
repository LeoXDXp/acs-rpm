# DockerFile to build ACS 2017.02 RPM
FROM centos:centos7

MAINTAINER CSRG <leonardo.pizarro@usm.cl>

#Installing dependencies
RUN curl https://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -o /etc/yum.repos.d/epel-apache-maven.repo
RUN curl http://repo.csrg.cl/acs-cb.repo -o /etc/yum.repos.d/acs-cb.repo
RUN yum -y install epel-release centos-release-scl
RUN yum install -y ACS-ExtProds ACS-ExtJars
RUN yum install -y gcc gcc-c++ emacs antlr expat expat-devel cppunit cppunit-devel swig loki-lib log4cpp shunit2 castor hibernate3 xerces-c xerces-c-devel xerces-j2 time ksh rh-java-common-PyXB python-pmw-1.3.2 pexpect PyXML pychecker apache-commons-lang junit javassist geronimo-jta mockito mysql-connector-java objenesis xmlunit procmail tkinter
RUN yum install -y git rpm-build tar
# Might need to source new files in profile.d if source within

#Creating rpm user
RUN adduser -U rpm
#Changing to rpm user
USER rpm

#Download rpm repo, Create Source0
RUN git clone -b master --depth 1 https://github.com/LeoXDXp/acs-rpm.git ~/rpmbuild
RUN cd ~/rpmbuild/SOURCES/ && git clone -b master --depth 1 https://github.com/csrg-utfsm/acscb.git ACS-2017.02/ && ls -la
RUN cd ~/rpmbuild/SOURCES/ && tar czvf ACS-2017.02.tar.gz ACS-2017.02/ACS* ACS-2017.02/Benchmark ACS-2017.02/Documents ACS-2017.02/L* ACS-2017.02/Makefile ACS-2017.02/R*

ENV MAKE_VERBOSE=on
RUN cd ~/rpmbuild && rpmbuild -ba SPECS/acs-cb-el7-full.spec
