%define		namesrc	settings
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - Settings
Summary(pl.UTF-8):	Wtyczka do Cacti - Ustawienia
Name:		cacti-plugin-settings
Version:	0.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mirror.cactiusers.org/downloads/plugins/%{namesrc}-%{version}.zip
# Source0-md5:	331f316ab5ee54ada0a0458ec52b075d
URL:		http://www.cactiusers.org/
BuildRequires:	rpm-perlprov
Requires:	cacti
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin houses common settings and functions used by different plugins.

%description -l pl.UTF-8
Wtyczka do Cacti - 

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -aRf * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE  
%{webcactipluginroot}
