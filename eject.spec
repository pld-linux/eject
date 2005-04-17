Summary:	ejects ejectable media and controls auto ejection
Summary(de):	wirft austauschbare Datenträger aus und steuert Auswurf
Summary(es):	Expulsa medias expulsables y controla autoexpulsión
Summary(fr):	éjecte un support éjectable et commande l'éjection automatique
Summary(pl):	Eject otwieranie szuflad CDROM, Jaz, ZIP i innych
Summary(pt_BR):	Ejeta mídias ejetáveis e controla auto-ejeção
Summary(ru):	ðÒÏÇÒÁÍÍÁ, ×ÙÔÁÌËÉ×ÁÀÝÁÑ ÓÍÅÎÎÙÅ ÎÏÓÉÔÅÌÉ ÉÚ ÎÁËÏÐÉÔÅÌÅÊ
Summary(tr):	Eject yeteneði olan aygýtlarý kontrol eder
Summary(uk):	ðÒÏÇÒÁÍÁ, ÝÏ ×ÉÛÔÏ×ÈÕ¤ ÚÍ¦ÎÎ¦ ÎÏÓ¦§ Ú ÎÁËÏÐÉÞÕ×ÁÞ¦×
Name:		eject
Version:	2.0.13
Release:	5
License:	GPL
Group:		Applications/System
Source0:	http://www.pobox.com/~tranter/%{name}-%{version}.tar.gz
# Source0-md5:	b796ad77beb4e7bdd08d6149701ab778
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	dd66d948c94fe0f0b4483c51873e6e20
Source2:	%{name}-pl.po
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-po.patch
Patch3:		%{name}-FHS.patch
Patch4:		%{name}-symlink.patch
URL:		http://eject.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows the user to eject media that is autoejecting like
CD-ROMs, Jaz and Zip drives, and floppy drives on SPARC machines.

%description -l de
Dieses Programm ermöglicht auf SPARC-Rechnern das Auswerfen von
Datenträgern wie CD-ROMs, Jaz-, Zip- und Floppy-Disketten, die
normalerweise automatisch ausgeworfen werden.

%description -l es
Este programa permite al usuario expulsar media que es autoexpulsable
como CD-ROMs, drives Jaz y Zip y floppy drives en máquinas SPARC.

%description -l fr
Ce programme permet à l'utilisateur d'éjecter un support autoéjectable
comme les CD-ROM, les lecteurs Zip et Jaz, et les disquettes sur les
SPARC.

%description -l pl
Program do automatycznego otwierania szuflad w urz±dzeniach CDROM,
Jaz, ZIP floppy (na maszynach SPARC) oraz innych.

%description -l pt_BR
Este programa permite ao usuário ejetar mídia que é auto-ejetável como
CD-ROMs, drives Jaz e Zip e floppy drives em máquinas SPARC.

%description -l ru
üÔÁ ÐÒÏÇÒÁÍÍÁ ÐÏÚ×ÏÌÑÅÔ ÐÏÌØÚÏ×ÁÔÅÌÀ ×ÙÔÁÌËÉ×ÁÔØ ÓÍÅÎÎÙÅ ÎÏÓÉÔÅÌÉ ÉÚ
ÎÁËÏÐÉÔÅÌÅÊ, ÐÏÄÄÅÒÖÉ×ÁÀÝÉÈ ÐÒÏÇÒÁÍÍÎÙÊ eject (ÔÁËÉÅ ËÁË CD-ROMÙ,
Iomega Jaz ÉÌÉ Zip ÄÉÓËÉ, ÆÌÏÐÐÉ-ÄÉÓËÉ ÎÁ SPARC-ÍÁÛÉÎÁÈ). Eject ÍÏÖÅÔ
ÔÁËÖÅ ÕÐÒÁ×ÌÑÔØ ÎÅËÏÔÏÒÙÍÉ CD ÞÅÎÄÖÅÒÁÍÉ.

%description -l tr
Bu yazýlým paketi ile kullanýcýya 'eject' yeteneði olan aygýtlarý
kontrol olanaðý verilmektedir. Bu yeteneði olan aygýtlar arasýnda
CD-ROM'lar, Zip sürücüleri ve bazý disket sürücüleri yer alýr.

%description -l uk
ãÑ ÐÒÏÇÒÁÍÁ ÄÏÚ×ÏÌÑ¤ ËÏÒÉÓÔÕ×ÁÞÅ×¦ ×ÉÛÔÏ×ÈÕ×ÁÔÉ ÚÍ¦ÎÎ¦ ÎÏÓ¦§ Ú
ÎÁËÏÐÉÞÕ×ÁÞ¦×, ÝÏ Ð¦ÄÔÒÉÍÕÀÔØ ÐÒÏÇÒÁÍÎÉÊ eject (ÔÁË¦ ÑË CD-ROMÉ,
Iomega Jaz ÞÉ Zip ÄÉÓËÉ, ÆÌÏÐ¦-ÄÉÓËÉ ÎÁ SPARC-ÍÁÛÉÎÁÈ). Eject ÍÏÖÅ
ÔÁËÏÖ ÕÐÒÁ×ÌÑÔÉ ÄÅÑËÉÍÉ CD ÞÅÎÄÖÅÒÁÍÉ

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# standardize locale names
mv -f po/{de_DE,de}.po
mv -f po/{fr_FR,fr}.po
mv -f po/{ja_JP.eucJP,ja}.po
mv -f po/{zh_TW.Big5,zh_TW}.po

cp %{SOURCE2} po/pl.po

echo "de fr ja pl zh_TW" >> po/LINGUAS
echo "eject.c\n i18n.h\n volname.c" >> po/POTFILES.in

%build
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
