#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Filesys
%define	pnam	Virtual-Async
%include	/usr/lib/rpm/macros.perl
Summary:	Filesys::Virtual::Async - Base class for non blocking virtual filesystems
Name:		perl-Filesys-Virtual-Async
Version:	0.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Filesys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	635bf2e6679b231c48684ef020f98880
URL:		http://search.cpan.org/dist/Filesys-Virtual-Async/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of Filesys::Virtual::Async is to provide an interface like
IO::AIO for a non blocking virtual filesystem

This is a base class, see the SEE ALSO section below

This module is still in flux to an extent. If you'd like to suggest
changes, please drop in the irc channel #poe on irc.perl.org and speak
with xantus[] or Apocalypse

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Filesys/Virtual/*.pm
#%%{perl_vendorlib}/Filesys/Virtual/Async
%{_mandir}/man3/*
