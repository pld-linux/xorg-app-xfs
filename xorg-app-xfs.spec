Summary:	Font server for X Window System
Summary(pl):	Serwer font�w dla X Window System
Summary(ru):	���������� ��� X Window System
Summary(uk):	���������� ��� X Window System
Name:		xorg-app-xfs
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xfs-%{version}.tar.bz2
# Source0-md5:	f43cb64d623b748208dfd9012d17b654
Source1:	xfs.config
Source2:	xfs.init
Source3:	xfs.sysconfig
Patch0:		xorg-xfs-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	xorg-lib-libFS-devel
BuildRequires:	xorg-lib-libXfont-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires(post,preun):	/sbin/chkconfig
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	rc-scripts
Provides:	group(xfs)
Provides:	user(xfs)
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
Pakiet zawiera serwer font�w dla X Window System. Mo�e udost�pnia�
fonty dla X serwer�w lokalnych lub zdalnych.

%description -l ru
xfs �������� ������ ������� ��� X Window System. Xfs ����� �����
������������� ������ ��������� X-��������. ��������� ������� �����
�������� ������������ ��� ������, ������������� �� ������� �������,
���� ���� ��� �� ����������� �� ��������� ����������.

%description -l uk
xfs ͦ����� ������ ����Ԧ� ��� X Window System. Xfs ����� ����
�������� ������ צ�������� X-��������. ��������� ������� �����
��������������� �Ӧ ������, �˦ ���������Φ �� �����Ҧ ����Ԧ�, ��צ��
���� ���� �� ���������Φ �� צ��������� ����'���Ҧ.

%prep
%setup -q -n xfs-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} \
	configdir=%{_sysconfdir}/X11/fs

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	configdir=%{_sysconfdir}/X11/fs

install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config
install -D %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install -D %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/xfs

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -P %{name}-xfs -g 56 -r -f xfs
%useradd -P %{name}-xfs -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs

%post
/sbin/chkconfig --add xfs
%service xfs restart "font server"

%preun
if [ "$1" = "0" ]; then
	%service xfs stop
	/sbin/chkconfig --del xfs
fi

%postun
if [ "$1" = "0" ]; then
	%userremove xfs
	%groupremove xfs
fi

%triggerpostun -- xfs
%groupadd -P %{name}-xfs -g 56 -r -f xfs
%useradd -P %{name}-xfs -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs
/sbin/chkconfig --add xfs
/sbin/service xfs start >&2

%triggerpostun -- X11-xfs
/sbin/chkconfig --add xfs
/sbin/service xfs start >&2

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xfs
%dir %{_sysconfdir}/X11/fs
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/fs/config
%attr(754,root,root) /etc/rc.d/init.d/xfs
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/xfs
%{_mandir}/man1/xfs.1x*
