%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Send files from nautilus using with mail or IM
Name:		nautilus-sendto
Version:	3.8.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-sendto/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.25.9
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.25.9
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gthread-2.0) >= 2.25.9
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90.9
Requires:	nautilus
Obsoletes:	%{name}-gajim
Obsoletes:	%{name}-sylpheed
Obsoletes:	%{name}-thunderbird
Obsoletes:	%{name}-balsa
Obsoletes:	%{name}-devel
Obsoletes:	%{name}-bluetooth
Obsoletes:	%{name}-evolution
Obsoletes:	%{name}-pidgin
Obsoletes:	%{name}-upnp

%description
This application provides integration between nautilus and mail clients.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the email account which you want to send the file/files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%doc NEWS AUTHORS ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

