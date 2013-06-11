Summary: Send files from nautilus using with mail or IM
Name: nautilus-sendto
Version: 3.8.0
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.es.gnome.org/~telemaco/
Source0: http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/3.6/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: glib2.0-common
BuildRequires: gnome-common
BuildRequires: gtk-doc
BuildRequires: pkgconfig(glib-2.0) >= 2.25.9
BuildRequires: pkgconfig(gthread-2.0) >= 2.25.9
BuildRequires: pkgconfig(gmodule-2.0) >= 2.25.9
BuildRequires: pkgconfig(gtk+-3.0) >= 2.90.9
BuildRequires: pkgconfig(libnautilus-extension) >= 2.31.3
BuildRequires: pkgconfig(libebook-1.2) >= 3.6.0
BuildRequires: pkgconfig(libedataserverui-3.0) >= 3.6.0
BuildRequires: pkgconfig(dbus-1) >= 1.0
BuildRequires: pkgconfig(dbus-glib-1) >= 0.60
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gupnp-1.0) >= 0.13

Requires: gsettings-desktop-schemas
Requires: nautilus
Obsoletes: nautilus-sendto-sylpheed nautilus-sendto-thunderbird nautilus-sendto-balsa
#suggest the most important plugins
Suggests: %{name}-bluetooth
Suggests: %{name}-evolution

%description
This application provides integration between nautilus and mail or IM clients.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package gajim
Summary: Send files from nautilus extras
Group: Graphical desktop/GNOME
Requires: %{name} = %{version}

%description gajim
This application provides integration between nautilus and mail or IM clients.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package pidgin
Summary: Send files from nautilus to pidgin
Group: Graphical desktop/GNOME
Requires: pidgin
Requires: %{name} = %{version}
Provides: nautilus-sendto-gaim
Obsoletes: nautilus-sendto-gaim

%description pidgin
This application provides integration between nautilus and pidgin.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package upnp
Summary: Send files from nautilus via UPNP
Group: Graphical desktop/GNOME
Requires: %{name} = %{version}

%description upnp
This application provides integration between nautilus and UPNP.
It adds a Nautilus context menu component ("Send To...") and allows sending
files to UPNP media servers.

%package evolution
Summary: Send files from nautilus to evolution
Group: Graphical desktop/GNOME
Requires: evolution
Requires: %{name} = %{version}

%description evolution
This application provides integration between nautilus and evolution.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package devel
Summary: Development files for nautilus-sendto
Group: Graphical desktop/GNOME

%description devel
This package provides development files needed to build plugins upon
nautilus-sendto.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %{name}.lang
%makeinstall_std
find %buildroot -name *.la | xargs rm
%find_lang %{name}

rm -f  %{buildroot}%{_libdir}/nautilus/extensions-3.0/libnautilus-sendto.so

%files -f %{name}.lang
%doc NEWS AUTHORS ChangeLog
%{_bindir}/nautilus-sendto
%{_mandir}/man1/nautilus-sendto.1*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libnstremovable_devices.so
%{_libdir}/%{name}/plugins/libnstburn.so
%{_datadir}/nautilus-sendto/
%{_datadir}/GConf/gsettings/nautilus-sendto-convert
%{_datadir}/glib-2.0/schemas/org.gnome.Nautilus.Sendto.gschema.xml

%files gajim
%{_libdir}/%{name}/plugins/libnstgajim.so

%files pidgin
%{_libdir}/%{name}/plugins/libnstpidgin.so

%files upnp
%{_libdir}/%{name}/plugins/libnstupnp.so

%files evolution	 
%{_libdir}/%{name}/plugins/libnstevolution.so

%files devel
%dir %{_includedir}/nautilus-sendto
%{_includedir}/nautilus-sendto/nautilus-sendto-plugin.h
%{_libdir}/pkgconfig/nautilus-sendto.pc
%{_datadir}/gtk-doc/html/nautilus-sendto



%changelog
* Thu Oct  4 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Fri Dec 09 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.0.1-2
+ Revision: 739276
- bump release b/c the BS
- added BR glib2.0-common
- new version 3.0.1
- cleaned up spec
- removed mkrel, BuildRoot, defattr, clean section
- split out gajim pkg why it was combined dunno
- removed .la files
- converted BRs to pkgconfig provides

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.32.0-2
+ Revision: 666595
- mass rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581811
- update to new version 2.32.0

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 578011
- update to new version 2.31.90

* Fri Aug 27 2010 Götz Waschk <waschk@mandriva.org> 2.31.7-1mdv2011.0
+ Revision: 573465
- update to new version 2.31.7

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-2mdv2011.0
+ Revision: 568246
- rebuild for new libproxy

* Wed Aug 04 2010 Götz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565828
- new version
- replace gconf schema by gsettings

* Wed Aug 04 2010 Götz Waschk <waschk@mandriva.org> 2.28.5-1mdv2011.0
+ Revision: 565811
- update to new version 2.28.5

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.28.4-3mdv2011.0
+ Revision: 563342
- fix linking (bug #60400)

* Tue Jun 22 2010 Frederic Crozat <fcrozat@mandriva.com> 2.28.4-2mdv2010.1
+ Revision: 548545
- rebuild with latest eds

* Mon Mar 29 2010 Götz Waschk <waschk@mandriva.org> 2.28.4-1mdv2010.1
+ Revision: 528905
- update to new version 2.28.4

* Mon Mar 15 2010 Götz Waschk <waschk@mandriva.org> 2.28.3-1mdv2010.1
+ Revision: 520321
- new version
- drop patch

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.28.2-2mdv2010.1
+ Revision: 475686
- disable empathy and bluetooth plugins
- merge gajim in main package

* Wed Nov 18 2009 Funda Wang <fwang@mandriva.org> 2.28.2-1mdv2010.1
+ Revision: 467260
- add devel sub package
- new version 2.28.2

* Thu Oct 15 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.0-2mdv2010.0
+ Revision: 457651
- Do not suggest nautilus-sendto-pidgin in main package, otherwise, it pulls pidgin when installing task-gnome (in addition to empathy)

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446804
- drop patch
- new version

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1.1.7-4mdv2010.0
+ Revision: 445864
- Rebuild for new gupnp

* Sun Sep 20 2009 Götz Waschk <waschk@mandriva.org> 1.1.7-3mdv2010.0
+ Revision: 445819
- rebuild for new gupnp-av

* Thu Sep 10 2009 Götz Waschk <waschk@mandriva.org> 1.1.7-2mdv2010.0
+ Revision: 437401
- rebuild for new empathy

* Wed Sep 02 2009 Götz Waschk <waschk@mandriva.org> 1.1.7-1mdv2010.0
+ Revision: 425493
- new version
- drop patch 1

* Tue Sep 01 2009 Götz Waschk <waschk@mandriva.org> 1.1.6-2mdv2010.0
+ Revision: 423699
- fix build with new empathy

* Thu Jul 30 2009 Götz Waschk <waschk@mandriva.org> 1.1.6-1mdv2010.0
+ Revision: 404612
- new version
- drop patch 1
- readd evolution plugin

* Wed Jul 29 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-6mdv2010.0
+ Revision: 404170
- rebuild for new empathy

* Sat Jun 20 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-5mdv2010.0
+ Revision: 387498
- update build deps
- patch for new empathy
- rebuild for new empathy

* Mon May 25 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-4mdv2010.0
+ Revision: 379724
- rebuild for new empathy

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-3mdv2010.0
+ Revision: 377576
- rebuild for new empathy

* Mon May 18 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-2mdv2010.0
+ Revision: 376905
- fix build deps
- rebuild for new empathy
- disable evolution plugin

* Wed May 06 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-1mdv2010.0
+ Revision: 372653
- new version

* Mon Apr 20 2009 Götz Waschk <waschk@mandriva.org> 1.1.4.1-1mdv2009.1
+ Revision: 368425
- update to new version 1.1.4.1

* Mon Apr 20 2009 Götz Waschk <waschk@mandriva.org> 1.1.4-1mdv2009.1
+ Revision: 368356
- new version

* Fri Apr 03 2009 Götz Waschk <waschk@mandriva.org> 1.1.3-1mdv2009.1
+ Revision: 363753
- new version

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 1.1.2-3mdv2009.1
+ Revision: 356001
- rebuild for new empathy

* Tue Mar 03 2009 Götz Waschk <waschk@mandriva.org> 1.1.2-2mdv2009.1
+ Revision: 348085
- rebuild for new empathy

* Mon Feb 23 2009 Götz Waschk <waschk@mandriva.org> 1.1.2-1mdv2009.1
+ Revision: 344090
- new version
- add plugins without external deps to the main package
- suggest the most important plugins
- remove plugins for thunderbird, sylpheed and balsa

* Tue Feb 17 2009 Götz Waschk <waschk@mandriva.org> 1.1.1-4mdv2009.1
+ Revision: 341387
- rebuild for new empathy

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 1.1.1-3mdv2009.1
+ Revision: 336857
- rebuild for new empathy

* Tue Jan 13 2009 Götz Waschk <waschk@mandriva.org> 1.1.1-2mdv2009.1
+ Revision: 328944
- add upnp plugin
- fix format string

* Sat Jan 10 2009 Götz Waschk <waschk@mandriva.org> 1.1.1-1mdv2009.1
+ Revision: 328028
- new version
- add balsa and empathy plugins

* Mon Oct 13 2008 Götz Waschk <waschk@mandriva.org> 1.1.0-2mdv2009.1
+ Revision: 293138
- fix build deps
- fix bluetooth deps

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 1.1.0-1mdv2009.1
+ Revision: 291927
- new version

* Fri Aug 08 2008 Götz Waschk <waschk@mandriva.org> 1.0.1-1mdv2009.0
+ Revision: 268132
- fix build deps
- new version

* Fri Jul 04 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdv2009.0
+ Revision: 231811
- update license

* Thu Jun 12 2008 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2009.0
+ Revision: 218463
- new version

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 0.14.0-1mdv2009.0
+ Revision: 192435
- new version
- drop patch
- add thunderbird plugin

* Sun Feb 24 2008 Emmanuel Andry <eandry@mandriva.org> 0.13.2-2mdv2008.1
+ Revision: 174387
- nautilus-sendto-bluetooth requires bluez-utils

* Fri Feb 08 2008 Götz Waschk <waschk@mandriva.org> 0.13.2-1mdv2008.1
+ Revision: 163993
- new version

* Mon Jan 21 2008 Götz Waschk <waschk@mandriva.org> 0.13.1-1mdv2008.1
+ Revision: 155632
- new version
- drop patches 1,2
- fix installation

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 0.12-3mdv2008.0
+ Revision: 95062
- rebuild against pidgin 2.2.1

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.12-2mdv2008.0
+ Revision: 63490
- apply icq patch to pidgin plugin as well
- remove gaim reference from pidgin plugin

* Tue Aug 14 2007 Götz Waschk <waschk@mandriva.org> 0.12-1mdv2008.0
+ Revision: 63028
- new version
- drop patch 1
- update file list

* Wed May 09 2007 Götz Waschk <waschk@mandriva.org> 0.10-4mdv2008.0
+ Revision: 25685
- update the pidgin patch

* Wed May 02 2007 Götz Waschk <waschk@mandriva.org> 0.10-3mdv2008.0
+ Revision: 20627
- build with pidgin


* Tue Mar 13 2007 Pascal Terjan <pterjan@mandriva.org> 0.10-2mdv2007.1
+ Revision: 142428
- Add support for ICQ and AIM accounts

* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 0.10-1mdv2007.1
+ Revision: 141619
- new version
- drop patches

* Sat Mar 10 2007 Götz Waschk <waschk@mandriva.org> 0.9-2mdv2007.1
+ Revision: 140491
- fix undefined symbol that prevented nautilus from starting

* Sat Mar 10 2007 Götz Waschk <waschk@mandriva.org> 0.9-1mdv2007.1
+ Revision: 140349
- new version
- drop patch
- fix build

* Sat Jan 20 2007 Götz Waschk <waschk@mandriva.org> 0.8-7mdv2007.1
+ Revision: 111101
- reflect Claws name change

* Wed Nov 29 2006 Götz Waschk <waschk@mandriva.org> 0.8-6mdv2007.1
+ Revision: 88313
- rebuild

* Wed Oct 25 2006 Götz Waschk <waschk@mandriva.org> 0.8-5mdv2007.0
+ Revision: 72300
- bot rebuild
- bot rebuild
- rebuild for new libbtctl and new gaim

* Fri Oct 13 2006 Götz Waschk <waschk@mandriva.org> 0.8-2mdv2006.0
+ Revision: 63782
- rebuild
- Import nautilus-sendto

* Thu Oct 12 2006 G�tz Waschk <waschk@mandriva.org> 0.8-1mdv2007.1
- update file list
- drop patches
- New version 0.8

* Thu Aug 24 2006 G�tz Waschk <waschk@mandriva.org> 0.7-4mdv2007.0
- pass a URI to the plugin when sending an archive instead of a filename

* Sat Aug 05 2006 Götz Waschk <waschk@mandriva.org> 0.7-1mdv2007.0
- reuild for new dbus

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 0.7-1mdv2007.0
- rebuild for new e-d-s

* Mon Jun 26 2006 Götz Waschk <waschk@mandriva.org> 0.7-1mdv2007.0
- New release 0.7

* Sun Jun 25 2006 G�tz Waschk <waschk@mandriva.org> 0.6-1mdv2007.0
- update file list
- New release 0.6

* Sun Jun 18 2006 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2007.0
- rebuild for new libbluetooth

* Sun Apr 16 2006 G�tz Waschk <waschk@mandriva.org> 0.5-1mdk
- bump deps
- drop patch 0
- New release 0.5

* Thu Feb 16 2006 G�tz Waschk <waschk@mandriva.org> 0.4-9mdk
- fix buildrequires

* Wed Dec 14 2005 G�tz Waschk <waschk@mandriva.org> 0.4-8mdk
- patch for new libbtctl
- use mkrel

* Sun Nov 20 2005 Götz Waschk <waschk@mandriva.org> 0.4-7mdk
- rebuild for new openssl

* Fri Oct 07 2005 G�tz Waschk <waschk@mandriva.org> 0.4-6mdk
- e-d-s 1.4 rebuild

* Mon Sep 05 2005 Michael Scherer <misc@mandriva.org> 0.4-5mdk
- Rebuild to avoid libglitz deps

* Mon Aug 22 2005 G�tz Waschk <waschk@mandriva.org> 0.4-4mdk
- drop patch

* Wed Aug 10 2005 Götz Waschk <waschk@mandriva.org> 0.4-3mdk
- split the plugins into subpackages

* Thu Aug 04 2005 Götz Waschk <waschk@mandriva.org> 0.4-2mdk
- enable bluetooth

* Thu Aug 04 2005 Götz Waschk <waschk@mandriva.org> 0.4-1mdk
- New release 0.4

* Fri Apr 22 2005 G�tz Waschk <waschk@mandriva.org> 0.3-3mdk
- rebuild for new e-d-s

* Thu Jan 20 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.3-2mdk
- fix buildrequires

* Tue Jan 18 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.3-1mdk
- update file list
- source URL
- New release 0.3

* Tue Nov 09 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.2-1mdk
- update file list
- requires new libgnomeui
- New release 0.2-1

* Sat Sep 04 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1-2mdk
- fix buildrequires

* Fri Sep 03 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.1-1mdk
- initial package

