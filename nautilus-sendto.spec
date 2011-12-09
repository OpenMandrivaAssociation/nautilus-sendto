Summary: Send files from nautilus using with mail or IM
Name: nautilus-sendto
Version: 3.0.1
Release: 1
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.es.gnome.org/~telemaco/
Source0: http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: glib2.0-common
BuildRequires: gnome-common
BuildRequires: gtk-doc
BuildRequires: pkgconfig(glib-2.0) >= 2.25.9
BuildRequires: pkgconfig(gthread-2.0) >= 2.25.9
BuildRequires: pkgconfig(gmodule-2.0) >= 2.25.9
BuildRequires: pkgconfig(gtk+-3.0) >= 2.90.9
BuildRequires: pkgconfig(libnautilus-extension) >= 2.31.3
BuildRequires: pkgconfig(libebook-1.2) >= 1.5.3
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

