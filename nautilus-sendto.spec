%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Send files from nautilus using with mail or IM
Name:		nautilus-sendto
Version:	3.0.3
Release:	1
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
BuildRequires:	pkgconfig(glib-2.0) >= 2.25.9
BuildRequires:	pkgconfig(gthread-2.0) >= 2.25.9
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.25.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.9
BuildRequires:	pkgconfig(libnautilus-extension) >= 2.31.3
BuildRequires:	pkgconfig(libebook-1.2) >= 1.5.3
BuildRequires:	pkgconfig(dbus-1) >= 1.0
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gupnp-1.0) >= 0.13
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
Requires:	nautilus
Provides:	nautilus-sendto-gajim 
Obsoletes:	nautilus-sendto-gajim
Obsoletes:	nautilus-sendto-sylpheed
Obsoletes:	nautilus-sendto-thunderbird
Obsoletes:	nautilus-sendto-balsa
#suggest the most important plugins
Suggests:	%{name}-bluetooth
Suggests:	%{name}-evolution

%description
This application provides integration between nautilus and mail or IM clients.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email or IM account which you want to send
the file/files.

%package pidgin
Summary:	Send files from nautilus to pidgin
Group:		Graphical desktop/GNOME
Requires:	pidgin
Requires:	%{name} = %{version}-%{release}
Obsoletes:	nautilus-sendto-gaim

%description pidgin
This application provides integration between nautilus and pidgin.  It
adds a Nautilus context menu component ("Send To...") and features a
dialog for insert the IM account which you want to send the file/files.

%package upnp
Summary:	Send files from nautilus via UPNP
Group:		Graphical desktop/GNOME
Requires:	%{name} = %{version}-%{release}

%description upnp
This application provides integration between nautilus and UPNP.
It adds a Nautilus context menu component ("Send To...") and allows sending
files to UPNP media servers.

%package evolution
Summary:	Send files from nautilus to evolution
Group:		Graphical desktop/GNOME
Requires:	evolution
Requires:	%{name} = %{version}-%{release}

%description evolution
This application provides integration between nautilus and evolution.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email acount which you want to send the
file/files.

%package devel
Summary:	Development files for nautilus-sendto
Group:		Graphical desktop/GNOME

%description devel
This package provides development files needed to build plugins upon
nautilus-sendto.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot} %name.lang
%makeinstall_std
%find_lang %name

find %buildroot -name *.la | xargs rm 
# the nautilus package now provides its own sendto plugin
rm -f %buildroot%_libdir/nautilus/extensions-*/libnautilus-sendto.so

%files -f %name.lang
%doc NEWS AUTHORS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libnstburn.so
%{_libdir}/%{name}/plugins/libnstgajim.so
%{_libdir}/%{name}/plugins/libnstremovable_devices.so
%{_datadir}/%{name}/
%{_datadir}/GConf/gsettings/%{name}-convert
%{_datadir}/glib-2.0/schemas/org.gnome.Nautilus.Sendto.gschema.xml

%files pidgin
%{_libdir}/%{name}/plugins/libnstpidgin.so

%files upnp
%{_libdir}/%{name}/plugins/libnstupnp.so

%files evolution	 
%{_libdir}/%{name}/plugins/libnstevolution.so

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/       
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
