#
# Conditional build:
%bcond_with	tests	# perform "make test" (uses network!)

%define		pdir	News
%define		pnam	NNTPClient
%include	/usr/lib/rpm/macros.perl
Summary:	News::NNTPClient perl module
Summary(pl.UTF-8):	Moduł perla News::NNTPClient
Name:		perl-News-NNTPClient
Version:	0.37
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/News/NNTPClient-%{version}.tar.gz
# Source0-md5:	1b0257d13f38d2b71bb85d5ac76f5fd1
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/News-NNTPClient/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-NNTPClient
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::NNTPClient - a client interface to NNTP.

%description -l pl.UTF-8
News::NNTPClient - interfejs klienta NNTP.

%prep
%setup -q -n NNTPClient-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/News/NNTPClient.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
