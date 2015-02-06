%define name		ocamldot
%define version		1.0
%define release		7

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	OCaml program dependency graph generator
Source: 	http://www.research.att.com/~trevor/ocamldot/%{name}.tar.bz2
URL:		http://www.research.att.com/~trevor/ocamldot
License:	Public Domain
Group:		Development/Other
BuildRequires:	ocaml
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Ocamldot generates program dependency graphs for ocaml programs.

%prep
%setup -q -n %{name}

%build
ocamllex ocamldot.mll
ocamlopt -o %{name} ocamldot.ml

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-6mdv2010.0
+ Revision: 430192
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 254192
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Dec 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2008.1
+ Revision: 135994
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Aug 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2007.0
- Rebuild

* Wed Mar 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdk
- first mdk release

