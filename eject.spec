Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare Datenträger aus und steuert Auswurf 
Summary(fr):	éjecte un support éjectable et commande l'éjection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(tr):	Eject yeteneði olan aygýtlarý kontrol eder
Name:		eject
Version:	2.0.2
Release:	4
License:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://metalab.unc.edu/pub/Linux/utils/disk-management/%{name}-%{version}.tar.gz
URL:		http://www.pobox.com/~tranter/eject.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de
Dieses Programm ermöglicht auf SPARC-Rechnern das Auswerfen von
Datenträgern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l fr
Ce programme permet à l'utilisateur d'éjecter un support autoéjectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l pl
Program do automatycznego otwierania szuflad w urz±dzeniach CDROM,
Jaz, ZIP floppy (na maszynach SPARC) oraz innych.

%description -l tr
Bu yazýlým paketi ile kullanýcýya 'eject' yeteneði olan aygýtlarý
kontrol olanaðý verilmektedir. Bu yeteneði olan aygýtlar arasýnda
CD-ROM'lar, Zip sürücüleri ve bazý disket sürücüleri yer alýr.

%prep
%setup -q

%build
make CFLAGS="-Wall $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s eject $RPM_BUILD_ROOT%{_bindir}/eject
install eject.1 $RPM_BUILD_ROOT%{_mandir}/man1/eject.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README ChangeLog
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/eject
%{_mandir}/man1/*
