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
Version:	2.0.13
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.pobox.com/~tranter/%{name}-%{version}.tar.gz
# Source0-md5: b796ad77beb4e7bdd08d6149701ab778
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5: dd66d948c94fe0f0b4483c51873e6e20
Source2:	%{name}-pl.po
Patch0:		%{name}-gettext.patch
URL:		http://eject.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
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

# standardize locale names
mv -f po/{de_DE,de}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{ja_JP.eucJP,ja}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

cp %{SOURCE2} po/pl.po

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS PORTING PROBLEMS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(pl) %{_mandir}/pl/man1/*
