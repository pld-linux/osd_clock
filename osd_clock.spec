# TODO:
# - desktop file and icons
Summary:	Minimalist on screen OSD clock for X11
Summary(pl):	Minimalistyczny zegar OSD dla X11
Name:		osd_clock
Version:	0.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://leftorium.net/software/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://leftorium.net/software.phtml
BuildRequires:	XFree86-devel
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
OSD clock designed for minimalist desktops. Cushy fly and speedy.

%description -l pl
Zegar OSD stworzony dla minimalistycznych desktopów. Szybki i lekki.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix} MANDIR=%{_mandir}

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
