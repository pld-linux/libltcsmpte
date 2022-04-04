#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Encode/decode linear SMPTE timecode
Summary(pl.UTF-8):	Kodowanie/dekodowanie liniowego kodu czasowego SMPTE
Name:		libltcsmpte
Version:	0.4.4
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/ltcsmpte/%{name}-%{version}.tar.gz
# Source0-md5:	9fe2156ca0ee7c846b94390030bf7efe
URL:		http://ltcsmpte.sourceforge.net/
BuildRequires:	doxygen
BuildRequires:	gmp-devel
BuildRequires:	graphviz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library functions to read and write linear/longitudinal audio
timecode.

%description -l pl.UTF-8
Funkcje biblioteczne do odczytu i zapisu liniowego kodu czasowego.

%package devel
Summary:	Header files for ltcsmpte library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ltcsmpte
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ltcsmpte library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ltcsmpte.

%package static
Summary:	Static ltcsmpte library
Summary(pl.UTF-8):	Statyczna biblioteka ltcsmpte
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ltcsmpte library.

%description static -l pl.UTF-8
Statyczna biblioteka ltcsmpte.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libltcsmpte.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libltcsmpte.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libltcsmpte.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libltcsmpte.so
%{_includedir}/ltcsmpte
%{_pkgconfigdir}/ltcsmpte.pc
%{_mandir}/man3/FrameRate.3*
%{_mandir}/man3/SMPTEFrame.3*
%{_mandir}/man3/SMPTEFrameExt.3*
%{_mandir}/man3/SMPTETime.3*
%{_mandir}/man3/framerate.h.3*
%{_mandir}/man3/ltcsmpte.h.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libltcsmpte.a
%endif
