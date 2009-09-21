%define name nautilus-sendto
%define version 2.28.0
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
BuildRequires: gajim
BuildRequires: empathy-devel >= 2.27.91.1-2mdv
BuildRequires: gupnp-av-devel
BuildRequires: evolution-data-server-devel evolution-devel	 
#gw libtool dep of evolution: 	     
BuildRequires: gnome-pilot-devel 	      
BuildRequires: intltool
BuildRequires: gnome-common
Requires: nautilus
Obsoletes: nautilus-sendto-sylpheed nautilus-sendto-thunderbird nautilus-sendto-balsa
#suggest the most important plugins
Suggests: %name-pidgin %name-bluetooth %name-evolution


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

%package empathy
Summary: Send files from nautilus to empathy
Group: Graphical desktop/GNOME
Requires: empathy
Requires: %name = %version

%description empathy
This application provides integration between nautilus and empathy.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package gajim
Summary: Send files from nautilus to gajim
Group: Graphical desktop/GNOME
Requires: gajim
Requires: %name = %version

%description gajim
This application provides integration between nautilus and gajim.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.


%package bluetooth
Summary: Send files from nautilus to bluetooth
Group: Graphical desktop/GNOME
Requires: %name = %version
Requires: bluez-gnome

%description bluetooth
This application provides integration between nautilus and bluetooth.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the bluetooth device which you want to send the
file/files.

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

%prep
%setup -q -n %name-%version

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std
%find_lang %name
rm -f %buildroot%_libdir/nautilus/extensions-*/*.la \
      %buildroot%_libdir/pidgin/*.la \
      %buildroot%_libdir/%name/plugins/*.la
%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas nst

%preun
%preun_uninstall_gconf_schemas nst

%files -f %name.lang
%defattr(-,root,root)
%doc NEWS AUTHORS ChangeLog
%_sysconfdir/gconf/schemas/nst.schemas
%_bindir/nautilus-sendto
%_libdir/nautilus/extensions-2.0/libnautilus-sendto.so
%_mandir/man1/nautilus-sendto.1*
%dir %_libdir/%name/
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/libnstburn.so
%_libdir/%name/plugins/libnstremovable_devices.so
%_datadir/nautilus-sendto/

%files pidgin
%defattr(-,root,root)
%_libdir/pidgin/nautilus.so
%_libdir/%name/plugins/libnstpidgin.so

%files empathy
%defattr(-,root,root)
%_libdir/%name/plugins/libnstempathy.so

%files gajim
%defattr(-,root,root)
%_libdir/%name/plugins/libnstgajim.so

%files bluetooth
%defattr(-,root,root)
%_libdir/%name/plugins/libnstbluetooth.so

%files upnp
%defattr(-,root,root)
%_libdir/%name/plugins/libnstupnp.so

%files evolution	 
%defattr(-,root,root)	 
%_libdir/%name/plugins/libnstevolution.so	 
