Summary:	Front-end for MAME
Summary(pl.UTF-8):	Front-end dla MAME
Name:		gmameui
Version:	0.2.11
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/gmameui/%{name}-%{version}.tar.gz
# Source0-md5:	06c3b2fd51ee6fa0c0f36881168102c7
Patch0:		%{name}-desktop.patch
URL:		http://gmameui.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	gnome-doc-utils
BuildRequires:	gtk+2-devel
BuildRequires:	libarchive-devel
BuildRequires:	libglade2-devel
BuildRequires:	rpmbuild(macros) >= 1.268
Suggests:	sdlmame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GMAMEUI is a front-end for MAME on Linux. It helps with the easy
playing and configuring of MAME games.

%description -l pl.UTF-8
GMAMEUI to linuksowy front-end dla MAME. Ułatwia on granie i
konfigurację w gry dla MAME.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/gmameui
%{_datadir}/%{name}
%{_desktopdir}/gmameui.desktop
%{_mandir}/man6/gmameui.6*
%{_pixmapsdir}/gmameui.png
