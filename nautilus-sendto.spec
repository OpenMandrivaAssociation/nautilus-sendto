%define name nautilus-sendto
%define version 1.1.1
%define release %mkrel 4

Summary: Send files from nautilus using evolution or gaim
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/%{name}-%{version}.tar.bz2
Patch: nautilus-sendto-1.1.1-format-string.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.es.gnome.org/~telemaco/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evolution-data-server-devel
BuildRequires: libnautilus-devel >= 2.13.3
BuildRequires: dbus-glib-devel
BuildRequires: pidgin-devel
BuildRequires: gajim
BuildRequires: empathy-devel
BuildRequires: gupnp-av-devel
BuildRequires: intltool
Requires: nautilus
#gw it's useless without at least one plugin
Requires: %name-plugin = %version

%description
This application provides integration between nautilus, evolution and gaim.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package pidgin
Summary: Send files from nautilus to pidgin
Group: Graphical desktop/GNOME
Requires: pidgin
Requires: %name = %version
Provides: %name-plugin = %version-%release
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
Provides: %name-plugin = %version-%release

%description empathy
This application provides integration between nautilus and empathy.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package gajim
Summary: Send files from nautilus to gajim
Group: Graphical desktop/GNOME
Requires: gajim
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description gajim
This application provides integration between nautilus and gajim.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package evolution
Summary: Send files from nautilus to evolution
Group: Graphical desktop/GNOME
Requires: evolution
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description evolution
This application provides integration between nautilus and evolution.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package thunderbird
Summary: Send files from nautilus to thunderbird
Group: Graphical desktop/GNOME
Requires: mozilla-thunderbird
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description thunderbird
This application provides integration between nautilus and thunderbird.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package sylpheed
Summary: Send files from nautilus to sylpheed
Group: Graphical desktop/GNOME
Requires:sylpheed
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description sylpheed
This application provides integration between nautilus and sylpheed.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package balsa
Summary: Send files from nautilus to bals
Group: Graphical desktop/GNOME
Requires:balsa
Requires: %name = %version
Provides: %name-plugin = %version-%release

%description balsa
This application provides integration between nautilus and balsa.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package bluetooth
Summary: Send files from nautilus to bluetooth
Group: Graphical desktop/GNOME
Requires: %name = %version
Provides: %name-plugin = %version-%release
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
Provides: %name-plugin = %version-%release

%description upnp
This application provides integration between nautilus and UPNP.
It adds a Nautilus context menu component ("Send To...") and allows sending
files to UPNP media servers.


%prep
%setup -q -n %name-%version
%patch -p1

%build
%configure2_5x
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

%files sylpheed
%defattr(-,root,root)
%_libdir/%name/plugins/libnstsylpheed.so

%files balsa
%defattr(-,root,root)
%_libdir/%name/plugins/libnstbalsa.so

%files evolution
%defattr(-,root,root)
%_libdir/%name/plugins/libnstevolution.so

%files thunderbird
%defattr(-,root,root)
%_libdir/%name/plugins/libnstthunderbird.so

%files bluetooth
%defattr(-,root,root)
%_libdir/%name/plugins/libnstbluetooth.so

%files upnp
%defattr(-,root,root)
%_libdir/%name/plugins/libnstupnp.so

