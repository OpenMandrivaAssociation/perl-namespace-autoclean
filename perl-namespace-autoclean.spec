%define upstream_name    namespace-autoclean
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Keep imports out of your namespace 
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/namespace/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(B::Hooks::EndOfScope)
BuildRequires: perl(Class::MOP)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires: perl(namespace::clean)
Provides: perl(namespace::autoclean)

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

The 'namespace::autoclean' pragma will remove all imported symbols at the
end of the current package's compile cycle. Functions called in the package
itself will still be bound by their name, but they won't show up as methods
on your class or instances.

This module is very similar to namespace::clean, except it will clean all
imported functions, no matter if you imported them before or after you
'use'd the pagma. It will also not touch anything that looks like a method,
according to 'Class::MOP::Class::get_method_list'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

