Summary:     ejects ejectable media and controls auto ejection
Summary(de): wirft austauschbare Datenträger aus und steuert den automatischen Auswurf 
Summary(fr): éjecte un support éjectable et commande l'éjection automatique
Summary(tr): Eject yeteneði olan aygýtlarý kontrol eder
Name:        eject
Version:     1.5
Release:     6
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://sunsite.unc.edu/pub/Linux/utils/disk-management/%{name}-%{version}.tar.gz
Patch0:      eject-make.patch
Patch1:      eject-device.patch
Patch2:      eject-kernel21.patch
BuildRoot:   /tmp/%{name}-%{version}-root

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de
Dieses Programm ermöglicht auf SPARC-Rechnern das Auswerfen 
von Datenträgern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l fr
Ce programme permet à l'utilisateur d'éjecter un support autoéjectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l tr
Bu yazýlým paketi ile kullanýcýya 'eject' yeteneði olan aygýtlarý kontrol
olanaðý verilmektedir. Bu yeteneði olan aygýtlar arasýnda CD-ROM'lar, Zip
sürücüleri ve bazý disket sürücüleri yer alýr.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p0

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s eject $RPM_BUILD_ROOT/usr/bin/eject
install eject.1 $RPM_BUILD_ROOT/usr/man/man1/eject.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README ChangeLog
%attr(755, root, root) /usr/bin/eject
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Fri Dec 3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5-6]
- added patch for proper compilation on kernel 2.1.x.

* Mon Sep 28 1998 Marcin 'Qrczak' Kowalczyk <qrczak@knm.org.pl>
  [1.5-5]
- use %%{name} and %%{version} macros,
- added full %attr description in %files,
- `mkdir -p' replaced with more standard `install -d'.

* Tue Aug  4 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Wed Jul 15 1998 Donnie Barnes <djb@redhat.com>
- added small patch to 1.5 for longer device names

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 15 1997 Donnie Barnes <djb@redhat.com>
- upgraded to 1.5
- various spec file clean ups
- eject rocks!

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc.
