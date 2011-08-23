Name: libdaemon
Version: 0.14
Release: 1%{?dist}
Summary: Library for writing UNIX daemons
Group: System Environment/Libraries
License: LGPLv2+
URL: http://0pointer.de/lennart/projects/libdaemon/
Source0: http://0pointer.de/lennart/projects/libdaemon/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Requires lynx to build the docs
BuildRequires:  lynx

%description
libdaemon is a lightweight C library which eases the writing of UNIX daemons.
It consists of the following parts:
* A wrapper around fork() which does the correct daemonization
  procedure of a process
* A wrapper around syslog() for simpler and compatible log output to
  Syslog or STDERR
* An API for writing PID files
* An API for serializing UNIX signals into a pipe for usage with
  select() or poll()
* An API for running subprocesses with STDOUT and STDERR redirected
  to syslog.

%package devel
Group: Development/Libraries
Summary: Libraries and header files for libdaemon development
Requires: libdaemon = %{version}-%{release}
Requires: pkgconfig

%description devel
The libdaemon-devel package contains the header files and libraries
necessary for developing programs using libdaemon.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm $RPM_BUILD_ROOT/%{_datadir}/doc/libdaemon/README
rm $RPM_BUILD_ROOT/%{_datadir}/doc/libdaemon/README.html
rm $RPM_BUILD_ROOT/%{_datadir}/doc/libdaemon/style.css

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE README
%{_libdir}/*so.*

%files devel
%defattr(-,root,root)
%doc LICENSE README
%doc doc/README.html doc/style.css
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Oct 18 2009 Lennart Poettering <lpoetter@redhat.com> - 0.14-1
- New release 0.14

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Lennart Poettering <lpoetter@redhat.com> - 0.13-1
- New release 0.13

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12-3
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.12-2
- Rebuild for selinux ppc32 issue.

* Wed Jul 11 2007 Lennart Poettering <lpoetter@redhat.com> - 0.12-1
- Update to upstream 0.12. (Basically just includes patch from 0.11-2)

* Mon Jul  2 2007 Dan Williams <dcbw@redhat.com> - 0.11-2
- Fix double-free bug when closing daemon file descriptor (avahi.org #148)

* Fri Jun 22 2007 Martin Bacovsky <mbacovsk@redhat.com> - 0.11-1
- Upgrade to new upstream version 0.11

* Thu Apr  5 2007 Martin Bacovsky <mbacovsk@redhat.com> - 0.10-4
- Resolves: #222855: fileconflict for /usr/share/doc/libdaemon-devel-0.10/Makefile 

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.10-3.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jason Vas Dias <jvdias@redhat.com> - 0.10-3
- rebuild for new gcc, glibc, glibc-kernheaders

* Mon Jan 06 2006 Jason Vas Dias <jvdias@redhat.com> - 0.10-2
- rebuild for new gcc / glibc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com> - 0.10-1.1
- rebuild on new gcc

* Wed Dec  7 2005 Jason Vas Dias <jvdias@redhat.com> - 0.10-1
- Update to 0.10

* Thu Oct 20 2005 Alexander Larsson <alexl@redhat.com> - 0.8-1
- Update to 0.8, move from extras to core, split out devel package

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.6-6
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu May 13 2004 Aaron Bennett <aaron.bennett@olin.edu> 0:0.6-0.fdr.4
- Added post and postun scripts to run ldconfig
- changed group to standard System/Libraries group
- removed libtool *.la files

* Tue May 4 2004 Aaron Bennett <aaron.bennett@olin.edu> 0:0.6.-0.fdr.3
- Signed packaged with GPG key

* Tue May 4 2004 Aaron Bennett <aaron.bennett@olin.edu> - 0:0.6-0.fdr.2
- Changed URL and Source tag for Fedora.us packaging compliance
- Incremented release tag

* Thu Apr 29 2004 Aaron Bennett <abennett@olin.edu> - 0:0.6-1
- Changed to version 0.6 of libdaemon

* Wed Mar 31 2004 Aaron Bennett <abennett@olin.edu>
- Initial build.
