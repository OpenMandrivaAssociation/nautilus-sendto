%define name nautilus-sendto
%define version 2.32.0
%define release %mkrel 1

Summary: Send files from nautilus using with mail or IM
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.es.gnome.org/~telemaco/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libnautilus-devel >= 2.13.3
BuildRequires: libglade2.0-devel
BuildRequires: dbus-glib-devel
BuildRequires: pidgin-devel
BuildRequires: gupnp-av-devel
BuildRequires: evolution-data-server-devel evolution-devel	 
#gw libtool dep of evolution: 	     
BuildRequires: gnome-pilot-devel 	      
BuildRequires: intltool
BuildRequires: gnome-common gtk-doc
Requires: nautilus
Provides: nautilus-sendto-gajim 
Obsoletes: nautilus-sendto-gajim nautilus-sendto-sylpheed nautilus-sendto-thunderbird nautilus-sendto-balsa
#suggest the most important plugins
Suggests: %name-bluetooth %name-evolution

%description
This application provides integration between nautilus and mail or IM clients.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package pidgin
Summary: Send files from nautilus to pidgin
Group: Graphical desktop/GNOME
Requires: pidgin
Requires: %name = %version
Provides: nautilus-sendto-gaim
Obsoletes: nautilus-sendto-gaim

%description pidgin
This application provides integration between nautilus and pidgin.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.


%package upnp
Summary: Send files from nautilus via UPNP
Group: Graphical desktop/GNOME
Requires: %name = %version

%description upnp
This application provides integration between nautilus and UPNP.
It adds a Nautilus context menu component ("Send To...") and allows sending
files to UPNP media servers.

%package evolution
Summary: Send files from nautilus to evolution
Group: Graphical desktop/GNOME
Requires: evolution
Requires: %name = %version

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
%setup -q -n %name-%version

%build
#gw: https://bugzilla.gnome.org/show_bug.cgi?id=597270 
%define _disable_ld_as_needed 1
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/nautilus/extensions-*/*.la \
      %buildroot%_libdir/pidgin/*.la \
      %buildroot%_libdir/%name/plugins/*.la
rm -f %buildroot%_libdir/nautilus-sendto/plugins/libnstbluetooth.so
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS AUTHORS ChangeLog
%_bindir/nautilus-sendto
%_libdir/nautilus/extensions-2.0/libnautilus-sendto.so
%_mandir/man1/nautilus-sendto.1*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libnstburn.so
%_libdir/%name/plugins/libnstgajim.so
%_libdir/%name/plugins/libnstremovable_devices.so
%_datadir/nautilus-sendto/
%_datadir/GConf/gsettings/nautilus-sendto-convert
%_datadir/glib-2.0/schemas/org.gnome.Nautilus.Sendto.gschema.xml

%files pidgin
%defattr(-,root,root)
%_libdir/%name/plugins/libnstpidgin.so

%files upnp
%defattr(-,root,root)
%_libdir/%name/plugins/libnstupnp.so

%files evolution	 
%defattr(-,root,root)	 
%_libdir/%name/plugins/libnstevolution.so

%files devel
%defattr(-,root,root)
%dir %_includedir/nautilus-sendto
%_includedir/nautilus-sendto/nautilus-sendto-plugin.h
%_libdir/pkgconfig/nautilus-sendto.pc
%_datadir/gtk-doc/html/nautilus-sendto

