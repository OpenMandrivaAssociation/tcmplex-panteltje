Name:		tcmplex-panteltje
Version:	0.4.7
Release:	%mkrel 6
Epoch:		0
Summary:	Audio/Video multiplexer
License:	GPL
Group:		Video
URL:		http://panteltje.com/panteltje/dvd/
Source0:	http://panteltje.com/panteltje/dvd/tcmplex-panteltje-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
tcmplex-pantelje is an audio/video multiplexer from the transcode
distribution which has been re-written to support up to 8 audio
channels.

%prep
%setup -q
%{__perl} -pi -e 's/-O2/%{optflags}/' Makefile

%build
%{make} CC="%{__cc}"

%install
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -p -m 755 %{name} %{buildroot}%{_bindir}/%{name}
%{__ln_s} %{name} %{buildroot}%{_bindir}/tcmplex

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(0644,root,root,0755)
%doc CHANGES COPYRIGHT LICENSE README %{name}-%{version}.lsm
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/tcmplex
