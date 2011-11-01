%define name tintii
%define version 2.5.3
%define release %mkrel 1

Summary:    Color photo image converter
Name:       %{name}
Version:    %{version}
Release:    %{release}
License:    GPLv2
Group:      Graphics
Source0:    http://www.indii.org/software/tintii/%{name}-%{version}.tar.gz
Source1:    %{name}.png
URL:        http://www.indii.org/software/tintii
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gcc-c++
BuildRequires: boost-devel 
BuildRequires: scons 
BuildRequires: rcs 
BuildRequires: flex
BuildRequires: wxGTK2.8-devel
BuildRequires: libgomp-devel
BuildRequires: doxygen
Requires:   glibc >= 2.10.1
Requires:   libstdc++6 >= 4.4.1
Obsoletes: %name < %version


%description
Tintii takes full color photos and processes them into black and white with some select regions highlighted in color. 
The technique is known as colour popping or selective coloring – tintii makes it easy. Think Schindler’s List’s little 
girl in red, or the dramatic style of Sin City. tintii takes a color photo and cleverly separates it into a handful of
major hues. You then select which colours to pop, and the rest become black & white.

%description -l de
Mit Tintii Photo Filter verleiht man Digitalfotos einen ganz speziellen Schwarz-Weiß-Look. Die kostenlose Software 
verwandelt alle bis auf einige ausgewählte farbige Bereiche einer Fotografie in Graustufen. Das Ergebnis ist ein 
Schwarzweiß-Bild, aus dem nur noch das gewünschte Objekt in einer zuvor festgelegten Farbe hervorsticht.

Zunächst öffnet man in Tintii Photo Filter das zu bearbeitende Foto und wählt aus den automatisch durch die Freeware 
erzeugten Miniaturvorschaubildern das aus, das dem späteren Ergebnis am Nächsten kommt. Per Mausklick sucht man sich die 
gewünschte Farbe heraus und gibt dem Bild anhand weiterer Einstellungsoptionen den letzen Schliff.

Tintii Photo Filter unterstützt die folgenden Formate:
BMP, PNG, JPG, TIF, GIF, PNM, PCX, ICO, CUR, ANI, TGA, XPM


%prep
%setup -q

%build

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}

# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m  644 %SOURCE1 %{buildroot}%{_datadir}/pixmaps

# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
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


%clean
rm -rf %{buildroot}

%post
%{update_menus}


%postun
%{clean_menus}


%files
%defattr(-, root, root)
%doc README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
