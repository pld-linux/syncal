Summary:	synchronizes palm DateBook with ical
Summary(pl):	synchronizuje palmowy DateBook z ical-em
Name:		syncal
Version:	0.8.7
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://hopf.math.nwu.edu/syncal/%{name}-%{version}.tar.gz
# Source0-md5:	860b2924c254c746401d286db026ffd9
Patch0:		syncal-newpisock.patch
URL:		http://hopf.math.nwu.edu/syncal/
BuildRequires:	pilot-link-devel >= 0.10.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc *.tcl

%description
Syncal lets owners of Palm OS devices (Palm, Sony CLIE etc)
synchronise their DateBook (and DateBk3/DateBk4) appointments with Ical
callendar.

%description -l pl
Syncal pozwala u¿ytkownikom urz±dzeñ z Palm OS (Palm, Sony CLIE itd.)
synchronizowaæ terminy i spotkania z DateBooka (a tak¿e
DateBk3/DateBk4) z kalendarzem programu Ical.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install syncal $RPM_BUILD_ROOT%{_bindir}
install syncal.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog GETTING_STARTED README* ical.patch user.tcl
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
