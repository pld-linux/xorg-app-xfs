Summary:	Font server for X Window System
Summary(pl):	Serwer fontСw dla X Window System
Summary(ru):	Фонтсервер для X Window System
Summary(uk):	Фонтсервер для X Window System
Name:		xorg-app-xfs
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xfs-%{version}.tar.bz2
# Source0-md5:	fc9ed8773c67bdd54a80c51e567e0076
Patch0:		xfs-man.patch
Patch1:		xfs-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-util-util-macros
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
%patch1 -p1

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/fs/config
%{_mandir}/man1/*.1*
