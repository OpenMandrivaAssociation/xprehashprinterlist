Name:		xprehashprinterlist
Version:	1.0.1
Release:	%mkrel 8
Summary:	Recomputes the list of available printers
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxp-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
XpRehashPrinterList causes the X Print Server to recompute (update)
its list of available printers, and update the attributes for the
printers. The intended usage of this routine is in a special tool
that a system administrator can run after changing the printer
topology.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xprehashprinterlist
%{_mandir}/man1/xprehashprinterlist.1*
