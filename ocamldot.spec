%define name		ocamldot
%define version		1.0
%define release		%mkrel 5

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

