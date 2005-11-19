Summary:	Font server for X Window System
Summary(pl):	Serwer fontСw dla X Window System
Summary(ru):	Фонтсервер для X Window System
Summary(uk):	Фонтсервер для X Window System
Name:		xorg-app-xfs
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC2/app/xfs-%{version}.tar.bz2
# Source0-md5:	c3a75285b1fb6ad4cd1d80ab6f7270ea
Patch0:		xorg-xfs-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
Obsoletes:	X11-xfs
Obsoletes:	XFree86-xfs
Obsoletes:	xfs
Obsoletes:	xfsft
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a font server for X Window System. You can serve fonts to
other X servers remotely with this package, and the remote system will
be able to use all fonts installed on the font server, even if they
are not installed on the remote computer.

%description -l pl
Pakiet zawiera serwer fontСw dla X Window System. Mo©e udostЙpniaФ
fonty dla X serwerСw lokalnych lub zdalnych.

%description -l ru
xfs содержит сервер шрифтов для X Window System. Xfs также может
предоставлять шрифты удаленным X-серверам. Удаленная система будет
способна использовать все шрифты, установленные на сервере шрифтов,
даже если они не установлены на удаленном компьютере.

%description -l uk
xfs м╕стить сервер шрифт╕в для X Window System. Xfs також може
надавати шрифти в╕ддаленим X-серверам. В╕ддалена система зможе
використовувати ус╕ шрифти, як╕ встановлен╕ на сервер╕ шрифт╕в, нав╕ть
якщо вони не встановлен╕ на в╕ддаленому комп'ютер╕.

%prep
%setup -q -n xfs-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	appmandir=%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/fs/config
%{_mandir}/man1/*.1x*
