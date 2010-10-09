%define	oname	nokogiri

Summary:	A HTML, XML, SAX, and Reader parser written in ruby
Name:		rubygem-%{oname}
Version:	1.4.3.1
Release:	%mkrel 1
License:	MIT
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems ruby-devel libxslt-devel
Requires:	ruby

%description
Nokogiri (鋸) is a HTML, XML, SAX, and Reader parser. Among Nokogiri's many
features is the ability to search documents via XPath or CSS3 selectors.
XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/{cache,gems/%{oname}-%{version}/ext}
mv %{buildroot}%{ruby_gemdir}/bin %{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_bindir}/nokogiri

