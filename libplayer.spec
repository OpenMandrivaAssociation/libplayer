%define major 2
%define libname %mklibname player %{major}
%define develname %mklibname player -d

Name: libplayer
Version: 2.0.0
Release: %mkrel 0.20100724.1
URL: http://libplayer.geexbox.org/
Source:	http://libplayer.geexbox.org/releases/%{name}-%{version}.tar.bz2
License: LGPLv2+
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries
BuildRequires: libxine-devel
BuildRequires: vlc-devel
Buildrequires: mplayer
BuildRequires: libgstreamer-devel
BuildRequires: libx11-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
libplayer is a multimedia A/V abstraction layer API. Its goal is to
interact with Enna Media Center.

libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

Its main goal is to provide an unique API that player frontends can use
to control any kind of multimedia player underneath. For example, it
provides a library to easily control MPlayer famous slave-mode.

%package test
Summary: A multimedia A/V abstraction layer API - test program
Group: System/Libraries

%description test
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

This package contains test program for libplayer.

%package -n %{libname}
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries

%description -n %{libname}
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

%package -n %{develname}
Summary: A multimedia A/V abstraction layer API
Group: System/Libraries
Provides: %{name}-devel = %{version}-%{release}
Requires: %libname = %version

%description -n %{develname}
libplayer provides a generic A/V API that relies on various multimedia
player for Linux systems. It currently supports MPlayer, xine VLC and
GStreamer only.

This package contains the headers required for compiling software that uses
the libplayer library.

%prep
%setup -q -n %{name}-%{version}

%build
%setup_compile_flags
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--libdir=%{_libdir} \
	--includedir=%{_includedir} \
	--disable-static \
	--enable-shared \
	--enable-gstreamer \
	--enable-mplayer \
	--enable-vlc \
	--enable-xine
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files test
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
