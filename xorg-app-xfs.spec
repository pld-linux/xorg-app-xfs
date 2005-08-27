# $Rev: 3388 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xfs application
Summary(pl):	Aplikacja xfs
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
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xfs-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xfs application.

%description -l pl
Aplikacja xfs.


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
%attr(755,root,wheel) %{_bindir}/*
%{_libdir}/X11/fs/config
%{_mandir}/man1/*.1*
