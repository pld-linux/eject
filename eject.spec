Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare DatentrДger aus und steuert Auswurf
Summary(es):	Expulsa medias expulsables y controla autoexpulsiСn
Summary(fr):	Иjecte un support Иjectable et commande l'Иjection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(pt_BR):	Ejeta mМdias ejetАveis e controla auto-ejeГЦo
Summary(ru):	Программа, выталкивающая сменные носители из накопителей
Summary(tr):	Eject yeteneПi olan aygЩtlarЩ kontrol eder
Summary(uk):	Програма, що виштовху╓ зм╕нн╕ нос╕╖ з накопичувач╕в
Name:		eject
Version:	2.0.12
Release:	5
License:	GPL
Group:		Applications/System
Source0:	http://members.home.net/jefftranter/%{name}-%{version}.tar.gz
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-DESTDIR_fix.patch
URL:		http://sourceforge.net/projects/eject/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de
Dieses Programm ermЖglicht auf SPARC-Rechnern das Auswerfen von
DatentrДgern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l es
Este programa permite al usuario expulsar media que es autoexpulsable
como CD-ROMs, drives Jaz y Zip y floppy drives en mАquinas SPARC.

%description -l fr
Ce programme permet Ю l'utilisateur d'Иjecter un support autoИjectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l pl
Program do automatycznego otwierania szuflad w urz╠dzeniach CDROM,
Jaz, ZIP floppy (na maszynach SPARC) oraz innych.

%description -l pt_BR
Este programa permite ao usuАrio ejetar mМdia que И auto-ejetАvel como
CD-ROMs, drives Jaz e Zip e floppy drives em mАquinas SPARC.

%description -l ru
Эта программа позволяет пользователю выталкивать сменные носители из
накопителей, поддерживающих программный eject (такие как CD-ROMы,
Iomega Jaz или Zip диски, флоппи-диски на SPARC-машинах). Eject может
также управлять некоторыми CD ченджерами.

%description -l tr
Bu yazЩlЩm paketi ile kullanЩcЩya 'eject' yeteneПi olan aygЩtlarЩ
kontrol olanaПЩ verilmektedir. Bu yeteneПi olan aygЩtlar arasЩnda
CD-ROM'lar, Zip sЭrЭcЭleri ve bazЩ disket sЭrЭcЭleri yer alЩr.

%description -l uk
Ця програма дозволя╓ користувачев╕ виштовхувати зм╕нн╕ нос╕╖ з
накопичувач╕в, що п╕дтримують програмний eject (так╕ як CD-ROMи,
Iomega Jaz чи Zip диски, флоп╕-диски на SPARC-машинах). Eject може
також управляти деякими CD ченджерами

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
gettextize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf AUTHORS ChangeLog NEWS PORTING PROBLEMS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
