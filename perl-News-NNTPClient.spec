%include	/usr/lib/rpm/macros.perl
Summary:	News::NNTPClient perl module
Summary(pl):	Modu� perla News::NNTPClient
Name:		perl-News-NNTPClient
Version:	0.37
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/News/NNTPClient-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
Obsoletes:	perl-NNTPClient
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::NNTPClient - a client interface to NNTP.

%description -l pl
News::NNTPClient - interfejs klienta NNTP.

%prep
%setup -q -n NNTPClient-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install demos/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/News/NNTPClient.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
