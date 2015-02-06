Name:		tintii
Version:	2.6.1
Release:	2
Summary:	Color photo image converter
License:	GPLv2+
Group:		Graphics
Source0:	http://www.indii.org/files/tint/releases/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Patch0:		tintii-2.6.0-mdv-buildfix.patch
URL:		http://www.indii.org/software/tintii
BuildRequires:	boost-devel
BuildRequires:	scons
BuildRequires:	rcs
BuildRequires:	flex
BuildRequires:	wxgtku-devel
BuildRequires:	libgomp-devel
BuildRequires:	doxygen
BuildRequires:	imagemagick

%description
Tintii takes full color photos and processes them into black and white
with some select regions highlighted in color. The technique is known as color
popping or selective coloring – tintii makes it easy. Think Schindler’s List’s
little girl in red, or the dramatic style of Sin City. Tintii takes a color
photo and cleverly separates it into a handful of major hues. You then select
which colours to pop, and the rest become black & white.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{name} %{buildroot}%{_bindir}

# icon
%__install -d %{buildroot}%{_iconsdir}/hicolor/16x16/apps/ %{buildroot}%{_iconsdir}/hicolor/32x32/apps/
convert -geometry 16x16 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -geometry 32x32 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -Dm 644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

# menu-entry
%__install -d %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Encoding=UTF-8
Terminal=false
Name=Tintii
Comment=Color photo image converter
Exec=%{name}
Icon=%{name}
Categories=Graphics;Viewer;X-MandrivaLinux-Graphics-Utility;
EOF

%files
%defattr(-, root, root)
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.*


%changelog
* Sat Mar 17 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.6.1-1mdv2011.0
+ Revision: 785454
- new version 2.6.1

* Mon Mar 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.6.0-1
+ Revision: 784413
- fix license
- new version 2.6.0

* Thu Jan 12 2012 Andrey Bondrov <abondrov@mandriva.org> 2.5.3-2
+ Revision: 760457
- Rebuild against utf8 wxGTK2.8, spec cleanup

* Wed Nov 02 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.5.3-1
+ Revision: 709960
- imported package tintii

