# TODO:
# - desktop file and icons
Summary:	Minimalist on screen OSD clock for X11
Summary(pl.UTF-8):	Minimalistyczny zegar OSD dla X11
Name:		osd_clock
Version:	0.5
Release:	6
License:	GPL
Group:		X11/Applications
Source0:	http://leftorium.net/software/%{name}-%{version}.tar.gz
# Source0-md5:	a6f30cc032336b34c10eb06602dc43ff
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-0.5-xosd-2.0.patch
Patch2:		%{name}-amd64.patch
URL:		http://leftorium.net/software.phtml
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSD clock designed for minimalist desktops. Cushy fly and speedy.

%description -l pl.UTF-8
Zegar OSD stworzony dla minimalistycznych desktopów. Szybki i lekki.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%if "%{_lib}" == "lib64"
%patch -P2 -p1
%endif

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I. " \
	LDFLAGS=""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
