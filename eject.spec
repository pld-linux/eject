Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare Datenträger aus und steuert Auswurf 
Summary(fr):	éjecte un support éjectable et commande l'éjection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(tr):	Eject yeteneði olan aygýtlarý kontrol eder
Name:		eject
Version:	2.0.2
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source:		http://metalab.unc.edu/pub/Linux/utils/disk-management/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

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

%description -l pl
Program do automatycznego otwierania szuflad w urz±dzeniach CDROM, Jaz,
ZIP floppy (na maszynach SPARC) oraz innych.

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
make CFLAGS="-Wall $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s eject $RPM_BUILD_ROOT/usr/bin/eject
install eject.1 $RPM_BUILD_ROOT/usr/man/man1/eject.1

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/* \
	README ChangeLog
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) /usr/bin/eject
/usr/man/man1/*

%changelog
* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.0.2-3]
- removed man group from man pages,
- changed base Source url,
- added Group(pl),
- gzipping man pages.

* Fri Dec 3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.5-6d]
- added patch for proper compilation on kernel 2.1.x.
- build for Tornado,
- some changes...

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
